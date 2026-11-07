import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from parse_and_build_dataset import parse_financial_rows, parse_number, detect_unit_multiplier


def test_missing_is_not_zero_or_parent_profit():
    f = parse_financial_rows([
        ('Finansal Durum Tablosu', None, None),
        ('Ticari Alacaklar', 10, None),
        ('ÖZKAYNAKLAR', 40, None),
        ('Gelir Tablosu', None, None),
        ('DÖNEM KARI/ZARARI', 12, None),
    ], 1)
    assert f['T09_ticari_alacaklar'] is None
    assert f['T14_ana_ortakliga_ait_ozkaynaklar'] is None
    assert f['T07_ana_ortaklik_net_kari_ytd'] is None


def test_arbitrary_last_cash_flow_line_is_not_total():
    f = parse_financial_rows([
        ('Nakit Akım Tablosu', None, None),
        ('İşletme faaliyetlerine ilişkin nakit', None, None),
        ('Amortisman gideri', 50, None),
    ], 1)
    assert f['T15_isletme_nakit_akisi_ytd'] is None


def test_numbers_and_unknown_units():
    assert parse_number('(1.234,56)') == -1234.56
    assert parse_number('Dipnot 3-4') is None
    assert parse_number('31.03.2016') is None
    assert pd.isna(detect_unit_multiplier('USD')[1])
    assert pd.isna(detect_unit_multiplier('')[1])


def test_flow_difference_requires_compatible_scope():
    from rebuild_dataset import quarterize
    d = pd.DataFrame({
        'ticker': ['A'] * 4, 'year': [2020] * 4, 'quarter': [1, 2, 3, 4],
        'consolidation': ['solo', 'consolidated', 'consolidated', 'consolidated'],
        'currency': ['TRY'] * 4, 'price_level_date': ['nominal'] * 4,
        'available_at': ['2020-05-01', '2020-08-01', '2020-11-01', '2021-03-01'],
        'revenue_ytd': [10, 30, 60, 100], 'revenue_3m_raw': [None]*4,
    })
    q = quarterize(d, 'revenue')
    assert q.tolist()[0] == 10
    assert pd.isna(q.tolist()[1])
    assert q.tolist()[2:] == [30, 40]


def test_feature_cutoff_excludes_target_and_late_report():
    from rebuild_dataset import select_reference
    d = pd.DataFrame({
        'ticker': ['A', 'A'], 'period_end_date': ['2019-12-31', '2020-03-31'],
        'available_at': ['2020-03-01', '2020-05-15'],
        'source_vintage_status': ['unverified', 'unverified'],
        'T11_toplam_varliklar': [100, 200],
    })
    assert select_reference(d, 'A', '2020-03-31', '2020-03-31') is None
    assert select_reference(d, 'A', '2019-12-31', '2020-03-31') is None


def test_verified_report_must_also_pass_date_cutoff():
    from rebuild_dataset import select_reference
    d=pd.DataFrame({
        'ticker':['A','A'], 'period_end_date':['2019-12-31','2020-03-31'],
        'available_at':['2020-03-01','2020-05-15'],
        'source_vintage_status':['disclosure_id_linked']*2,
        'quality_status':['source_extracted']*2,
        'T11_toplam_varliklar':[100,999999],
    })
    assert select_reference(d,'A','2019-12-31','2020-03-31').T11_toplam_varliklar==100
    assert select_reference(d,'A','2020-03-31','2020-03-31') is None


def test_correction_is_bound_to_original_and_evidence(tmp_path,monkeypatch):
    import hashlib
    import rebuild_dataset as m
    monkeypatch.setattr(m,'ROOT',tmp_path)
    source=tmp_path/'source.xls'
    source.write_bytes(b'original')
    evidence=tmp_path/'evidence.pdf'
    evidence.write_bytes(b'evidence')
    spec={'original_file':'source.xls','original_sha256':hashlib.sha256(b'original').hexdigest(),
          'path':'evidence.pdf','sha256':hashlib.sha256(b'evidence').hexdigest()}
    m.validate_correction(spec,source,b'original')
    with pytest.raises(ValueError,match='original source hash'):
        m.validate_correction(spec,source,b'changed')
    evidence.write_bytes(b'changed')
    with pytest.raises(ValueError,match='evidence'):
        m.validate_correction(spec,source,b'original')


def test_direct_three_month_reference_does_not_need_unverified_prior_ytd():
    from rebuild_dataset import build_features
    d=pd.DataFrame({
        'ticker':['A','A'], 'year':[2016,2016], 'quarter':[2,3],
        'observation_period':['2016Q2','2016Q3'],
        'period_end_date':['2016-06-30','2016-09-30'],
        'available_at':['2016-08-01','2016-11-01'],
        'source_vintage_status':['disclosure_id_linked']*2,
        'quality_status':['source_extracted']*2,
        'T01_hasilat_ceyrek':[123,999999],
        'T01_hasilat_available_at':['2016-08-01','2016-11-01'],
        'T01_hasilat_quarter_method':['direct_3m']*2,
    })
    f=build_features(d)
    assert f.loc[1,'q_minus_1_T01_hasilat_ceyrek']==123
    assert 'T01_hasilat_ceyrek' not in f


def test_paper_fields_keep_statement_scope_and_units():
    from rebuild_dataset import extract_extra
    out=extract_extra([
        ('Finansal Durum Tablosu',None,None),
        ('Ertelenmiş Vergi Varlıkları',12,None),
        ('Kontrol Gücü Olmayan Paylar',5,None),
        ('Gelir Tablosu',None,None),
        ('Kontrol Gücü Olmayan Paylar',99,None),
        ('Sürdürülen Faaliyetler Vergi Öncesi Karı/Zararı',8,3),
    ],1000)
    assert out['paper2019_ertelenmis_vergi_varliklari']==12000
    assert out['paper2019_kontrol_gucu_olmayan_paylar']==5000
    assert out['paper2019_vergi_oncesi_kar_ytd']==8000
    assert out['paper2019_vergi_oncesi_kar_3m_raw']==3000


def test_source_expense_sign_and_separate_service_revenue():
    from rebuild_dataset import reconcile_source_conventions
    f={'T01_hasilat_ytd':5089535000,'T02_satislarin_maliyeti_ytd':4786556000,
       'T03_brut_kar_ytd':324652000}
    reconcile_source_conventions(f,[('Hizmet Gelirleri',21673,None)],1000)
    assert f['T02_satislarin_maliyeti_ytd']==-4786556000
    assert f['reported_cogs_ytd']==4786556000
    assert f['T01_hasilat_ytd']==5111208000
    assert f['reported_sales_revenue_ytd']==5089535000
    # Services already contained in reported revenue must not be counted twice.
    f={'T01_hasilat_ytd':100,'T02_satislarin_maliyeti_ytd':-80,'T03_brut_kar_ytd':20}
    reconcile_source_conventions(f,[('Hizmet Gelirleri',10,None)],1)
    assert f['T01_hasilat_ytd']==100

