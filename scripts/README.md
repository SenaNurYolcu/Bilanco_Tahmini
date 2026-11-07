# Veri Çekme ve Veri Seti Oluşturma Betikleri (`scripts/`)

Bu klasör, `docs/model_oncesi/degiskenler.json` ve `docs/model_oncesi/DEGISKEN_LISTESI.md` belgelerinde tanımlanan veri sözleşmesine uygun olarak **2010–2020 (44 çeyrek)** dönemi için **6 farklı sektörden 5'er şirketin (toplam 30 BIST şirketi)** KAP finansal raporlarını, Türkiye makroekonomik göstergelerini ve küresel risk endekslerini çeken ve birleştiren Python betiklerini içerir.

## Betikler ve Görevleri

1. **[`fetch_external_macro_and_risk.py`](file:///c:/Users/ASUS/OneDrive/Desktop/repo/Bilanco_Tahmini/scripts/fetch_external_macro_and_risk.py)**
   - KAP finansal raporlarında yer almayan dışsal değişkenleri (`degiskenler.json` içerisinde belirtilen resmi kaynaklardan) indirir ve `data/external/` altına kaydeder:
     - **Küresel Risk (`R01`–`R04`)**: Caldara & Iacoviello Jeopolitik Risk Endeksi (`GPR`, `GPRT`, `GPRA` — `matteoiacoviello.com`), Küresel Ekonomik Politika Belirsizliği (`GEPU_ppp` — `policyuncertainty.com`) ve OFR Finansal Stres Endeksi (`OFR FSI` — `financialresearch.gov`).
     - **Türkiye Makroekonomik Göstergeleri (`M01`–`M06`)**: Günlük `USD/TRY` ve `EUR/TRY` kurları (`Yahoo Finance / TCMB`), Türkiye politika/bankalararası faiz oranı (`TCMB / OECD MEI`), `TÜFE` ve `Yİ-ÜFE` yıllık enflasyon oranları (`TCMB / TÜİK`) ve Takvim Etkisinden Arındırılmış Sanayi Üretim Endeksi yıllık değişimi (`TÜİK / OECD MEI`).

2. **[`fetch_kap_financials_2010_2020.py`](file:///c:/Users/ASUS/OneDrive/Desktop/repo/Bilanco_Tahmini/scripts/fetch_kap_financials_2010_2020.py)**
   - KAP'ın dönemlik toplu finansal tablo arşivlerinden (`/tr/api/financialTable/download/{year}/{period}`) 2010 Q1 – 2020 Q4 arasındaki 44 çeyreğin arşivlerini (`data/kap_zips/`) indirir.
   - Seçilen 6 sektördeki 30 şirketin `.xls` formatındaki finansal raporlarını `data/kap_raw_xls/` klasörüne çıkarır.
   - KAP bildirim sorgu API'si (`/tr/api/disclosure/members/byCriteria`) üzerinden yalnızca **Finansal Rapor (`FR`)** bildirimlerini sorgulayarak her şirket-çeyrek raporunun ilk kamuya açıklanma zaman damgasını (`first_published_at`) ve bildirim numarasını (`disclosure_index`) `data/kap_fr_catalog_2010_2020.json` dosyasına kaydeder.

3. **[`parse_and_build_dataset.py`](file:///c:/Users/ASUS/OneDrive/Desktop/repo/Bilanco_Tahmini/scripts/parse_and_build_dataset.py)**
   - `data/kap_raw_xls/` altındaki hem **2010–2015 BIFF8 Excel (`.xls`)** hem de **2016–2020 HTML tabanlı (`.xls`)** KAP finansal tablolarını ayrıştırır.
   - Raporlama birimi (`TL`, `1.000 TL`, `Bin TL`) farklılıklarını normalize ederek tüm parasal tutarları tam **TL (`TRY`)** cinsine dönüştürür.
   - Gelir Tablosu ve Nakit Akış Tablosu kalemleri için hem kümülatif (`_ytd`) hem de tek çeyreklik (`_ceyrek`) akış değerlerini üretir.
   - 17 çekirdek finansal kalemi (`T01`–`T17`), P0 finansal oran ve büyüme serilerini (`F01`–`F14`), Türkiye makro serilerini (`M01`–`M06`), küresel risk serilerini (`R01`–`R04`) ve rejim etkileşim terimlerini (`X02`, `X03`) bilançonun dönem sonu tarihi (`period_end_date = t0`) itibarıyla ileriye bakma hatası (*look-ahead bias*) olmadan birleştirir.
   - Nihai veri setini [`bist_bilanco_tahmini_2010_2020.csv`](file:///c:/Users/ASUS/OneDrive/Desktop/repo/Bilanco_Tahmini/bist_bilanco_tahmini_2010_2020.csv) ve [`data/bist_bilanco_tahmini_2010_2020.csv`](file:///c:/Users/ASUS/OneDrive/Desktop/repo/Bilanco_Tahmini/data/bist_bilanco_tahmini_2010_2020.csv) olarak kaydeder.

## Çalıştırma Sırası

```bash
python scripts/fetch_external_macro_and_risk.py
python scripts/fetch_kap_financials_2010_2020.py
python scripts/parse_and_build_dataset.py
```
