# Açıklanmamış finansal sonuçları makine öğrenmesiyle tahmin etme

Araştırma tarihi: **2026-11-06**. Bu sıralama, incelenen açık GitHub depoları arasında **istenen hedefe uygunluk, kodun denetlenebilirliği ve değerlendirme kalitesi** için yapılmıştır. Ortak veri setinde yeniden eğitim yapılmadığından evrensel bir doğruluk sıralaması değildir.

## Sonuç

İhtiyaca en uygun üç proje:

1. **[Forma](https://github.com/forma-lab-mccombs/forma-release)**: finansal tabloların çok sayıda kalemini birlikte tahmin etmek için en kapsamlı araştırma temeli.
2. **[Quarterly EPS Forecast Study](https://github.com/dario-disanto/quarterly-eps-forecast-study)**: sıradaki çeyreğin hisse başına kârını tahmin eden, anlaşılır ve küçük bir başlangıç modeli.
3. **[EPS Forecasting](https://github.com/minsu0011/eps-forecasting)**: EPS geçmişi üzerinde farklı model ailelerini karşılaştırmak ve verinin ne zaman bilinebilir olduğunu yönetmek için yararlı bir araştırma deposu.

**Hiçbiri herhangi bir BIST hissesinde hazır ve doğrulanmış bir tahmin hizmeti sunmuyor.** Üçü de ağırlıklı olarak ABD verileriyle çalışıyor. İkinci ve üçüncü proje tüm finansal tabloyu değil EPS'yi hedefliyor. “Bilanço” sözcüğü burada gelir tablosu, finansal durum tablosu ve nakit akış tablosunu kapsayacak geniş anlamıyla kullanıldı.

Sıradaki açıklanacak rapor ile bir sonraki takvim çeyreği aynı olmayabilir: henüz açıklanmamış rapor bitmiş bir döneme ait olabilir. Uygulamada hedef, şirketin mali takvimi ve açıklama tarihinden belirlenmeli; bugüne üç ay eklenerek seçilmemeli.

## İlk üçün karşılaştırması

| Özellik | Forma | Quarterly EPS Forecast Study | minsu0011/EPS Forecasting |
|---|---|---|---|
| Hedef | Üç tablodan 78 kalem; 1–20 çeyrek sonrası | Bir çeyrek sonrası seyreltilmiş EPS, olağanüstü kalemler hariç | Sonraki çeyreğin GAAP seyreltilmiş EPS'si; ayrıca 4 çeyrek yolu ve ilerideki TTM |
| Yöntem | Hesap–çeyrek–değer üçlülerini işleyen Transformer; olasılıksal çıktı | OLS ve HistGradientBoosting | Ridge, HistGB, CatBoost, LSTM gibi sıra modelleri, Chronos, NGBoost, topluluk modelleri |
| Ana veri | WRDS/Compustat; sektör | WRDS/Compustat | SEC açıklamaları ve mali dönem kayıtları |
| Girdi | 12 çeyrek geçmiş; 78 kalem ve FF48 sektör | EPS'nin 1 ve 4 çeyrek gecikmesi ile 6 gecikmeli oran | V2 tablo modelinde EPS/TTM gecikmeleri, maskeler ve EPS'den türetilen özellikler |
| Makro / haber | Kanonik Forma girdisinde yok | Yok | V2 `native_features` girdisinde yok |
| En yararlı yön | Kalemleri birlikte tahmin etmesi; muhasebe ilişkileri | Basitlik; sezonluk tahminle açık karşılaştırma | Dönem, birim, açıklanma zamanı ve model ailelerini ayırması |
| Başlıca sınır | Lisanslı veri; ağırlıklar ayrı ve erişim koşullu; finans şirketleri hariç | Güncel yeniden düzenlenmiş veri; tek zaman bölmesi | Küçük sabit şirket grubu; önce görülmüş doğrulama dönemleri; ek muhasebe kanalı bloke |

Kaynaklar: [Forma model deposu](https://github.com/forma-lab-mccombs/forma-release), [ProForma-20Q veri ve değerlendirme protokolü](https://github.com/forma-lab-mccombs/proforma-20q), [Dario araştırma raporu](https://github.com/dario-disanto/quarterly-eps-forecast-study/blob/main/REPORT.md), [Minsu hedef/veri tasarımı](https://github.com/minsu0011/eps-forecasting/blob/main/docs/wiki/Target-and-Data-Design.md).

### 1. Forma

Model ve karşılaştırma kodu `forma-release`, veri oluşturma/değerlendirme kodu `proforma-20q` deposunda. Kanonik girdilerde şirket kimliği yerine geçmiş finansal kalemler ve sektör kullanılıyor. Bu, yeni şirkete uygulama niyetini destekler; ülke veya muhasebe standardı değişiminde başarı kanıtı oluşturmaz.

Girdiler arasında ciro, satış maliyeti, faaliyet giderleri, Ar-Ge, amortisman, faiz ve vergi gideri, net kâr, nakit, alacaklar, stoklar, maddi duran varlıklar, borç, özkaynak, işletme nakit akışı, yatırım harcaması ve temettüler bulunuyor. Eksik kalemler seyrek üçlü yapısıyla işleniyor. Model; gelecekteki gelir yolunun verilmesi gibi koşullu senaryoları da destekliyor.

Makaledeki genel değişim-uzayı R² yaklaşık **0,289**; bu **tek sonraki çeyrekte %28,9 doğruluk** demek değildir. Farklı kalem ve ufuklardan oluşan ortak örneklemde ölçülmüş bir performans istatistiğidir. Ağırlık, veri ve kod lisanslarının ayrı olması doğrudan ürünleştirmeyi etkiler. [Makale](https://arxiv.org/abs/2608.11327), [lisans ve yeniden üretim açıklaması](https://github.com/forma-lab-mccombs/forma-release#license).

### 2. Quarterly EPS Forecast Study

Kodda yalnızca sekiz tahmin girdisi var: iki EPS gecikmesi, işletme nakit akışı/aktifler, tahakkuk/aktifler, brüt marj, aktif devir hızı, yıllık satış büyümesi ve uzun vadeli yükümlülük/aktifler. Oranlar bir çeyrek geciktiriliyor; mali takvimde boşluk varsa yanlış gecikme oluşturulmuyor. [Girdi kodu](https://github.com/dario-disanto/quarterly-eps-forecast-study/blob/main/src/epsforecast/features.py).

Yazarın gerçek veri sonuçlarında GBM MAE'si **0,7530**, sezonluk basit tahmininki **0,8469**; fark yaklaşık %11,1. Ham hedefte RMSE kazancı yalnızca %0,48. Ayrıca sadece iki EPS gecikmesiyle kurulan GBM, tüm girdileri kullanan modele çok yakın. Bu nedenle çalışmadan “ne kadar çok oran, o kadar iyi” sonucu çıkmıyor. Sonuçlar bu incelemede yeniden üretilmedi. Lisanslı veri bulunmazsa depo sentetik veri oluşturuyor; sentetik çalıştırma gerçek sonuçları yeniden üretmek sayılmaz. [Sonuçlar ve sınırlar](https://github.com/dario-disanto/quarterly-eps-forecast-study/blob/main/REPORT.md).

### 3. minsu0011/EPS Forecasting

V2 tablo modelinin giriş fonksiyonu 32 EPS ve 8 TTM geçmiş değeri, bunların gözlem maskeleri, EPS büyüme/hızlanma/oynaklık ölçüleri, zarar işareti, mali çeyrek döngüsü, gözlem sayısı ve veri eskiliğini kullanıyor. **Geniş muhasebe kanallarının araştırılmış olması, yayımlanan V2 sonucun bu kanalları kullandığı anlamına gelmiyor.** Kodda kontrol edilen `native_features` 88 sütun üretir. Sıra modellerinin girdisi ayrı oluşturuluyor. [Tablo girdisi](https://github.com/minsu0011/eps-forecasting/blob/main/research/eps_model_lab_v2/model_common.py), [sıra girdisi](https://github.com/minsu0011/eps-forecasting/blob/main/research/eps_model_lab_v2/sequence.py).

Depo birim ve dönem hatalarını, yetersiz doğrulanmış muhasebe girdilerini ve başarısız uzun vadeli hedefleri açıkça belgeliyor. Ancak 69 şirketlik seçilmiş örneklem, tarihsel verinin sonradan düzeltilmesi ve daha önce görülmüş kontrol dönemleri güçlü genelleme iddiasını sınırlar. Ayrı veri ve ağırlık hazırlığı gerekiyor. [Sınırlar](https://github.com/minsu0011/eps-forecasting/blob/main/docs/limitations.md).

## Diğer incelenen projeler

Aşağıdaki kapsam, değişken belgesindeki **16 projeye** karşılık gelir. Forma'nın yardımcı benchmark deposu ayrıca arşivlendi. Aramalarda çıkan maaş, YouTube geliri ve konuyla ilgisiz fiyat örnekleri proje listesine alınmadı.

| Proje | İlk üç dışında kalma gerekçesi |
|---|---|
| [Financial Forecasting FP&A ML Comparison](https://github.com/alpdemiroz1994/financial-forecasting-fpa-ml-comparison) | Faaliyet kârı/nakit akışı için yararlı ek örnek. Notebook sonuçlarında ML basit yöntemleri tutarlı biçimde geçmiyor; OCF testinde yalnızca 18 kullanılabilir gözlem belirtiliyor. |
| [DeepEarnings](https://github.com/alexanderpei/DeepEarnings) | Kâr tutarını değil beklentiyi aşmayı sınıflandırıyor. İmputasyon/standardizasyon ayrımdan önce; örnekler şirket blokları halinde hazırlanıyor. İlan edilen test oranı güçlü zaman dışı kanıt sayılmadı. |
| [EPSBench](https://github.com/chuyuxu/EPSBench) | Sıradaki açıklama için iyi muhasebe sürücüsü örneği; esas olarak LLM ajan değerlendirmesi. Sabit sayısal ML modeli değil. |
| [Streetbench](https://github.com/fundamental-research-labs/streetbench) | LLM ve web araştırması benchmark'ı; geriye dönük kurulum. Sabit eğitim değişkenleri ve BIST doğrulaması yok. |
| [ForecastGPT](https://github.com/abhay-yemekar/forecastgpt-financial-outlook-agent) | Sayısal kâr regresyonundan çok kaynaklara dayalı nitel gelecek dönem raporu üretiyor. |
| [EPS Forecasting ML SGD](https://github.com/JamesEzeilo/eps-forecasting-ml-sgd) | Şirketler arası mevcut EPS kestirimi; rastgele bölme ve negatif test R². Sıradaki açıklamayı zaman dışı tahmin ettiğini göstermiyor. |
| [Corporate Earnings Prediction](https://github.com/kryptologyst/Corporate-Earnings-Prediction) | Sentetik veri demosu. Bazı özellik hesaplarında tüm seri sonundan değer okunuyor; isimleri ekonomik olarak makul olsa da sonuçlar gerçek finansal kanıt değil. |
| [Earnings Surprise Prediction Platform](https://github.com/AnanmayS/Earnings-Surprise-Prediction-Platform) | Beat/miss sınıflandırması; tarihsel veri kısmen sentetik, bazı canlı alanlar tahminî yedek girdilere dönüyor. |
| [Predicting PER](https://github.com/my2582/predicting-per) | Ana hedef ileri F/K ve bileşenleri. README eğitim/test için aynı veriyi kullandığını belirtiyor; güvenilir zaman dışı kıyas değil. |
| [Financial Health Forecasting PSX](https://github.com/UmerMuzaffar/financial-health-forecasting-psx) | Yıllık finansal oran tahmini. Notebook'ta aynı yılın hedefini içeren trend/ortalama/oran girdileri bulunuyor; yüksek R² değerleri açıklanmamış dönem başarısı olarak okunamaz. |
| [Earnings Engine](https://github.com/chandewardnyanesh/earnings-engine) | Hedef açıklama sonrası fiyat yönü; bilanço tutarı değil. |
| [Moozzart EPS Prediction](https://github.com/Moozzart/Beating-Analysts-Predictions-Using-Machine-Learning-Algorithms-to-predict-EPS-of-US-Firms) | İlgili EPS/RF/ANN örneği; değişken ve model kıyaslarından yararlanılabilir, değerlendirme disiplini ilk üç kadar açık değil. |
| [DhirainVij Earnings Prediction](https://github.com/DhirainVij/earnings-prediction) | Tek şirket odaklı küçük çalışma; geniş şirket evrenine genelleme kanıtı yetersiz. |

## Kendi modelin için başlangıç önerisi

Bu bölüm, kaynakların sentezinden üretilmiş uygulama önerisidir; BIST üzerinde yapılmış bir deney sonucu değildir.

1. Hedefleri ayrı tut: ciro, faaliyet kârı/FAVÖK, ana ortaklık net kârı ve uygun hisse sayısıyla EPS. Rapor tanımlarını veri boyunca sabitle.
2. İlk temel modelde hedefin son açıklanmış değeri, geçen yıl aynı dönem değeri ve son 4–8 çeyreği kullan. Tek şirketin az sayıdaki çeyreği yerine yeterli veri varsa şirketler arası bir panel model dene.
3. İkinci blokta marjlar, nakit akışı, tahakkuklar, vergi, faiz, borç, özkaynak, stok/alacak ve yatırım kalemleri ekle. Seviye yanında yıllık değişimleri ve aktif/satışla ölçeklenmiş karşılıkları dene.
4. Makro ve sektör bloklarını ayrıca ölç: kur, enflasyon, faiz, sanayi üretimi, emtia ve şirketin satış hacmi/kapasite gibi faaliyet göstergeleri. Her değişken tahmin tarihinde yayımlanmış olmalı.
5. Yönetim açıklamaları ve geçmiş faaliyet raporları için metin kanalı ekle; hedef dönemin gelecekte yayımlanacak raporunu girdiye koyma.
6. Her blok eklenince ilerleyen zaman pencerelerinde aynı basit tahminlere karşı hata farkını ölç. Negatif veya sıfıra yakın kâr için MAPE yerine MAE/RMSE ve ölçeklenmiş hataları kullan; tahmin aralıklarının kapsamasını ayrıca kontrol et.

**Öncelik sıram:** çalışan başlangıç için Dario'nun küçük modeli; tüm tabloları birlikte tahmin etme hedefi için Forma; dönem/birim/açıklanma kontrolleri için Minsu'nun tasarımı. Değişken seçiminin akademik dayanakları [makale notlarında](MAKALELER.md), her projenin somut girdileri [değişken belgesinde](PROJELERIN_DEGISKENLERI.md).

## İnceleme yöntemi ve doğrulama sınırı

README'ler, seçili özellik üretme/eğitim dosyaları, makalelerin yöntem ve değişken bölümleri incelendi. Bütün depolardaki her satırın denetimi yapılmadı. Bildirilen başarılar yazarların sonuçlarıdır. Veri indirilip modeller yeniden eğitilmedi. Kaynak arşivleri ZIP bütünlüğü ve SHA-256 ile, PDF'ler dosya imzası ve metin çıkarımıyla kontrol edildi. Erişilemeyen veya tam listesi yayımlanmayan girdiler değişken belgesinde açıkça işaretlendi.
