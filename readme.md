# Bilanço Tahmini

BIST şirketlerinin sıradaki açıklanacak finansal raporlarındaki ana kalemleri makine öğrenmesiyle tahmin etmeyi amaçlayan araştırma projesi.

Hedef; gelir tablosu, bilanço ve nakit akışındaki kalemleri aralarındaki muhasebe ilişkilerini gözeterek birlikte tahmin etmek. EPS (hisse başına kâr), bu sonuçlardan hesaplanabilecek göstergelerden biri.

**Mevcut durum:** Kaynak araştırması ve yöntem karşılaştırması tamamlandı. Bu depoda henüz eğitilmiş bir tahmin modeli veya çalışan tahmin uygulaması bulunmuyor.

## Tahmin kapsamı

İlk sürüm için planlanan ana çıktılar:

| Finansal tablo | Hedef kalemler |
|---|---|
| Gelir tablosu | Ciro, brüt kâr, faaliyet kârı, FAVÖK, ana ortaklık net kârı |
| Bilanço | Nakit, ticari alacaklar, stoklar, duran varlıklar, kısa ve uzun vadeli finansal borçlar, ticari borçlar, özkaynak |
| Nakit akış tablosu | İşletme faaliyetlerinden nakit akışı, yatırım harcamaları, nakitteki net değişim |

Bazı temel kalemler modelle tahmin edilecek; brüt kâr, marjlar ve EPS gibi türetilmiş sonuçlar uygun hesaplarla üretilecek. Bilanço eşitliği ve tablolar arası bağlantılar ayrıca kontrol edilecek. Banka ve sigorta şirketleri için ayrı kalemler ve modeller gerekecek.

## Araştırma ve belgeler

6 Kasım 2026 tarihli araştırmada 16 GitHub projesi değerlendirildi. Önemli kaynakların sürümleri, bağlantıları ve inceleme sınırları belgelendi.

| Belge | İçerik |
|---|---|
| [Güncellenebilir kendi değişken listemiz](docs/tasarim/DEGISKEN_LISTESI.md) | Seçilen risk endeksleri, aday girdiler, şirket profilleri, olay etkileşimleri ve deney durumları |
| [Araştırma ve proje karşılaştırması](docs/arastirma/2026-11-06-bilanco-tahmini/ARASTIRMA.md) | İlk üç proje, güçlü yönleri ve sınırlamaları |
| [Projelerin değişken sözlüğü](docs/arastirma/2026-11-06-bilanco-tahmini/PROJELERIN_DEGISKENLERI.md) | Kullanılan ve aday değişkenler, açıklamaları ve kaynak kodları |
| [Değişken sözlüğünün HTML sürümü](docs/arastirma/2026-11-06-bilanco-tahmini/PROJELERIN_DEGISKENLERI.html) | Tarayıcıda okunabilecek dışa aktarım |
| [Algoritmalar ve çalışma mekanikleri](docs/arastirma/2026-11-06-bilanco-tahmini/ALGORITMALAR_VE_CALISMA_MEKANIKLERI.md) | Eğitim, tahmin, model birleştirme ve muhasebe mekanizmaları |
| [Makale incelemeleri](docs/arastirma/2026-11-06-bilanco-tahmini/MAKALELER.md) | Değişken seçiminin akademik dayanakları |
| [Kaynak manifestosu](docs/arastirma/2026-11-06-bilanco-tahmini/kaynak-manifestosu.json) | Sürüm, indirme durumu ve SHA-256 kayıtları |

Ayrıntılı ekler: [Forma'nın 78 kalemi](docs/arastirma/2026-11-06-bilanco-tahmini/EK_FORMA_78.md), [DeepEarnings'in 236 aday alanı](docs/arastirma/2026-11-06-bilanco-tahmini/EK_DEEPEARNINGS.md), [EPSBench'in 149 şemasındaki 1.652 ara hedef](docs/arastirma/2026-11-06-bilanco-tahmini/EK_EPSBENCH_SURUCULERI.md).

## İncelenen başlıca yaklaşımlar

- **Forma:** Finansal kalemleri ve gelecek dönemleri birlikte işleyen özel Transformer.
- **Quarterly EPS Forecast Study:** Gecikmeli finansal özelliklerle OLS ve gradient boosting.
- **EPS Forecasting:** Klasik ML, zaman serisi ağları ve Chronos-2 karşılaştırmaları; veri zamanı kontrolleri ve model birleştirme.
- **Zincirlenmiş LightGBM:** Önce tahmin edilen kalemleri sonraki kalemlerin modellerinde kullanma.

Kaynak projelerde bildirilen başarılar bu depoda yeniden üretilmedi. BIST verisi üzerindeki yöntem seçimi, ortak veri ve test dönemlerinde yapılacak karşılaştırmayla belirlenecek.

## Geliştirme planı

1. Şirket, mali dönem, açıklanma zamanı, birim ve raporlama kapsamını içeren veri yapısını kurmak.
2. Çeyreklik ve kümülatif tutarları ayırmak; karşılaştırılabilir para birimi ve enflasyon düzeltme bazını korumak.
3. Basit sezonluk tahminleri ve standart ML modellerini referans olarak eğitmek.
4. Bağımsız, zincirlenmiş ve ortak çoklu çıktı tahminlerini karşılaştırmak.
5. Muhasebe tutarlılığını, kalem bazında hatayı ve tahmin aralıklarının gerçekleşenleri kapsama oranını ölçmek.

Testlerde yalnızca tahmin tarihinde açıklanmış bilgiler kullanılacak; sonraki dönemler üzerinde ilerleyen zaman pencereleriyle değerlendirme yapılacak.

## Dizin yapısı

```text
docs/
├── README.md
└── arastirma/2026-11-06-bilanco-tahmini/
    ├── ARASTIRMA.md
    ├── PROJELERIN_DEGISKENLERI.md
    ├── ALGORITMALAR_VE_CALISMA_MEKANIKLERI.md
    ├── MAKALELER.md
    ├── EK_*.md
    ├── makaleler/    # 6 makale PDF'si
    ├── projeler/     # 7 kaynak kod arşivi
    └── *.json       # Kaynak ve değişken kayıtları
```

Arşivlenen projelerin lisansları kendi dosyalarında korunmuştur. Kaynak kodu, model ağırlıkları ve finansal veri için kullanım koşulları ayrı olabilir.
