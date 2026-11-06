# Makaleler: hangi değişkenler neden kullanılmalı?

Araştırma tarihi: **2026-11-06**. “Makalede kullanılmış”, “katkısı deneyle ölçülmüş” ve “BIST için öneriliyor” aynı iddia değildir. Aşağıda bunlar ayrılmıştır. Tam bibliyografik bağlantılar ve indirilen sürümler kaynak manifestosunda yer alır.

## 1. Scherrmann ve Elsas — Earnings Prediction Using Recurrent Neural Networks (2023)

[Makale](https://arxiv.org/abs/2311.10756) · [Yerel PDF](makaleler/scherrmann-elsas-2023.pdf). Özellikle §4.1 ve model yapısı.

**Hedef:** çeyreklik ve mali yıl sonu kâr/EPS. **Muhasebe girdileri:** geçmiş kâr/EPS, toplam aktifler, özkaynak/aktif oranı, hisse başına nakit temettü ve hisse başına tahakkuklar. En fazla 20 çeyrek kullanılıyor. Aradaki dönem boşlukları için zaman bilgisi ekleniyor.

**Piyasa girdileri:** şirket getirisi, hisse başına hacim, Tobin Q değişimi, S&P 500 getirisi, VIX değişimi. Açıklama öncesi en fazla 63 günlük pencere özetleniyor; pencere uzunluğu ve çeyrek göstergeleri de modele giriyor.

**Çıkarım:** EPS geçmişi, kârın nakit/tahakkuk bileşimi ve mevsimsellik güçlü bir başlangıç tasarımıdır. Çalışma bütün girdilerin tek tek zorunlu olduğunu kanıtlamaz. Piyasa verisi, tahmin gününe kadar kesilmeli. Açık ve kullanılabilir bir resmi GitHub uygulaması bu taramada doğrulanamadığından proje ilk üçüne konulmadı.

## 2. Cao ve You — Fundamental Analysis via Machine Learning (2024; incelenen açık taslak 2021)

[Yayımlanan makale](https://doi.org/10.1080/0015198X.2024.2313692) · [İncelenen açık taslak](https://business.columbia.edu/sites/default/files-efs/imce-uploads/CEASA/Cao%20and%20You%2020210120.pdf) · [Yerel PDF](makaleler/cao-you-2021-draft.pdf).

**Sürüm ayrımı:** Aşağıdaki sayılar ve yöntem ayrıntıları 20 Ocak 2021 taslağına aittir; 2024 yayınındaki bütün tablolarla aynı oldukları varsayılmadı.

**Hedef:** bir yıl sonraki kâr. Taslakta 28 finansal tablo kalemi ile bunların birinci farkları olmak üzere 56 girdi kullanılıyor. Kâr bileşenleri, varlık/yükümlülükler ve nakit akışı birlikte işleniyor. Doğrusal modeller ile RF, gradient boosting ve sinir ağı karşılaştırılıyor.

**Değişken katkısı bulgusu:** mevcut kâr, faaliyet nakit akışı ve vergi giderinin seviye/değişimleri öne çıkıyor. Özkaynak, aktif ve alacak değişimleri de önem taşıyor. Satış–satış maliyeti ve stok–satış maliyeti gibi ekonomik ilişkili kalemlerin etkileşimleri ayrıca bilgi sağlıyor.

**Çıkarım:** sadece EPS ve birkaç oranla sınırlı kalmadan, vergi ve nakit akışı gibi ayrıntılı kalemleri ve değişimlerini aday olarak denemek gerekçeli. Yıllık sonuçları doğrudan “gelecek çeyrekte aynı kazanç” diye yorumlamak doğru olmaz.

## 3. Koval, Andrews ve Yan — Financial Forecasting from Textual and Tabular Time Series (EMNLP 2024)

[Yayın sayfası](https://aclanthology.org/2024.findings-emnlp.486/) · [Yerel PDF](makaleler/koval-2024.pdf). Değişkenler: §3 ve Ek A.5.

**Hedef:** sonraki çeyreğin standardize kâr sürprizi; doğrudan kâr tutarı değil. Geçmiş 8 çeyrek kullanılıyor.

**Girdi blokları:** geçmiş sürprizler; 15 finansal/piyasa özelliği; geçmiş sonuç toplantıları; faaliyet raporlarının yönetim değerlendirmesi; makro veriler.

15 özellik: temettü verimi, kâr/fiyat, satış/fiyat, defter değeri/fiyat, satış büyümesi, kâr büyümesi, brüt kâr/aktif, net kâr/özkaynak, net kâr/aktif, orta vadeli momentum, kısa vadeli tersine dönüş, fiyat oynaklığı, piyasa kaldıracı, hisse devir hızı, piyasa değeri.

Makro listesi: sanayi üretimi, enflasyon, tüketici güveni, 3 aylık ve 10 yıllık tahvil getirileri, vade farkı, kredi risk farkı, petrol fiyatı. Metin 8 kanal sayıyor; aynı bölümdeki boyut denkleminde 6 yazıyor. Bu tutarsızlık not edildi.

**Katkı:** metin bloklarının eklenmesi deneylerde yararlı; özellikle rejim değişimlerinde yönetimin ileriye dönük açıklamaları değer taşıyor. Makaledeki GitHub adresi araştırma tarihinde 404 döndüğü için erişilebilir kodlu ilk üç arasına alınmadı.

## 4. Elend, Tideman, Lopatta ve Kramer — Earnings Prediction with Deep Learning (2020)

[Makale](https://arxiv.org/abs/2006.03132) · [Yerel PDF](makaleler/elend-2020.pdf). Değişkenler §4, pencere §6.

**Hedef:** gelecek EPS. LSTM ve TCN, 20 çeyrek muhasebe geçmişi ve 20 günlük piyasa girdileriyle karşılaştırılıyor.

Muhasebe girdileri arasında EPS, aktif, ciro, faaliyet dışı gelir, faaliyet gideri, ticari borç, şerefiye, alacak, Ar-Ge, satış maliyeti, özkaynak, net kâr, amortisman öncesi/sonrası faaliyet kârı, amortisman, maddi duran varlık, vergi öncesi kâr ve vergi gideri var. Piyasa girdileri getiri, fiyat, hacim, dolaşımdaki hisse sayısı ve piyasa getirisi.

**Çıkarım:** kârla ekonomik ilişkisi olan gider ve işletme sermayesi kalemlerini geçmiş seri halinde kullanmak için doğrudan bir örnek. Kaynak metindeki bütün sütunlar model girdisi değil; kimlik ve analist alanlarının bir kısmı eşleştirme/karşılaştırma için. Finansal şirketlerin ayrı incelenmesi de önemli. Çalışma, her girdinin marjinal katkısını sıralayan bir değişken seçme kılavuzu olarak okunmamalı.

## 5. Johnson ve diğerleri — Long-Horizon Forecasting of Complete Financial Statements with Forma (2026)

[Makale](https://arxiv.org/abs/2608.11327) · [Yerel PDF](makaleler/forma-2026.pdf) · [Kod](https://github.com/forma-lab-mccombs/forma-release).

**Hedef:** 1–20 çeyrek sonra 78 kalemi birlikte tahmin etmek. 12 çeyrek geçmiş ve sektör kodu kullanılıyor. Kalem evreni 34 finansal durum tablosu, 18 gelir tablosu, 20 nakit akışı ve 6 türetilmiş kalemden oluşuyor.

**Çıkarım:** ciro/net kârın yanında borç, işletme sermayesi ve nakit akışını birlikte tahmin etmek, sonuçların muhasebe ilişkileriyle tutarlılığını değerlendirmeyi mümkün kılıyor. Bu bir “en iyi 78 bağımsız değişken” listesi değil; aynı kalemler geçmişte girdi, gelecekte hedef görevi görüyor. Seviye ve değişim ölçülerinin ayrılması, eksik raporlanan kalemleri zorla sıfırlamamak ve finansal şirketleri ayrı ele almak tasarım açısından yararlı.

## 6. Yin ve diğerleri — EPSBench: Benchmarking LLM Agents for Earnings Forecasting (2026)

[Makale](https://arxiv.org/abs/2610.38293) · [Yerel PDF](makaleler/epsbench-2026.pdf) · [Kod](https://github.com/chuyuxu/EPSBench).

**Hedef:** açıklama öncesinde GAAP seyreltilmiş EPS; 86 şirketten 149 şirket-çeyrek. Finansal rapor, önceki sonuç toplantısı ve haberlerden şirkete özgü muhasebe sürücüleri tahmin ediliyor; ortak hesaplayıcı bunları EPS'ye dönüştürüyor.

**Çıkarım:** gelir büyümesi, maliyet marjı, faaliyet gideri, faiz, vergi ve seyreltilmiş hisse sayısını ayrı tahmin etmek, hatanın kaynağını izlemeyi kolaylaştırıyor. Bu sürücüler sabit bir tabular ML girdi vektörü değil; LLM'nin tahmin ettiği ara hedefler. Makalede 80% nominal aralıkların kapsaması modeller arasında yaklaşık %37–70; bir modelin aralık vermesi aralığın güvenilir olduğu anlamına gelmiyor. Toplam EPS hatası kadar faaliyet kârı ve vergi köprüsünü de incelemek yararlı.

## Ek referanslar ve inceleme düzeyi

| Kaynak | Bu araştırmadaki kullanım | Sınır |
|---|---|---|
| [Hou, van Dijk ve Zhang — The Implied Cost of Capital: A New Approach, 2012](https://www.sciencedirect.com/science/article/pii/S0165410111000966) | Küçük muhasebe değişkenli yıllık kâr tahmininin temel kıyası. Kâr, aktif, temettü, zarar/temettü göstergeleri ve tahakkuklar için arka plan. | Burada bir çeyrek ML başarısı olarak sunulmadı. Model tanımı ayrıca Scherrmann–Elsas ve Cao–You'da kontrol edildi. |
| [Geertsema, Lu ve Ma — Projecting Financial Statements with Chained Machine Learning](https://papers.ssrn.com/sol3/Delivery.cfm/5039433.pdf?abstractid=5039433&mirid=1) | Kalemleri sırayla, önceki tahminlere koşullu üretme fikri. Forma deposunda chained GBM rakip uygulaması da var. | SSRN yazar özeti incelendi; bu makalenin tam PDF'si arşivlenmedi ve değişken listesi yeniden kurulmadı. |
| [Financial Statement Analysis with Large Language Models](https://arxiv.org/abs/2407.17866) | Gelecek kâr yönünü sınıflandırma ile sayısal kâr tahmininin ayrımı. | Özet düzeyinde kontrol; PDF indirme başarısızlığı manifestoda kayıtlı. Sayısal ML ilk üç sıralamasına temel yapılmadı. |
| [Abarbanell ve Bushee — Fundamental Analysis, Future Earnings, and Stock Prices, 1997](https://doi.org/10.2307/2491464) | Tarihsel temel analiz sinyalleri için bibliyografik başlangıç. | Bu taramada asıl tam metin doğrulanmadı; modern çeyrek tahmini için ölçülmüş bağımsız kanıt diye kullanılmadı. |

## Önerilen değişken blokları

Bu tablo **uyarlama önerisidir**. Katkı sırası, kendi verimizde zaman dışı deneyle belirlenecek.

| Öncelik | Blok | Adaylar | Dayanak |
|---|---|---|---|
| 1 | Geçmiş sonuçlar | EPS, net kâr, ciro; son açıklanmış ve geçen yıl aynı çeyrek; son 4–8 dönem; mevsim | Dario, Minsu, Scherrmann–Elsas |
| 2 | Kârın bileşimi | CFO, tahakkuk, brüt/faaliyet marjı, vergi gideri, efektif vergi, faiz gideri | Cao–You; EPSBench'in muhasebe köprüsü |
| 2 | Sermaye ve çalışma döngüsü | Aktif, özkaynak, borç, alacak, stok, ticari borç, yatırım harcaması ve bunların değişimleri | Forma; Cao–You; Elend |
| 3 | Piyasa ve ekonomi | Getiri, hacim, oynaklık, kur, faiz, enflasyon, üretim, emtia | Scherrmann–Elsas; Koval. Türkiye eşlemesi bu araştırmanın önerisi. |
| 3 | Metin ve faaliyet | Geçmiş yönetim açıklaması, talep/maliyet beklentisi; varsa satış hacmi, kapasite, sipariş, fiyat | Koval; şirkete özgü faaliyet ölçüleri ayrıca test edilecek öneri. |

Değişkenlerin eklenmesini tek tek önem sıralamasıyla değil **blok çıkarma deneyleriyle** değerlendirmek daha açıklayıcı olur: EPS geçmişi → muhasebe → makro/piyasa → metin. Aynı ileri dönemlerde aynı baz modellerle kıyaslanmalı. Muhasebe seviye/dönem birimleri ve bilginin ilk açıklanma zamanı doğrulanmadan performans farkına anlam yüklenmemeli.

Küresel risk ve şirket maruziyeti için yeni inceleme: [değişken seçimi ve risk skoru taslağı](DEGISKEN_SECIMI_VE_RISK_SKORU.md). GPR, GEPU, OFR FSI ve WUI'nin farkları; riskin coğrafi satış, döviz pozisyonu ve borç yapısıyla birlikte kullanımı; yayın gecikmeleri ve karşılaştırmalı deney planı burada açıklanır.
