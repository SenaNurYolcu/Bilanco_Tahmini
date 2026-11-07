"""Reproducible financial snapshot, source facts, coverage and dated references.

The snapshot is an observation table, NOT a ready-made training matrix. Unknown
vintages are excluded from strict historical features. No imputation is applied.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from fetch_kap_financials_2010_2020 import SELECTED_COMPANIES
from parse_and_build_dataset import (
    extract_rows_from_biff8, extract_rows_from_html_xls, parse_financial_rows,
    normalize_tr, detect_unit_multiplier, load_catalog_dates,
)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
FLOW_BASES = ['T01_hasilat', 'T02_satislarin_maliyeti', 'T03_brut_kar',
              'T04_esas_faaliyet_kari', 'T05_finansman_gideri',
              'T06_vergi_gideri_geliri', 'T07_donem_net_kari',
              'T07_ana_ortaklik_net_kari', 'F08_finansman_geliri',
              'T15_isletme_nakit_akisi', 'T16_yatirim_nakit_akisi',
              'T17_finansman_nakit_akisi', 'F15_capex_nakit',
              'F16_ar_ge_gideri', 'F16_genel_yonetim_gideri',
              'F16_pazarlama_gideri', 'F15_amortisman_itfa']
BALANCE = ['T08_nakit_ve_nakit_benzerleri', 'T09_ticari_alacaklar',
           'T10_stoklar', 'T11_toplam_varliklar', 'T12_finansal_borclar',
           'T13_toplam_yukumlulukler', 'T14_toplam_ozkaynaklar']
VERIFIED_VINTAGES = {'disclosure_id_linked'}


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def write_csv(frame, path):
    """Single canonical content; replace each file only after a full write."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    frame.to_csv(tmp, index=False, encoding='utf-8-sig')
    tmp.replace(path)


def extract_extra(rows, mult):
    """Exact statement labels only; no arbitrary CF leaf is a total."""
    out = {}
    section = 'BS'
    bs = 'current'
    capex_combined, capex_parts = None, {}
    direct = {
        'maddi duran varliklar': 'F15_maddi_duran_varliklar',
        'maddi olmayan duran varliklar': 'F15_maddi_olmayan_duran_varliklar',
        'sozlesme varliklari': 'F17_sozlesme_varliklari',
        'sozlesme yukumlulukleri': 'F18_sozlesme_yukumlulukleri',
        'ertelenmis gelirler': 'F18_ertelenmis_gelirler',
        'alinan siparis avanslari': 'F18_alinan_siparis_avanslari',
        'ertelenmis vergi varligi': 'paper2019_ertelenmis_vergi_varliklari',
        'ertelenmis vergi varliklari': 'paper2019_ertelenmis_vergi_varliklari',
        'kontrol gucu olmayan paylar': 'paper2019_kontrol_gucu_olmayan_paylar',
        'azınlik paylari': 'paper2019_kontrol_gucu_olmayan_paylar',
        'azinlik paylari': 'paper2019_kontrol_gucu_olmayan_paylar',
        'finansal duran varliklar': 'paper2019_finansal_duran_varliklar',
        'odenecek vergi ve yasal yukumlulukler': 'paper2019_odenecek_vergi_yasal_yukumlulukler',
    }
    flow = {
        'arastirma ve gelistirme giderleri (-)': 'F16_ar_ge_gideri',
        'arastirma ve gelistirme giderleri': 'F16_ar_ge_gideri',
        'genel yonetim giderleri (-)': 'F16_genel_yonetim_gideri',
        'pazarlama, satis ve dagitim giderleri (-)': 'F16_pazarlama_gideri',
        'pazarlama giderleri (-)': 'F16_pazarlama_gideri',
        'amortisman ve itfa gideri ile ilgili duzeltmeler': 'F15_amortisman_itfa',
        'amortisman ve itfa giderleri ile ilgili duzeltmeler': 'F15_amortisman_itfa',
        'surdurulen faaliyetler vergi oncesi kari/zarari': 'paper2019_vergi_oncesi_kar',
        'surdurulen faaliyetler vergi oncesi kari (zarari)': 'paper2019_vergi_oncesi_kar',
        'surdurulen faaliyetler vergi oncesi kari veya zarari': 'paper2019_vergi_oncesi_kar',
        'diger faaliyet giderleri (-)': 'paper2019_diger_faaliyet_giderleri',
        'diger faaliyetlerden zararlar ve giderler (-)': 'paper2019_diger_faaliyet_giderleri',
    }
    def store_flow(key, y, q):
        if key + '_ytd' not in out:
            out[key + '_ytd'] = y * mult
            out[key + '_3m_raw'] = q * mult if q is not None else None
    for label, y, q in rows:
        n = normalize_tr(label).lstrip('- ').strip()
        if n in ('bilanco', 'finansal durum tablosu', 'finansal durum tablosu (bilanco)'):
            section = 'BS'
        elif n in ('gelir tablosu', 'kar veya zarar tablosu', 'kapsamli gelir tablosu',
                   'kar veya zarar ve diger kapsamli gelir tablosu', 'kar veya zarar kismi'):
            section = 'IS'
        elif n.startswith(('nakit akis tablosu', 'nakit akim tablosu')):
            section = 'CF'
        elif 'ozkaynak' in n and 'degisim tablosu' in n:
            section = 'EQ'
        if section == 'BS':
            if n in ('donen varliklar', 'duran varliklar', 'kisa vadeli yukumlulukler', 'uzun vadeli yukumlulukler'):
                bs = n.replace(' ', '_')
            if y is not None and n in direct:
                key = direct[n]
                if key.startswith(('F17_', 'F18_')):
                    key += '_' + bs
                out.setdefault(key, y * mult)
        if y is None:
            continue
        if section == 'IS' and n in flow:
            store_flow(flow[n], y, q)
        if section == 'CF':
            if n in flow:
                store_flow(flow[n], y, q)
            # Tax/interest lines and operating profit adjustments are not CFO.
            if any(z in n for z in ('saglanan', 'kullanilan', 'elde edilen', 'kaynaklanan')) and 'nakit' in n:
                if n.startswith(('isletme faaliyetlerinden', 'isletme faaliyetlerinde', 'esas faaliyetlerden', 'esas faaliyetlere iliskin')):
                    out['T15_isletme_nakit_akisi_ytd'] = y * mult
                elif n.startswith(('yatirim faaliyetlerinden', 'yatirim faaliyetlerinde')):
                    out['T16_yatirim_nakit_akisi_ytd'] = y * mult
                elif n.startswith(('finansman faaliyetlerinden', 'finansman faaliyetlerinde', 'finansal faaliyetlerden', 'finansal faaliyetlerde')):
                    out['T17_finansman_nakit_akisi_ytd'] = y * mult
            if n in ('maddi ve maddi olmayan duran varliklarin alimindan kaynaklanan nakit cikislari',
                     'maddi ve maddi olmayan duran varlik alimlari'):
                capex_combined = y * mult
            elif n in ('maddi duran varlik alimlarina iliskin nakit cikislari',
                       'maddi olmayan duran varlik alimlarina iliskin nakit cikislari'):
                capex_parts[n] = y * mult
    if capex_combined is not None:
        out['F15_capex_nakit_ytd'] = capex_combined
    elif len(capex_parts) == 2:
        out['F15_capex_nakit_ytd'] = sum(capex_parts.values())
    return out


def corrections():
    p = DATA / 'kap_refresh_manifest.json'
    if not p.exists():
        return {}
    j = json.loads(p.read_text())
    return {(s['ticker'], int(s['year']), int(s['quarter'])): s
            for s in j.get('sources', []) if s.get('status') == 'verified'}


def reconcile_source_conventions(fin, rows, mult):
    """Keep original signs and separately reported goods/service components.

    Add services only when the source explicitly reports them and the commercial
    gross profit identity independently confirms the components do not overlap.
    """
    for suffix in ['ytd','3m_raw']:
        col='T02_satislarin_maliyeti_'+suffix
        value=fin.get(col)
        if value is not None:
            fin['reported_cogs_'+suffix]=value
            fin[col]=-abs(value)
    service=next(((y,q) for label,y,q in rows
                  if normalize_tr(label)=='hizmet gelirleri' and y is not None),None)
    fin['revenue_mapping']='reported_revenue'
    if service is None:
        return
    for n,suffix in enumerate(['ytd','3m_raw']):
        r,c,g=(fin.get(k+suffix) for k in ['T01_hasilat_','T02_satislarin_maliyeti_','T03_brut_kar_'])
        s=service[n]*mult if service[n] is not None else None
        if all(v is not None for v in [r,c,g,s]) and abs(g-r-c)>5*mult and abs(g-r-c-s)<=5*mult:
            fin['reported_sales_revenue_'+suffix]=r
            fin['separate_service_revenue_'+suffix]=s
            fin['T01_hasilat_'+suffix]=r+s
            fin['revenue_mapping']='goods_plus_separate_services_gross_identity_confirmed'


def validate_correction(record, source_file, source_bytes):
    if record.get('original_file') != str(source_file.relative_to(ROOT)):
        raise ValueError('Correction source file mismatch')
    if record.get('original_sha256') != hashlib.sha256(source_bytes).hexdigest():
        raise ValueError('Correction original source hash mismatch; re-verify report')
    evidence = ROOT / record.get('path', '')
    if not evidence.is_file() or record.get('sha256') != hashlib.sha256(evidence.read_bytes()).hexdigest():
        raise ValueError('Correction evidence missing or hash mismatch')


def quarterize(df, base):
    y = df[base + '_ytd']
    grouped = df.groupby(['ticker', 'year'], sort=False)
    compatible = grouped['quarter'].shift().eq(df.quarter - 1)
    for col in ['consolidation', 'currency', 'price_level_date']:
        compatible &= grouped[col].shift().eq(df[col]) & df[col].notna() & df[col].ne('')
    diff = (y - grouped[base + '_ytd'].shift()).where(compatible)
    raw = df.get(base + '_3m_raw', pd.Series(np.nan, index=df.index))
    return y.where(df.quarter.eq(1), raw.where(raw.notna(), diff))


def quality_issues(df):
    issues = []
    def add(i, code, col, value):
        issues.append({'ticker': df.at[i, 'ticker'], 'year': int(df.at[i, 'year']),
                       'quarter': int(df.at[i, 'quarter']), 'code': code,
                       'field': col, 'value': value, 'source_file': df.at[i, 'source_file']})
    assets = df.T11_toplam_varliklar
    residual = assets - df.T13_toplam_yukumlulukler - df.T14_toplam_ozkaynaklar
    tolerance = pd.concat([assets.abs() * 1e-5, pd.Series(10., index=df.index),
                           df.unit_multiplier.fillna(1) * 5], axis=1).max(axis=1)
    for i in df.index[residual.abs().gt(tolerance)]:
        add(i, 'balance_identity_mismatch', 'T11_toplam_varliklar', float(residual[i]))
    for result_col,left,right,code in [
        ('T11_toplam_varliklar','donen_varliklar','duran_varliklar','asset_subtotals_mismatch'),
        ('T13_toplam_yukumlulukler','kisa_vadeli_yukumlulukler','uzun_vadeli_yukumlulukler','liability_subtotals_mismatch'),
        ('T03_brut_kar_ytd','T01_hasilat_ytd','T02_satislarin_maliyeti_ytd','gross_profit_identity_review'),
    ]:
        difference=df[result_col]-df[left]-df[right]
        for i in df.index[difference.abs().gt(tolerance)]:
            add(i,code,result_col,float(difference[i]))
    for col in BALANCE + [b + '_ytd' for b in FLOW_BASES]:
        if col not in df:
            continue
        if col != 'T11_toplam_varliklar':
            for i in df.index[df[col].abs().gt(assets.abs() * 100) & assets.gt(0)]:
                add(i, 'extreme_relative_to_assets_review', col, float(df.at[i, col]))
    ratio = assets / df.groupby('ticker').T11_toplam_varliklar.shift()
    for i in df.index[(ratio.gt(100) | ratio.lt(.01)) & ratio.gt(0)]:
        add(i, 'asset_scale_break_review', 'T11_toplam_varliklar', float(assets[i]))
    return pd.DataFrame(issues, columns=['ticker','year','quarter','code','field','value','source_file'])


def build_financial_snapshot():
    first_dates, by_id = load_catalog_dates()
    edits = corrections()
    file_map = {}
    for p in sorted((DATA / 'kap_raw_xls').glob('*.xls')):
        m = re.fullmatch(r'([A-Z0-9]+)_(\d{4})_Q([1-4])(?:_(\d+))?\.xls', p.name)
        if m:
            t, y, q, disc = m.groups()
            file_map.setdefault((t,int(y),int(q)), []).append((p,disc or ''))
    records, raw_records = [], []
    for t, comp in SELECTED_COMPANIES.items():
        for y in range(2010,2021):
            for q in range(1,5):
                key = (t,y,q)
                candidates = file_map.get(key, [])
                # Multiple report versions remain a blocker, never silently last wins.
                period_end = pd.Period(f'{y}Q{q}', freq='Q').end_time.date().isoformat()
                row = dict(ticker=t, year=y, quarter=q, observation_period=f'{y}Q{q}',
                           period_end_date=period_end, company_name=comp['title'],
                           sector_group=comp['sector_group'], currency='TRY',
                           C01_sector_snapshot=comp['kap_sub_sector'],
                           C01_sector_vintage_status='current_static_unverified_history',
                           price_level_date='nominal_pre_2021_scope', available_at='',
                           first_published_at='', report_published_at='', disclosure_index='',
                           period_first_published_at=first_dates.get(key, ('',''))[0],
                           report_timezone='Europe/Istanbul',
                           source_file='', source_url='', source_sha256='', consolidation='',
                           original_unit='', unit_multiplier=np.nan,
                           source_vintage_status='unavailable_vintage', correction_source_url='',
                           quality_status='missing_source')
                if len(candidates) != 1:
                    row['quality_status'] = 'ambiguous_report_versions' if candidates else 'missing_source'
                    records.append(row)
                    continue
                fp, disc = candidates[0]
                content = fp.read_bytes()
                meta, rows = (extract_rows_from_biff8(fp) if content.startswith(b'\xd0\xcf\x11\xe0')
                              else extract_rows_from_html_xls(fp))
                unit, mult = detect_unit_multiplier(meta.get('original_unit',''))
                stamp = by_id.get(disc, '') if disc else meta.get('published_at_header','')
                # First release is a separate concept; retain the exact file's date.
                row.update(source_file=str(fp.relative_to(ROOT)), source_sha256=hashlib.sha256(content).hexdigest(),
                           source_url=f'https://www.kap.org.tr/tr/Bildirim/{disc}' if disc else
                           f'https://www.kap.org.tr/tr/api/financialTable/download/{y}/{q}',
                           disclosure_index=disc, original_unit=unit, unit_multiplier=mult,
                           consolidation=meta.get('consolidation',''),
                           report_published_at=stamp, available_at=stamp,
                           source_vintage_status='disclosure_id_linked' if disc and stamp else 'header_dated_archive_unverified')
                # A date is not enough to prove this is the first version.
                correction = edits.get(key)
                if correction:
                    validate_correction(correction, fp, content)
                    if correction.get('verified_unit_multiplier') is not None:
                        mult = float(correction['verified_unit_multiplier'])
                        row['unit_multiplier'] = mult
                    row['correction_source_url'] = correction['url']
                    row['source_vintage_status'] = 'historical_company_copy_unverified'
                    # Original report date doesn't date today's corrected PDF copy.
                    row['available_at'] = ''
                fin = parse_financial_rows(rows,mult)
                fin.update(extract_extra(rows,mult))
                reconcile_source_conventions(fin,rows,mult)
                # Correct dictionary IDs (F07 is tax, F08 is financing).
                for suffix in ['ytd','3m_raw']:
                    fin['F08_finansman_geliri_' + suffix] = fin.pop('F07_finansman_geliri_' + suffix, None)
                if correction:
                    fin.update(correction.get('field_overrides',{}))
                row.update(fin)
                # Date of the exact selected version; never borrow period's first date.
                row['first_published_at'] = stamp
                row['quality_status'] = 'source_extracted' if np.isfinite(mult) else 'unknown_unit'
                records.append(row)
                # Preserve ALL source rows, including blanks and corrupt originals.
                for n,(label,vy,vq) in enumerate(rows,1):
                    raw_records.append(dict(ticker=t,year=y,quarter=q,source_row=n,label=label,
                        original_ytd=vy,original_three_month=vq,original_unit=unit,
                        normalized_ytd=vy*mult if vy is not None else None,
                        normalization_status='verified_unit_correction' if correction and correction.get('verified_unit_multiplier') else 'reported_unit',
                        source_file=row['source_file'],source_sha256=row['source_sha256']))
    df = pd.DataFrame(records).sort_values(['ticker','year','quarter']).reset_index(drop=True)
    for base in FLOW_BASES:
        for suffix in ['ytd','3m_raw']:
            if base+'_'+suffix not in df:
                df[base+'_'+suffix] = np.nan
        df[base+'_ceyrek'] = quarterize(df,base)
        # Distinct date for a derived quarter needing two source reports.
        prev = df.groupby(['ticker','year']).available_at.shift()
        available = pd.concat([pd.to_datetime(df.available_at,errors='coerce'),
                               pd.to_datetime(prev,errors='coerce')],axis=1).max(axis=1)
        direct = df.quarter.eq(1) | df[base+'_3m_raw'].notna()
        df[base+'_quarter_method'] = np.where(df.quarter.eq(1),'direct_ytd_q1',
            np.where(df[base+'_3m_raw'].notna(),'direct_3m','difference'))
        df[base+'_available_at'] = pd.to_datetime(df.available_at,errors='coerce').where(direct,available)
        current_ok=df.source_vintage_status.isin(VERIFIED_VINTAGES) & df.available_at.ne('')
        previous_ok=current_ok.groupby([df.ticker,df.year]).shift(fill_value=False)
        df[base+'_historical_eligible']=current_ok & (direct | previous_ok)
        df.drop(columns=base+'_3m_raw',inplace=True)
    # No inferred EPS: weighted-average shares / nominal value are not available.
    df['hisse_basina_kar_missing_reason'] = 'weighted_average_shares_not_extracted'
    issues = quality_issues(df)
    bad = set(zip(issues.ticker,issues.year,issues.quarter)) if len(issues) else set()
    df['quality_status'] = [s if (t,y,q) not in bad else 'review_required'
                            for t,y,q,s in zip(df.ticker,df.year,df.quarter,df.quality_status)]
    return df, pd.DataFrame(raw_records), issues


def select_reference(df, ticker, period_end, cutoff):
    available = pd.to_datetime(df.available_at,errors='coerce')
    mask = (df.ticker.eq(ticker) & df.period_end_date.eq(period_end) &
            available.le(pd.Timestamp(cutoff)) &
            df.source_vintage_status.isin(VERIFIED_VINTAGES))
    if 'quality_status' in df:
        mask &= df.quality_status.eq('source_extracted')
    valid = df.loc[mask]
    return valid.iloc[0] if len(valid)==1 else None


def build_features(df):
    """q-1/q-4 references available at q end; target values stay in labels."""
    rows=[]
    lookup = {(r.ticker,r.period_end_date):r for _,r in df.iterrows()}
    def reference_at(ticker, period, cutoff):
        r=lookup.get((ticker,period))
        if r is None or r.source_vintage_status not in VERIFIED_VINTAGES or r.quality_status!='source_extracted':
            return None
        stamp=pd.to_datetime(r.available_at,errors='coerce')
        return r if pd.notna(stamp) and stamp <= pd.Timestamp(cutoff) else None
    fields = BALANCE + [b+'_ceyrek' for b in FLOW_BASES]
    for _, target in df.iterrows():
        period = pd.Period(target.observation_period,freq='Q')
        out = dict(ticker=target.ticker,observation_period=target.observation_period,
                   target_period_end=target.period_end_date,forecast_at=target.period_end_date,
                   quarter=target.quarter)
        for lag in [1,4]:
            p = (period-lag).end_time.date().isoformat()
            reference = reference_at(target.ticker,p,target.period_end_date)
            prefix=f'q_minus_{lag}_'
            out[prefix+'reference_period_end']=p
            out[prefix+'available_at']=reference.available_at if reference is not None else ''
            out[prefix+'missing_reason']='' if reference is not None else 'unavailable_by_cutoff_or_unverified_vintage'
            for field in fields:
                value = reference.get(field,np.nan) if reference is not None else np.nan
                if reference is not None and field.endswith('_ceyrek'):
                    base = field[:-7]
                    if not bool(reference.get(base+'_historical_eligible',True)):
                        value=np.nan
                    if pd.isna(reference.get(base+'_available_at')) or pd.Timestamp(reference[base+'_available_at']) > pd.Timestamp(target.period_end_date):
                        value=np.nan
                    # Derived quarters also require the previous YTD version.
                    if reference.get(base+'_quarter_method') == 'difference':
                        previous_period=(pd.Period(reference.observation_period,freq='Q')-1).end_time.date().isoformat()
                        prev=reference_at(target.ticker,previous_period,target.period_end_date)
                        if prev is None:
                            value=np.nan
                out[prefix+field]=value
        # Ratios use only the q-1 report, never target-quarter assets.
        prefix='q_minus_1_'
        a=out.get(prefix+'T11_toplam_varliklar',np.nan)
        revenue=out.get(prefix+'T01_hasilat_ceyrek',np.nan)
        for fid,field in [('F03','T03_brut_kar_ceyrek'),('F04','T04_esas_faaliyet_kari_ceyrek'),('F05','T07_donem_net_kari_ceyrek')]:
            out[fid+'_margin']=out.get(prefix+field,np.nan)/revenue if pd.notna(revenue) and revenue>0 else np.nan
        for fid,field in [('F06','T15_isletme_nakit_akisi_ceyrek'),('F09','T08_nakit_ve_nakit_benzerleri'),
                          ('F10','T09_ticari_alacaklar'),('F11','T10_stoklar'),('F13','T12_finansal_borclar'),
                          ('F14','T14_toplam_ozkaynaklar')]:
            out[fid+'_over_assets']=out.get(prefix+field,np.nan)/a if pd.notna(a) and a>0 else np.nan
        rows.append(out)
    return pd.DataFrame(rows)


def attach_macro_snapshot(snapshot):
    """Latest-vintage observation summaries; names explicitly forbid PIT use."""
    path=DATA/'external/rebuilt/macro_observations.csv'
    if not path.exists():
        return snapshot
    obs=pd.read_csv(path)
    obs=obs.loc[obs.feature_id.ne('proxy_only')].copy()
    obs['period_end']=pd.to_datetime(obs.period_end,errors='coerce')
    quarter_rows=[]
    for period_end in sorted(snapshot.period_end_date.unique()):
        cutoff=pd.Timestamp(period_end)
        start=cutoff.to_period('Q').start_time
        part=obs.loc[obs.period_end.between(start,cutoff)]
        row={'period_end_date':period_end}
        for name,group in part.groupby('series_name'):
            last=group.sort_values('period_end').iloc[-1]
            column='snapshot_only_'+name
            row[column]=last.value
            row[column+'_observation_date']=last.period_end.date().isoformat()
        quarter_rows.append(row)
    result=snapshot.merge(pd.DataFrame(quarter_rows),on='period_end_date',how='left',validate='many_to_one')
    result['macro_snapshot_status']='latest_vintage_not_historical_model_inputs'
    return result


def attach_macro_features(features):
    from external_point_in_time import external_asof
    path=DATA/'external/rebuilt/macro_observations.csv'
    if not path.exists():
        return features
    obs=pd.read_csv(path)
    rows=[]
    # Join once per date, not once per company; no invented release lag.
    for cutoff in sorted(features.forecast_at.unique()):
        row={'forecast_at':cutoff}
        for name in obs.loc[obs.feature_id.ne('proxy_only'),'series_name'].unique():
            record=external_asof(obs,name,cutoff)
            row['macro_'+name]=record['value'] if record else np.nan
            row['macro_'+name+'_available_at']=record['available_at'] if record else ''
        row['macro_missing_reason']='unavailable_vintage'
        rows.append(row)
    return features.merge(pd.DataFrame(rows),on='forecast_at',how='left',validate='many_to_one')


FAMILY_FIELDS = {
    'F01':['T11_toplam_varliklar'], 'F02':['T01_hasilat_ceyrek'],
    'F03':['T02_satislarin_maliyeti_ceyrek','T03_brut_kar_ceyrek'],
    'F04':['T04_esas_faaliyet_kari_ceyrek'], 'F05':['T07_donem_net_kari_ceyrek'],
    'F06':['T15_isletme_nakit_akisi_ceyrek'], 'F07':['T06_vergi_gideri_geliri_ceyrek'],
    'F08':['T05_finansman_gideri_ceyrek','F08_finansman_geliri_ceyrek'],
    'F09':['T08_nakit_ve_nakit_benzerleri'], 'F10':['T09_ticari_alacaklar'],
    'F11':['T10_stoklar'], 'F12':['F12_ticari_borclar'], 'F13':['T12_finansal_borclar'],
    'F14':['T13_toplam_yukumlulukler','T14_toplam_ozkaynaklar'],
    'F15':['F15_maddi_duran_varliklar','F15_capex_nakit_ceyrek','F15_amortisman_itfa_ceyrek'],
    'F16':['F16_ar_ge_gideri_ceyrek','F16_genel_yonetim_gideri_ceyrek','F16_pazarlama_gideri_ceyrek'],
}


def build_coverage(df):
    registry=json.loads((ROOT/'docs/model_oncesi/degiskenler.json').read_text())
    results=[]
    for f in registry['features']:
        fid=f['id']
        fields=FAMILY_FIELDS.get(fid,[])
        if fid in ('F17','F18'):
            fields=[c for c in df if c.startswith(fid+'_')]
        values=[df[c].notna().sum() for c in fields if c in df]
        results.append(dict(feature_id=fid,label=f.get('label',f.get('name','')),
            priority=f.get('priority',''),mapped_columns='|'.join(fields),
            rows_with_any_component=int(df[[c for c in fields if c in df]].notna().any(axis=1).sum()) if values else 0,
            minimum_component_nonmissing=int(min(values)) if values else 0,
            total_company_quarters=len(df),
            status='partial_financial_mapping' if values and max(values)>0 else 'not_extracted',
            missing_reason='' if values and max(values)>0 else ('unavailable_vintage' if fid.startswith(('M','R')) else 'not_extracted'),
            note='Family coverage is not proof of full definition or historical availability.'))
    coverage=pd.DataFrame(results)
    path=DATA/'external/rebuilt/macro_observations.csv'
    coverage['source_observations_2010_2020']=0
    coverage['strict_source_observations_2010_2020']=0
    if path.exists():
        obs=pd.read_csv(path)
        obs=obs.loc[obs.period_end.between('2010-01-01','2020-12-31')]
        for fid,group in obs.groupby('feature_id'):
            mask=coverage.feature_id.eq(fid)
            coverage.loc[mask,'source_observations_2010_2020']=len(group)
            coverage.loc[mask,'strict_source_observations_2010_2020']=int(group.pit_eligible.astype(str).str.lower().eq('true').sum())
            coverage.loc[mask,'status']='macro_snapshot_only'
            coverage.loc[mask,'note']='Official observations retrieved; historical release/vintage unverified; strict model input remains missing.'
    coverage.loc[coverage.feature_id.eq('C01'),'status']='current_sector_snapshot_unverified_history'
    profile_path=DATA/'company_profile_pilot.csv'
    if profile_path.exists():
        profile=pd.read_csv(profile_path)
        for fid,group in profile.groupby('feature_id'):
            mask=coverage.feature_id.eq(fid)
            coverage.loc[mask,'status']='company_note_pilot_partial_snapshot'
            coverage.loc[mask,'source_observations_2010_2020']=len(group)
            coverage.loc[mask,'strict_source_observations_2010_2020']=0
            coverage.loc[mask,'note']='Small source-note pilot only; conflicting/disaggregated definitions preserved; original vintage unverified.'
    return coverage


def run():
    snapshot,raw,issues=build_financial_snapshot()
    snapshot=attach_macro_snapshot(snapshot)
    snapshot['label_historical_eligible']=snapshot.source_vintage_status.isin(VERIFIED_VINTAGES) & snapshot.quality_status.eq('source_extracted')
    canonical=DATA/'bist_bilanco_tahmini_2010_2020.csv'
    write_csv(snapshot,canonical)
    # Compatibility mirror is byte-for-byte identical; data/ is authoritative.
    (ROOT/canonical.name).write_bytes(canonical.read_bytes())
    write_csv(raw,DATA/'financial_source_rows.csv')
    write_csv(issues,DATA/'financial_quality_issues.csv')
    features=attach_macro_features(build_features(snapshot))
    write_csv(features,DATA/'model_features_point_in_time.csv')
    label_cols=['ticker','observation_period','available_at','source_vintage_status','quality_status',
                'label_historical_eligible']+BALANCE+[b+'_ceyrek' for b in FLOW_BASES]+[
                    b+s for b in FLOW_BASES for s in ['_available_at','_historical_eligible']]
    write_csv(snapshot[label_cols],DATA/'model_labels.csv')
    write_csv(build_coverage(snapshot),DATA/'feature_coverage.csv')
    summary=dict(generated_at=utc_now(),rows=len(snapshot),columns=len(snapshot.columns),
        source_rows=len(raw),issue_count=len(issues),
        linked_disclosure_vintages=int(snapshot.source_vintage_status.eq('disclosure_id_linked').sum()),
        financial_reference_rows=int(features.q_minus_1_available_at.ne('').sum()),
        canonical_sha256=hashlib.sha256(canonical.read_bytes()).hexdigest(),
        model_ready=False,reason='Coverage, historical vintages and source exceptions require review before training.')
    (DATA/'dataset_build_manifest.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__=='__main__':
    run()
