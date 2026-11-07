# Veri denetimi — 7 Kasım 2026

**Sonuç: Veri hazırlama iyileştirildi; bütün değişkenler ve tarihsel sürümler tamamlanmış değil. Model eğitimine hazır onayı verilmedi.**

İncelenen GitHub sürümü `91a7d0eba593dd90b2d37a4e73bdfbb4756b421c`. Kontrol sırasında bağlı depoda yalnız main vardı; ayrıca gönderilmiş düzeltme dalı görünmedi.

## Üretilen veriler

- 30 şirket × 44 çeyrek = 1,320 satır. Kanonik CSV 205 alan içerir; bunların hepsi model özelliği değildir.
- Ham tablolardaki 308,072 satır etiketleri ve özgün değerleriyle saklandı. Önceki iki CSV farklıydı; artık birebir aynı içerik üretilir.
- Resmi dış kaynaklarda 2010–2020 için 17,026 sayısal kayıt var. Bu sayı 48 eski ÜFE vekil kaydını da içerir; bunlar Yİ-ÜFE yerine kullanılmaz. Tüm arşiv 32,783 kayıttır; düzey ve yıllık değişim ayrı kayıtlar olabilir.
- Beş resmi şirket PDF’siyle kaynak düzeltmesi; beş PDF üzerinde 55 aile–kaynak dipnot araması ve KAREL için 17 sayısal/türetilmiş pilot gözlem kaydedildi. Pilot bütün şirket/dönem evreni değildir.
- Mevcut 1.320 KAP XLS yeniden ayrıştırıldı. Bütün 44 KAP arşivinin bu çalışmada yeniden indirildiği iddia edilmiyor; resmi makro kaynakları ve beş doğrulama PDF’si yeni indirildi.

## Kaynakla doğrulanan düzeltmeler

| Şirket/dönem | Yeni tutar / düzeltme |
|---|---|
| THYAO 2015 Q4 | Toplam varlık 47.638.000.000 TL; parasal tutarlarda milyon TL çarpanı |
| THYAO 2016 Q1 | Toplam varlık 48.349.000.000 TL; parasal tutarlarda milyon TL çarpanı |
| TOASO 2013 Q1 | Toplam varlık 6.266.179.000 TL; bin TL çarpanı |
| TOASO 2014 Q3 | Toplam varlık 6.550.101.000 TL; bin TL çarpanı |
| KAREL 2012 Q1 | İşletme 11.528.269; yatırım −4.778.913; finansman nakit akışı 8.800.694 TL |

Kaynak URL’leri, PDF sayfaları, özgün XLS ve kanıt PDF özetleri `data/kap_refresh_manifest.json` içindedir. Kaynak değişirse düzeltme sessiz uygulanmaz. THYAO hisse başına kazancı parasal tablo çarpanıyla çarpılmadı.

Gider işaretleri için özgün maliyet saklanır; RYSAS’ın pozitif bildirilmiş satış maliyeti eksi gider işaretine çevrilir. Ayrı hizmet geliri bulunan TUPRS dönemlerinde gelir bileşenleri ancak brüt kâr mutabakatıyla birleştirilir. Kaynak tutarı uydurulmaz.

## Kalan kalite kayıtları

Genişletilmiş muhasebe kontrolleri 15 şirket-çeyrek kaydını inceleme için işaretledi. Bu kayıtlar `financial_quality_issues.csv` içindedir ve sıkı tarihsel girdiye alınmaz.
GSDDE’de sıfır genel hasılat satırının altında denizcilik gelir/giderleri ve finans sektörü kalemleri birlikte raporlanıyor; kapsam eşlemesi tamamlanmadan genel şirket hasılatı diye doldurulmadı. ALCTL ve bazı TUPRS eski raporlarında brüt kâr ile çıkarılabilen gelir/maliyet eşitliği ayrıca inceleme gerektiriyor. Bu bayraklar otomatik olarak şirketin raporunun hatalı olduğunu kanıtlamaz.

## Tarih ve sürüm güvenliği

`period_first_published_at`, seçilen dosyanın `report_published_at` tarihi ve modelin `available_at` alanları ayrıdır. Bir dönemin ilk bildirim tarihi, daha sonra indirilen düzeltilmiş tutarın o gün bilindiğini kanıtlamaz.
Kimliği bilinen KAP bildirim sürümleri kendi tarihlerine bağlanır. Yalnız üstbilgi tarihi olan eski arşivler ile bugün indirilen şirket PDF kopyaları sıkı tarihsel sürüm kanıtı sayılmaz. Bunların değerleri gözlem tablosunda korunur, geçmiş model girdisinde kullanılmaz.
YTD farkı aynı yıl/konsolidasyon/para/fiyat temeliyle alınır; türetilmiş akış için iki raporun da zaman ve sürüm denetimi gerekir. Doğrudan raporlanan üç aylık değer ayrıca ayırt edilir.
Güncel makro dosyaları tarihsel ilk sürüm değildir. Yayın/sürüm kanıtı bulunmadığı için bütün indirilen makro gözlemlerinde PIT uygunluğu kapalıdır. `snapshot_only_` alanları betimsel gözlem içindir; `model_features_point_in_time.csv` bunları girdi olarak içermez.

## Kapsam ve açık işler

51 ailenin tamamı `feature_coverage.csv` ve `VERI_KAPSAM_PLANI.md` içinde takip edilir. Kısmi eşleme, bütün ham bileşenlerin veya gecikmelerin tamamlandığı anlamına gelmez.
- Kullanıcının onayıyla EVDS verileri PHP+cURL ile çekildi: 6 ailede 6,909 sayısal kayıt. Dolar/avro döviz alış, TL ticari kredi faizi, TÜFE, Yİ-ÜFE ve takvim etkisinden arındırılmış sanayi üretimi ana CSV’ye eklendi. Aylık serilerde 2010–2020 için 132 ay tamam; faiz serisinde 574 haftanın 573’ü sayısal, eksik hafta sıfır yapılmadı. M08 için sektör serisi seçimi halen gerekiyor.
- TCMB döviz alış kuru ile ECB referans kuru ayrı sütunlardır. M07 emtia adayları için şirket/sektör eşlemesi henüz yapılmadı. Yİ-ÜFE’nin eski web sayfasında boş olan ayları EVDS’deki doğrulanmış Yİ-ÜFE serisinden alınır; eski ÜFE sessizce ikame edilmez.
- Faaliyet karması, sipariş yapısı, coğrafya, müşteri/tedarik ve net döviz pozisyonu bütün evrende tamamlanmış değil. KAREL pilotunda toplam döviz pozisyonu anlatısı ile tablosu ve ihracat tutarları arasında çelişkiler saklandı; oran üretip gizlenmedi.
- Eksik değerler sıfır yapılmaz; toplam kâr/özkaynak ana ortaklık yerine kopyalanmaz; ağırlıklı ortalama pay adedi olmadan kesin EPS hesaplanmaz.

## Hedeflerin sayısal kapsamı

Aşağıdaki sayılar eksik olmayan gözlemleri sayar; kalite, sürüm veya eğitim uygunluğu onayı değildir.

| Hedef alanı | Dolu | Eksik |
|---|---:|---:|
| `T01_hasilat_ceyrek` | 1318 | 2 |
| `T02_satislarin_maliyeti_ceyrek` | 1317 | 3 |
| `T03_brut_kar_ceyrek` | 1318 | 2 |
| `T04_esas_faaliyet_kari_ceyrek` | 1317 | 3 |
| `T05_finansman_gideri_ceyrek` | 1302 | 18 |
| `T06_vergi_gideri_geliri_ceyrek` | 1296 | 24 |
| `T07_donem_net_kari_ceyrek` | 1318 | 2 |
| `T08_nakit_ve_nakit_benzerleri` | 1320 | 0 |
| `T09_ticari_alacaklar` | 570 | 750 |
| `T10_stoklar` | 1293 | 27 |
| `T11_toplam_varliklar` | 1320 | 0 |
| `T12_finansal_borclar` | 1181 | 139 |
| `T13_toplam_yukumlulukler` | 1320 | 0 |
| `T14_toplam_ozkaynaklar` | 1320 | 0 |
| `T15_isletme_nakit_akisi_ceyrek` | 1264 | 56 |
| `T16_yatirim_nakit_akisi_ceyrek` | 1286 | 34 |
| `T17_finansman_nakit_akisi_ceyrek` | 1251 | 69 |

## Öğretim üyesinin önerdiği çalışma

2019 DergiPark makalesi iflas sınıflandırması yapıyor. Ayrıntılı değerlendirme ve ek ham alan eşlemeleri `arastirma/2026-11-07-hoca-makalesi/MAKALE_DEGERLENDIRMESI.md` içindedir. Kaynak PDF korunmuştur. Makalenin skorları veya başarı yüzdeleri bu projede elde edilmiş sonuç diye kullanılmadı.

## Doğrulama

Denetimin 22 yapısal/sayısal kontrolü: geçti.
Test komutları `python -m pytest -q` ve `php tests/test_evds_php.php`. Mevcut oturumda 17 Python testi ve 37 bağımsız PHP kontrolü geçti. PHP çekiminde 1000 gözlem sınırı için yıllık parçalama, sınır haftası ayırma, eksik/sıfır ayrımı ve tam takvim ayıyla yıllık değişim kontrol edildi. Anahtar koda, CSV’ye veya kaynak kayıtlarına yazılmadı.
Kontrollerin geçmesi model eğitimi onayı değildir. Henüz model eğitilmedi; tahmin başarısı ölçülmedi. Denetim sonucu `data/dataset_audit.json` içinde makine tarafından da okunabilir.
