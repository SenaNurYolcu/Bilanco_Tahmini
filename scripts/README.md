# Veri toplama, yeniden üretim ve denetim

Kapsam: 30 finans dışı BIST şirketi, 2010–2020, 44 çeyrek. Yetkili değişken sözlüğü `docs/model_oncesi/degiskenler.json`; 51 aile 51 hazır sütun demek değildir. Bu sürüm bir veri hazırlama çıktısıdır; model eğitmez.

## Kurulum ve çalıştırma

```bash
python -m pip install -r requirements-data.txt
python scripts/fetch_kap_financials_2010_2020.py
python scripts/refresh_kap_sources.py
php scripts/fetch_evds_data.php --prompt-key
python scripts/fetch_external_macro_and_risk.py --refresh
python scripts/fetch_company_profile_pilot.py
python scripts/rebuild_dataset.py
python scripts/audit_dataset.py
python -m pytest -q
php tests/test_evds_php.php
```

KAP arşiv indiricisi mevcut ham dosyaları korur. `--start-year`, `--end-year`, `--quarters` ve `--refresh-catalog` seçeneklerini `--help` ile inceleyin. Mevcut 1.320 KAP dosyası silinmeden yeniden ayrıştırıldı; bütün 44 arşiv bu incelemede sıfırdan indirilmedi. Beş birim/tutar sorunu için şirketlerin resmi PDF'leri ayrıca indirildi ve doğrulandı. Makro kaynakları yeniden indirildi.

Dış veri için `--offline`, önbellekteki kaynaklardan aynı gözlem tablosunu üretir. EVDS çekimi kullanıcının isteğiyle **PHP+cURL** ile uygulanmıştır; `php scripts/fetch_evds_data.php --prompt-key` anahtarı Terminal'de gizli olarak belleğe alır ve sadece TCMB'nin resmi HTTPS adresine `key` başlığında gönderir. Anahtar dosyaya, komut satırına, CSV'ye veya kaynak manifestine yazılmaz. PHP 8+ ve cURL eklentisi gerekir; ayrı PHP sunucusu başlatılmaz.

`config/evds_series.json` altı resmi seri tanımını içerir. 2010–2020 USD/EUR döviz alış, ticari kredi faizi, TÜFE, Yİ-ÜFE ve takvim etkisinden arındırılmış sanayi üretimi çekilir. Aylık endeksler 2009'dan alınarak yıllık değişim tam 12 ay eşleştirmesiyle hesaplanır. EVDS'nin 1000 kayıt sınırı için yıllık sorgular kullanılır; haftalık isteğin ekleyebildiği önceki cuma ham yanıtta korunur ve ait olduğu takvim yılına ayrılır. Yeni çağrılarda yalnız kaynak özeti doğrulanan önbellek yeniden kullanılabilir; alınma zamanı korunur.

PHP çıktısı `data/external/rebuilt/evds/` altındadır. Ortak dış veri birleştiricisi bu CSV'yi okuyup mevcut makro havuzuna ekler; EVDS veri çekimini Python'a çevirmez. Eski EVDS2 adresleri kullanılmaz. Seri/yıl doluluğu `series_year_coverage.csv` içindedir. Orijinal açıklama sürümleri doğrulanmadığı için bu değerler tarihsel modele otomatik açılmaz. M08 sektör göstergeleri için seri seçimi halen gerekir.

## Hangi CSV kullanılmalı?

| Dosya | İçerik |
|---|---|
| `data/bist_bilanco_tahmini_2010_2020.csv` | Kanonik finansal gözlem tablosu; kaynak, birim, kalite ve sürüm bilgileri. `snapshot_only_` makrolar güncel tarihsel kopyadır, model girdisi değildir. |
| Kökteki aynı adlı CSV | Uyum kopyası; kanonik dosyayla aynı baytlar. İki dosya ayrı elle düzenlenmemeli. |
| `data/financial_source_rows.csv` | Kaynak dosyalardan mevcut tüm etiket/satırlar; bozuk özgün değerler de korunur. Semantik olarak hepsi bağımsız özellik değildir. |
| `data/model_features_point_in_time.csv` | Hedef dönemi bitiminde kullanılabilen q−1/q−4 referansları. Eksik veya doğrulanmamış sürümler geçmiş girdiye alınmaz. |
| `data/model_labels.csv` | Hedef tutarlar ayrı dosyada; dönem, kalite ve tarihsel uygunluk alanlarıyla. Eğitime otomatik onay değildir. |
| `data/financial_quality_issues.csv` | Muhasebe eşitliği, ölçek ve brüt kâr kontrolünde inceleme gerektiren kayıtlar. |
| `data/feature_coverage.csv` | 51 ailenin eşleme ve eksik durumu; makro kaynak gözlemi ile şirket-çeyrek kapsamı ayrı sayılır. |
| `data/external/rebuilt/macro_observations.csv` | Resmi makro/risk/emtia gözlemleri; birim, kaynak, alınma zamanı ve sürüm. |
| `data/company_profile_pilot.csv` | Beş kaynak PDF üzerinden sınırlı dipnot pilotu. Bütün şirket/tarih evreni değildir. Çelişen ölçüler işaretlidir. |
| `data/company_profile_pilot_search.csv` | C02–C10 ve F19–F20 için kaynak/sayfa araması ve eksik nedenleri. |

## Temel kurallar

- Eksik değer sıfır değildir. Kısa/uzun bileşen toplamı bir bileşen bilinmiyorsa tamamlanmış sayılmaz.
- Toplam konsolide kâr/özkaynak, ana ortaklık kârı/özkaynağı yerine kopyalanmaz.
- Nakit akışı toplamı bölümün son sayısal satırından tahmin edilmez.
- Ağırlıklı ortalama pay adedi bilinmiyorsa sermayeye bölerek kesin EPS üretilmez.
- Birim düzeltmeleri kaynak PDF ve özgün XLS özetine bağlıdır; kaynak değişirse eski düzeltme reddedilir.
- Gider işareti ve ayrıca raporlanan hizmet geliri korunur. Ayrı hizmet gelirini ekleme ancak kaynak satırı ve brüt kâr mutabakatı birlikte doğruladığında yapılır; özgün satış/maliyetler ayrıca saklanır.
- YTD farkı aynı mali yıl, para birimi, konsolidasyon ve fiyat temeli gerektirir. Doğrudan üç aylık değer varsa önceliklidir. Tarihsel girdide farkın önceki raporu da zaman/sürüm denetimini geçmelidir.
- `report_published_at` seçilen sürümün tarihi, `period_first_published_at` dönem için katalogdaki ilk bildirim tarihidir. İkinci tarih, düzeltilmiş tutarın o gün bilindiğini kanıtlamaz.
- `disclosure_id_linked` kimliği belli bildirim sürümünü tarihine bağlar; 2010–2016 başındaki yalnız üstbilgi tarihli arşivler ve bugün indirilen şirket PDF'leri aynı kanıt düzeyinde değildir. Bu kaynaklar sıkı tarihsel girdilerden dışlanır.
- Makrolarda orijinal yayın zamanı/sürümü kanıtlanmadığı için geçmişe sabit gecikme uydurulmaz. ECB referans kuru TCMB kuru, bankalararası faiz ticari kredi faizi, eski ÜFE Yİ-ÜFE değildir.
- `paper2019_` alanları öğretim üyesinin önerdiği makaleden esinlenen ham adaylardır; otomatik seçilmiş model girdileri değildir.

Tüm açık işler ve sonuçlar `docs/model_oncesi/VERI_DENETIMI_2026-11-07.md`, ayrıntılı aile planı `VERI_KAPSAM_PLANI.md` içinde tutulur. JSON değişken kaydının `verified` veya `tested` durumları bu denetimle topluca yükseltilmedi.

`data/financial_source_rows.csv` ve `data/external/rebuilt/macro_observations.csv` büyük türetilmiş ara dosyalardır; GitHub sürümünde saklanmaz. Kaynaklar depoda korunur; `python scripts/fetch_external_macro_and_risk.py --offline` ve `python scripts/rebuild_dataset.py` ile yeniden üretilir. Gerçek anahtar yerel `.env` içindedir; depodaki `.env.example` sadece boş şablondur.
