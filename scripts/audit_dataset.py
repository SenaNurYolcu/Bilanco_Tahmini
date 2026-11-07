"""Run after rebuild_dataset.py. Structural pass does not mean model ready."""
import hashlib
import json
import csv
from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]


def audit():
    data=ROOT/'data'
    snapshot=pd.read_csv(data/'bist_bilanco_tahmini_2010_2020.csv')
    features=pd.read_csv(data/'model_features_point_in_time.csv')
    labels=pd.read_csv(data/'model_labels.csv')
    checks={}
    checks['canonical_mirror_identical']=(data/'bist_bilanco_tahmini_2010_2020.csv').read_bytes()==(ROOT/'bist_bilanco_tahmini_2010_2020.csv').read_bytes()
    checks['unique_company_quarter']=not snapshot.duplicated(['ticker','year','quarter']).any()
    checks['expected_grid']=len(snapshot)==1320 and snapshot.ticker.nunique()==30
    checks['feature_label_keys_align']=features[['ticker','observation_period']].equals(labels[['ticker','observation_period']])
    checks['targets_not_unlagged_inputs']=not any(c.startswith('T') for c in features)
    financial_dates=[c for c in features if c.startswith('q_minus_') and c.endswith('_available_at')]
    checks['financial_availability_before_forecast']=all(
        (pd.to_datetime(features[c],errors='coerce').isna() |
         pd.to_datetime(features[c],errors='coerce').le(pd.to_datetime(features.forecast_at))).all()
        for c in financial_dates)
    checks['macro_snapshot_not_model_input']=not any(c.startswith('snapshot_only_') for c in features)
    corrected=snapshot.set_index(['ticker','year','quarter'])
    checks['thyao_2015q4_assets']=corrected.loc[('THYAO',2015,4),'T11_toplam_varliklar']==47638000000
    checks['thyao_2016q1_assets']=corrected.loc[('THYAO',2016,1),'T11_toplam_varliklar']==48349000000
    checks['karel_2012q1_operating_cf']=corrected.loc[('KAREL',2012,1),'T15_isletme_nakit_akisi_ytd']==11528269
    checks['toaso_2013q1_assets']=corrected.loc[('TOASO',2013,1),'T11_toplam_varliklar']==6266179000
    checks['toaso_2014q3_assets']=corrected.loc[('TOASO',2014,3),'T11_toplam_varliklar']==6550101000
    coverage=pd.read_csv(data/'feature_coverage.csv')
    registry=json.loads((ROOT/'docs/model_oncesi/degiskenler.json').read_text())
    checks['all_51_family_ids_reported']=set(coverage.feature_id)=={x['id'] for x in registry['features']} and len(coverage)==51
    macro=data/'external/rebuilt/macro_observations.csv'
    macro_count=0
    macro_total=0
    evds_numeric=0
    evds_downloaded=False
    if macro.exists():
        obs=pd.read_csv(macro,low_memory=False)
        macro_total=len(obs)
        historical=obs.loc[obs.period_end.between('2010-01-01','2020-12-31')]
        macro_count=len(historical)
        not_pit=historical.loc[~historical.pit_eligible.astype(str).str.lower().eq('true')]
        checks['unverified_macro_dates_not_fabricated']=not_pit.available_at.isna().all()
    evds_path=data/'external/rebuilt/evds/observations.csv'
    if evds_path.exists():
        evds=pd.read_csv(evds_path)
        evds_numeric=int(evds.value.notna().sum())
        evds_downloaded=evds.feature_id.nunique()==6
        checks['evds_six_macro_families_retrieved']=evds_downloaded
        evds_coverage=pd.read_csv(data/'external/rebuilt/evds/series_year_coverage.csv')
        monthly=evds_coverage.loc[evds_coverage.frequency.eq('monthly')]
        checks['evds_monthly_2010_2020_complete']=len(monthly)==66 and monthly.monthly_grid_complete.astype(str).str.lower().eq('true').all()
        checks['evds_observations_unique']=not evds.duplicated(['series_name','period_end']).any()
        expected=['USDTRY_TCMB_buying','EURTRY_TCMB_buying','M03_Ticari_Kredi_Faizi',
                  'M04_TUFE_YoY_EVDS','M05_YIUFE_YoY_EVDS','M06_SanayiUretimi_YoY']
        checks['evds_six_series_added_to_main_csv']=all(
            'snapshot_only_'+name in snapshot and snapshot['snapshot_only_'+name].notna().all()
            for name in expected)
        checks['evds_snapshots_excluded_from_historical_inputs']=not evds.pit_eligible.astype(str).str.lower().eq('true').any()
        receipt_manifest=json.loads((data/'external/rebuilt/evds/manifest.json').read_text())
        checks['evds_raw_receipt_hashes_match']=all(
            hashlib.sha256((data/'external/rebuilt/evds/raw'/
                (r['series_code'].replace('.','_')+'_'+str(r['requested_year'])+'.json')).read_bytes()).hexdigest()==r['sha256']
            for r in receipt_manifest['requests'])
        # Independent checks against original JSON response cells, not merged CSV.
        raw_dir=data/'external/rebuilt/evds/raw'
        credit=json.loads((raw_dir/'TP_KTF17_2010.json').read_text())['items']
        source_credit=[(pd.to_datetime(r['Tarih'],format='%d-%m-%Y'),r['TP_KTF17']) for r in credit
                       if r.get('TP_KTF17') not in (None,'','NA')]
        source_credit=[(d,float(v)) for d,v in source_credit if d<=pd.Timestamp('2010-03-31')]
        expected_credit=sorted(source_credit)[-1][1]
        quarter=snapshot.loc[snapshot.observation_period.eq('2010Q1')]
        checks['evds_credit_2010q1_matches_source_cell']=quarter['snapshot_only_M03_Ticari_Kredi_Faizi'].sub(expected_credit).abs().lt(1e-8).all()
        ip={}
        for year in [2009,2010]:
            records=json.loads((raw_dir/f'TP_TSANAYTKVM2021_BCD_{year}.json').read_text())['items']
            ip[year]=float(next(r['TP_TSANAYTKVM2021_BCD'] for r in records if r['Tarih']==f'{year}-3'))
        expected_ip=(ip[2010]/ip[2009]-1)*100
        checks['evds_industrial_yoy_matches_two_source_cells']=quarter['snapshot_only_M06_SanayiUretimi_YoY'].sub(expected_ip).abs().lt(1e-8).all()
    issues=pd.read_csv(data/'financial_quality_issues.csv')
    with open(data/'financial_source_rows.csv',encoding='utf-8-sig',newline='') as stream:
        source_row_count=sum(1 for _ in csv.reader(stream))-1
    result={'checks':{k:bool(v) for k,v in checks.items()},'structural_pass':all(checks.values()),
            'rows':len(snapshot),'columns':len(snapshot.columns),'companies':snapshot.ticker.nunique(),
            'financial_source_rows':source_row_count,
            'macro_observations_2010_2020':macro_count,'financial_quality_issues':len(issues),
            'evds_php_downloaded':evds_downloaded,'evds_numeric_records':evds_numeric,
            'model_ready':False,
            'limits':['Original report vintages not fully established',
                      'Company exposure profile extraction incomplete',
                      'EVDS original releases/vintages unverified' if evds_downloaded else 'Authenticated EVDS download not completed',
                      'No forecasting model trained or evaluated']}
    path=data/'dataset_audit.json'
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    targets=['T01_hasilat_ceyrek','T02_satislarin_maliyeti_ceyrek','T03_brut_kar_ceyrek',
             'T04_esas_faaliyet_kari_ceyrek','T05_finansman_gideri_ceyrek',
             'T06_vergi_gideri_geliri_ceyrek','T07_donem_net_kari_ceyrek',
             'T08_nakit_ve_nakit_benzerleri','T09_ticari_alacaklar','T10_stoklar',
             'T11_toplam_varliklar','T12_finansal_borclar','T13_toplam_yukumlulukler',
             'T14_toplam_ozkaynaklar','T15_isletme_nakit_akisi_ceyrek',
             'T16_yatirim_nakit_akisi_ceyrek','T17_finansman_nakit_akisi_ceyrek']
    lines=[
        '# Veri denetimi — 7 Kasım 2026', '',
        '**Sonuç: Veri hazırlama iyileştirildi; bütün değişkenler ve tarihsel sürümler tamamlanmış değil. Model eğitimine hazır onayı verilmedi.**', '',
        'İncelenen GitHub sürümü `91a7d0eba593dd90b2d37a4e73bdfbb4756b421c`. Kontrol sırasında bağlı depoda yalnız main vardı; ayrıca gönderilmiş düzeltme dalı görünmedi.', '',
        '## Üretilen veriler', '',
        f'- {result["companies"]} şirket × 44 çeyrek = {result["rows"]:,} satır. Kanonik CSV {result["columns"]} alan içerir; bunların hepsi model özelliği değildir.',
        f'- Ham tablolardaki {source_row_count:,} satır etiketleri ve özgün değerleriyle saklandı. Önceki iki CSV farklıydı; artık birebir aynı içerik üretilir.',
        f'- Resmi dış kaynaklarda 2010–2020 için {macro_count:,} sayısal kayıt var. Bu sayı 48 eski ÜFE vekil kaydını da içerir; bunlar Yİ-ÜFE yerine kullanılmaz. Tüm arşiv {macro_total:,} kayıttır; düzey ve yıllık değişim ayrı kayıtlar olabilir.',
        '- Beş resmi şirket PDF’siyle kaynak düzeltmesi; beş PDF üzerinde 55 aile–kaynak dipnot araması ve KAREL için 17 sayısal/türetilmiş pilot gözlem kaydedildi. Pilot bütün şirket/dönem evreni değildir.',
        '- Mevcut 1.320 KAP XLS yeniden ayrıştırıldı. Bütün 44 KAP arşivinin bu çalışmada yeniden indirildiği iddia edilmiyor; resmi makro kaynakları ve beş doğrulama PDF’si yeni indirildi.', '',
        '## Kaynakla doğrulanan düzeltmeler', '',
        '| Şirket/dönem | Yeni tutar / düzeltme |', '|---|---|',
        '| THYAO 2015 Q4 | Toplam varlık 47.638.000.000 TL; parasal tutarlarda milyon TL çarpanı |',
        '| THYAO 2016 Q1 | Toplam varlık 48.349.000.000 TL; parasal tutarlarda milyon TL çarpanı |',
        '| TOASO 2013 Q1 | Toplam varlık 6.266.179.000 TL; bin TL çarpanı |',
        '| TOASO 2014 Q3 | Toplam varlık 6.550.101.000 TL; bin TL çarpanı |',
        '| KAREL 2012 Q1 | İşletme 11.528.269; yatırım −4.778.913; finansman nakit akışı 8.800.694 TL |', '',
        'Kaynak URL’leri, PDF sayfaları, özgün XLS ve kanıt PDF özetleri `data/kap_refresh_manifest.json` içindedir. Kaynak değişirse düzeltme sessiz uygulanmaz. THYAO hisse başına kazancı parasal tablo çarpanıyla çarpılmadı.', '',
        'Gider işaretleri için özgün maliyet saklanır; RYSAS’ın pozitif bildirilmiş satış maliyeti eksi gider işaretine çevrilir. Ayrı hizmet geliri bulunan TUPRS dönemlerinde gelir bileşenleri ancak brüt kâr mutabakatıyla birleştirilir. Kaynak tutarı uydurulmaz.', '',
        '## Kalan kalite kayıtları', '',
        f'Genişletilmiş muhasebe kontrolleri {len(issues)} şirket-çeyrek kaydını inceleme için işaretledi. Bu kayıtlar `financial_quality_issues.csv` içindedir ve sıkı tarihsel girdiye alınmaz.',
        'GSDDE’de sıfır genel hasılat satırının altında denizcilik gelir/giderleri ve finans sektörü kalemleri birlikte raporlanıyor; kapsam eşlemesi tamamlanmadan genel şirket hasılatı diye doldurulmadı. ALCTL ve bazı TUPRS eski raporlarında brüt kâr ile çıkarılabilen gelir/maliyet eşitliği ayrıca inceleme gerektiriyor. Bu bayraklar otomatik olarak şirketin raporunun hatalı olduğunu kanıtlamaz.', '',
        '## Tarih ve sürüm güvenliği', '',
        '`period_first_published_at`, seçilen dosyanın `report_published_at` tarihi ve modelin `available_at` alanları ayrıdır. Bir dönemin ilk bildirim tarihi, daha sonra indirilen düzeltilmiş tutarın o gün bilindiğini kanıtlamaz.',
        'Kimliği bilinen KAP bildirim sürümleri kendi tarihlerine bağlanır. Yalnız üstbilgi tarihi olan eski arşivler ile bugün indirilen şirket PDF kopyaları sıkı tarihsel sürüm kanıtı sayılmaz. Bunların değerleri gözlem tablosunda korunur, geçmiş model girdisinde kullanılmaz.',
        'YTD farkı aynı yıl/konsolidasyon/para/fiyat temeliyle alınır; türetilmiş akış için iki raporun da zaman ve sürüm denetimi gerekir. Doğrudan raporlanan üç aylık değer ayrıca ayırt edilir.',
        'Güncel makro dosyaları tarihsel ilk sürüm değildir. Yayın/sürüm kanıtı bulunmadığı için bütün indirilen makro gözlemlerinde PIT uygunluğu kapalıdır. `snapshot_only_` alanları betimsel gözlem içindir; `model_features_point_in_time.csv` bunları girdi olarak içermez.', '',
        '## Kapsam ve açık işler', '',
        '51 ailenin tamamı `feature_coverage.csv` ve `VERI_KAPSAM_PLANI.md` içinde takip edilir. Kısmi eşleme, bütün ham bileşenlerin veya gecikmelerin tamamlandığı anlamına gelmez.',
        (f'- Kullanıcının onayıyla EVDS verileri PHP+cURL ile çekildi: 6 ailede {evds_numeric:,} sayısal kayıt. Dolar/avro döviz alış, TL ticari kredi faizi, TÜFE, Yİ-ÜFE ve takvim etkisinden arındırılmış sanayi üretimi ana CSV’ye eklendi. Aylık serilerde 2010–2020 için 132 ay tamam; faiz serisinde 574 haftanın 573’ü sayısal, eksik hafta sıfır yapılmadı. M08 için sektör serisi seçimi halen gerekiyor.' if evds_downloaded else '- EVDS seri eşlemesi hazır; anahtarlı veri çekimi tamamlanmadı. M08 sektör serisi seçimi gerekiyor.'),
        '- TCMB döviz alış kuru ile ECB referans kuru ayrı sütunlardır. M07 emtia adayları için şirket/sektör eşlemesi henüz yapılmadı. Yİ-ÜFE’nin eski web sayfasında boş olan ayları EVDS’deki doğrulanmış Yİ-ÜFE serisinden alınır; eski ÜFE sessizce ikame edilmez.',
        '- Faaliyet karması, sipariş yapısı, coğrafya, müşteri/tedarik ve net döviz pozisyonu bütün evrende tamamlanmış değil. KAREL pilotunda toplam döviz pozisyonu anlatısı ile tablosu ve ihracat tutarları arasında çelişkiler saklandı; oran üretip gizlenmedi.',
        '- Eksik değerler sıfır yapılmaz; toplam kâr/özkaynak ana ortaklık yerine kopyalanmaz; ağırlıklı ortalama pay adedi olmadan kesin EPS hesaplanmaz.', '',
        '## Hedeflerin sayısal kapsamı', '',
        'Aşağıdaki sayılar eksik olmayan gözlemleri sayar; kalite, sürüm veya eğitim uygunluğu onayı değildir.', '',
        '| Hedef alanı | Dolu | Eksik |', '|---|---:|---:|',
    ]
    lines += [f'| `{c}` | {int(snapshot[c].notna().sum())} | {int(snapshot[c].isna().sum())} |' for c in targets]
    lines += ['', '## Öğretim üyesinin önerdiği çalışma', '',
              '2019 DergiPark makalesi iflas sınıflandırması yapıyor. Ayrıntılı değerlendirme ve ek ham alan eşlemeleri `arastirma/2026-11-07-hoca-makalesi/MAKALE_DEGERLENDIRMESI.md` içindedir. Kaynak PDF korunmuştur. Makalenin skorları veya başarı yüzdeleri bu projede elde edilmiş sonuç diye kullanılmadı.', '',
              '## Doğrulama', '',
              f'Denetimin {len(checks)} yapısal/sayısal kontrolü: '+('geçti.' if result['structural_pass'] else 'başarısız kontroller var.'),
              'Test komutları `python -m pytest -q` ve `php tests/test_evds_php.php`. Mevcut oturumda 17 Python testi ve 37 bağımsız PHP kontrolü geçti. PHP çekiminde 1000 gözlem sınırı için yıllık parçalama, sınır haftası ayırma, eksik/sıfır ayrımı ve tam takvim ayıyla yıllık değişim kontrol edildi. Anahtar koda, CSV’ye veya kaynak kayıtlarına yazılmadı.',
              'Kontrollerin geçmesi model eğitimi onayı değildir. Henüz model eğitilmedi; tahmin başarısı ölçülmedi. Denetim sonucu `data/dataset_audit.json` içinde makine tarafından da okunabilir.', '']
    (ROOT/'docs/model_oncesi/VERI_DENETIMI_2026-11-07.md').write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result


if __name__=='__main__':
    if not audit()['structural_pass']:
        raise SystemExit(1)
