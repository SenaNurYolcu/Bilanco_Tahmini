# Projelerin algoritmaları ve çalışma mekanikleri

İnceleme tarihi: **2026-11-06**. İlk üç için kaynak manifestosundaki sabit commit arşivleri okundu. Burada eğitim yeniden çalıştırılmadı; aşağıdaki açıklama kod ve yöntem incelemesidir. Projede bulunan seçeneklerle kanonik deneyde etkin seçenekler ayrılmıştır.

## ML, derin öğrenme ve muhasebe katmanı

Makine öğrenmesi, geçmiş girdiler ile gerçekleşmiş sonuçlar arasındaki ilişkiyi veriden öğrenme çerçevesidir. Derin öğrenme bunun sinir ağları kullanan alt grubudur. LLM ve zaman serisi temel modelleri de öğrenilmiş modellerdir; fakat aynı veri biçimini ve aynı eğitim işini yapmazlar.

| Yaklaşım | Öğrenilen şey | Bu araştırmadaki örnek |
|---|---|---|
| Doğrusal regresyon | Girdilerin ağırlıkları | Dario OLS, Minsu Ridge |
| Ağaç toplulukları | Koşullara bağlı doğrusal olmayan ilişkiler | HistGradientBoosting, CatBoost, Random Forest |
| Sıra/sinir ağı | Geçmiş dönem örüntüleri ve kanallar arası ilişkiler | LSTM, TimeXer, Forma |
| Önceden eğitilmiş zaman serisi modeli | Çok sayıda seriden önceden öğrenilmiş örüntülerin aktarımı | Chronos-2 |
| LLM + araçlar | Belgelerden kanıt toplama ve finansal sürücü tahmini | EPSBench, Streetbench |
| Muhasebe hesabı/düzeltmesi | Önceden tanımlanmış eşitlikler; öğrenilmesi şart değil | Brüt kâr hesabı, EPS hesaplayıcı, tahmin uzlaştırması |

“ML kullanıyor” demek her projede yeni bir algoritma icat edildiği anlamına gelmez. Katkı; model mimarisinde, girdilerin kodlanmasında, eğitim hedefinde, veri zamanlamasında veya farklı modellerin birleştirilmesinde olabilir.

## 1. Dario: standart denetimli regresyon

Kaynaklar: [models.py](https://github.com/dario-disanto/quarterly-eps-forecast-study/blob/d67b39e470cc7aa66e855e589915938dc3da6af4/src/epsforecast/models.py), [features.py](https://github.com/dario-disanto/quarterly-eps-forecast-study/blob/d67b39e470cc7aa66e855e589915938dc3da6af4/src/epsforecast/features.py), [REPORT.md](https://github.com/dario-disanto/quarterly-eps-forecast-study/blob/d67b39e470cc7aa66e855e589915938dc3da6af4/REPORT.md).

### Veri birimi

Her satır bir şirketin bir mali çeyreğini temsil eder. Girdiler daha önceki dönemlerden oluşturulur; cevap o satırın gerçekleşmiş EPS'sidir. Birçok şirketin geçmiş satırları aynı modelde birleştirilir.

1. Şirket ve mali dönem sırasını kurar.
2. Önceki çeyrek EPS'sini, geçen yıl aynı çeyrek EPS'sini ve altı gecikmeli oranı üretir.
3. Eksik mali dönem varsa sıradaki satırı yanlışlıkla “bir çeyrek önce” saymaz.
4. Eski tarihleri eğitime, sonraki tarihleri teste ayırır.
5. Aşırı değer sınırlarını eğitimden öğrenir. Eğitim hedefini ve girdilerini, testte ise yalnızca girdileri kırpar; test sonucu ham gerçekleşmiş EPS'ye karşı ölçülür.
6. Aynı veri üzerinde OLS ve HistGradientBoosting modellerini ayrı ayrı eğitir.

### OLS nasıl çalışır?

`EPS_tahmin = sabit + a*önceki_EPS + b*geçen_yıl_EPS + ...`

Katsayılar toplam karesel hatayı azaltacak biçimde öğrenilir. Şirket içinde ilişkili hatalara göre düzeltilmiş standart hatalar ayrıca hesaplanır. Bu düzeltme katsayıların istatistiksel değerlendirmesini etkiler; yeni bir tahmin algoritması veya muhasebe kısıtı değildir.

### HistGradientBoosting nasıl çalışır?

Başlangıç tahmininin üzerine ardışık küçük karar ağaçları ekler. Her ağaç mevcut modelin kalan hatasını düzeltmeye çalışır. Örneğin marj ile geçmiş EPS'nin birlikte etkisini farklı dallarla öğrenebilir; bu ilişkilerin doğrusal olması gerekmez. Projede `max_depth=3`, `learning_rate=0.05`, `max_iter=400`, `l2_regularization=1.0` kullanılıyor.

### Ekstra ne var?

Finansal özellik üretimi, mali takvim kontrolü, eğitimden öğrenilen uç değer sınırları, sezonluk basit tahminle kıyas ve hata farklarının istatistiksel analizi. Yeni bir sinir ağı mimarisi, otomatik hiperparametre taraması veya birden çok modeli tek tahminde birleştiren ensemble yok. Hedef tek EPS; tablolar arası muhasebe eşitlikleri uygulanmıyor.

## 2. Forma: finansal tabloya özel Transformer

Kaynaklar: [model kodu](https://github.com/forma-lab-mccombs/forma-release/blob/65074edf6f7baea5176ec53f3454325ec370f8cc/src/forma/models/forma.py), [veri ve maskeleme](https://github.com/forma-lab-mccombs/forma-release/blob/65074edf6f7baea5176ec53f3454325ec370f8cc/src/forma/data/forma_data.py), [kanonik ayar](https://github.com/forma-lab-mccombs/forma-release/blob/65074edf6f7baea5176ec53f3454325ec370f8cc/configs/r13_forma_fgrid_seed60.yaml), [makale](https://arxiv.org/abs/2608.11327).

### 2.1 Sayıları nasıl temsil ediyor?

Geçmiş 12 çeyreğin 78 kalemini `(hesap, göreli çeyrek, değer)` üçlülerine çevirir. Örnek: `(ciro, -1, 100)` ve `(stok, -1, 25)`. Buradaki rakamlar anlatım için örnektir. Şirket büyüklüğüyle ölçekleme, asinh dönüşümü, standardizasyon ve kırpma uygulanır.

Model her üçlüye hesap türü, zaman ve sayısal değer temsili verir. Sektör için ayrı bir temsil kullanır. **Ek olarak bugünkü şirket büyüklüğünü taşıyan bir `scale` girdisi vardır.** Bu ölçek belirteci 78 tahmin hedefinden biri değildir ve gelecekte sorgulanmaz.

Eksik tarihsel kalemler raporlanmış gibi doldurulmaz; mevcut üçlüler kullanılır. Gelecekte tahmin edilecek hesap/çeyrek çiftleri için değeri gizli sorgular oluşturulur. Sorgu oluşturma, daha sonra hangi şirketin veya kalemin gözleneceği bilgisini girdi biçiminden sızdırmayacak şekilde tasarlanmıştır.

### 2.2 Nasıl öğreniyor?

Geçmişte sonucu artık bilinen örneklerden sayılar saklanır; model saklanan sayıları geri tahmin eder. Eğitim örneklerinin bir kısmında bütün gelecek blok gizlenir. Diğerlerinde geleceğin çoğu gizlenir, küçük bir bölümü koşul olarak görünür bırakılır. Böylece hem saf tahmin hem koşullu senaryo öğrenilir.

Tarihsel veride de bazı kalemler maskelenir. Muhasebe eşitliğiyle bağlı bir grupta en az iki sayının birlikte gizlenmesi, tek eksik sayıyı basit çıkarma işlemiyle bulmayı zorlaştırır. Bu işlem **maskeleme tasarımıdır**, eşitliği çıktıda zorla sağlatma değildir.

Transformer'ın attention işlemi, bir hesap/dönem temsilini diğer hesap/dönem temsilleriyle ilişkilendirir. Satış, maliyet, stok, alacak ve borç bilgisini birlikte kullanabilir. Attention ağırlıklarını tek başına nedensellik veya güvenilir açıklama saymak doğru olmaz.

### 2.3 Neyi çıkarıyor?

Her hedef hesap ve ufuk için tahmini merkez ile belirsizlik ölçeği üretir. Kanonik deney Gaussian beta-NLL (`beta=0.5`) kullanır; ayrıca Laplace varyantı vardır. Kayıp, maskelenmiş ve gerçek sonucu mevcut kalemlerde hesaplanır. Bir sonraki çeyreğin tahminini girdiye çevirip 20 kez ilerlemek yerine, istenen hesap/ufukları tek geçişte birlikte çıkarır.

Kanonik mimari dört Transformer katmanı, 128 boyutlu temsil ve dört attention başlığı kullanır. Beş farklı rastgele başlangıçla bağımsız eğitim yapılır; tahmin dağılımları eşit ağırlıklı karışımla birleştirilir. Eğitim ufku başlangıçtaki dört çeyrekten kademeli olarak 20 çeyreğe genişler.

### 2.4 Muhasebe eşitlikleri gerçekten zorunlu mu?

**Kanonik ayarda hayır:** `constraint_mode: none`, `reconcile: false`. Kodda bir kısıt düzeltme katmanı bulunması, yayımlanan ana deneyde etkin olduğu anlamına gelmez. Model muhasebe ilişkilerini veri ve ortak eğitimden öğrenmeye çalışır; ham tahminlerin tam olarak denkleşmesi garanti değildir.

Makale ayrıca tahmin sonrasında eşitlikleri sağlayan uzlaştırma/projeksiyon deneylerini inceler. Bu işlem ayrı bir aşamadır. Bizim ürünümüzde tam denklik isteniyorsa bunu açık bir hesaplama/uzlaştırma bileşeni olarak tasarlamak gerekir.

### 2.5 Forma'daki özgün taraf

Temel Transformer bileşenleri bilinen yöntemlerdir. Finansal hesapların üçlü temsili, eksik raporlamanın işlenmesi, muhasebe ilişkilerine göre maskeleme, ortak çok kalem/çok ufuk hedefi ve senaryo koşullandırması bu alana özgü tasarımdır. Sayısal tahmin için uzmanlaşmış derin öğrenmedir; metin üzerinden rapor yazan bir sohbet modeli olarak çalışmaz.

## 3. Minsu: hazır model aileleri ve deney/veri sistemi

Kaynaklar: [tabular.py](https://github.com/minsu0011/eps-forecasting/blob/aee8a79405c845ae4d66f946b437a357f8e3d1b1/research/eps_model_lab_v2/tabular.py), [sequence.py](https://github.com/minsu0011/eps-forecasting/blob/aee8a79405c845ae4d66f946b437a357f8e3d1b1/research/eps_model_lab_v2/sequence.py), [model reçeteleri](https://github.com/minsu0011/eps-forecasting/blob/aee8a79405c845ae4d66f946b437a357f8e3d1b1/research/eps_model_lab_v2/freeze_inputs.py), [ensemble.py](https://github.com/minsu0011/eps-forecasting/blob/aee8a79405c845ae4d66f946b437a357f8e3d1b1/research/eps_model_lab_v2/ensemble.py).

### 3.1 Hangi modeller?

V2'de tanımlanan ve karşılaştırılan aileler:

| Aile | Çalışma fikri |
|---|---|
| Ridge | Katsayıları cezalandırılarak aşırı uyumu azaltılan doğrusal regresyon. |
| HistGradientBoosting | Küçük ağaçların ardışık hata düzeltmeleri. |
| CatBoost | Gradient boosting ağaçları; bu deneyde sayısal hazırlanmış özellik matrisiyle kullanılıyor. |
| NGBoost-Laplace | Yalnızca nokta yerine dağılımın parametrelerini öğrenen boosting yaklaşımı. |
| LSTM | Zaman sırasındaki bilgiyi bellek durumu üzerinden taşıyan sinir ağı. |
| DLinear | Geçmiş seriyi eğilim/mevsim bileşenlerine ayıran doğrusal zaman serisi modeli. |
| XLinear, SOFTS | Zamansal ve çok kanallı ilişkileri farklı karıştırma/özetleme yapılarıyla öğrenen modeller. |
| TimeXer | Zaman serisi ve ilişkili kanallar için attention tabanlı model. |
| Chronos-2 | Önceden eğitilmiş zaman serisi temel modeli; doğrudan kullanım ve EPS/TTM görevlerine ek eğitim varyantları. |

Liste her modelin nihai ensemble'a girdiği anlamına gelmez. Aynı model ailesinin farklı temsil veya zaman pencereleriyle çalıştırılması da yeni bir algoritma icadı değildir.

### 3.2 Veriyi ve hedefi nasıl hazırlıyor?

SEC kayıtlarını şirketin kendi mali takvimine yerleştirir; EPS, TTM, birim ve hisse sayısı tutarlılığını kontrol eder. Tablo modelleri 88 özellik kullanır. Sıra modelleri 32 dönemlik EPS/TTM kanalları ve mevcutluk/eskilik/mevsim bilgisini kendi giriş yapısıyla işler.

Bir eğitim satırının geçmişte olması yeterli sayılmaz; tahmin edilmesi istenen cevabın da eğitim kesiminden önce açıklanmış olması gerekir. Ek finansal kalemleri kullanacak Track A, doğrulanmış gelişim verisi bulunmadığından bloke edilmiştir. Bu nedenle mevcut sonuçları geniş finansal tablo modelinin başarısı olarak okumamalı.

### 3.3 Direct ve residual farkı

Direct model EPS'yi doğrudan öğrenir. Residual model, basit başlangıç tahmininden sapmayı öğrenir:

`son tahmin = basit tahmin + modelin öğrendiği düzeltme`

Örnek: son bilinen EPS 2 TL, gelecek EPS 2,30 TL ise residual hedef 0,30 TL olur. Bu rakamlar açıklayıcı örnektir. Ayrıca negatif değerlerde de çalışabilen asinh hedef dönüşümü denenir. Tahmin sonunda dönüşüm geri alınır.

### 3.4 Eğitim pencereleri ve birleştirme

- **Expanding:** eldeki eski dönemlerin hepsini kullanır.
- **Rolling:** son beş yıllık eğitim penceresiyle sınırlar.
- **Recency weighted:** yeni gözlemlere daha çok ağırlık verir; yarı ömür iki yıl.

Modeller gelişim döneminde kıyaslanır. Üyeler ve ağırlıklar sonraki kontrol sonuçlarına bakılmadan sabitlenir. Basit ortalama, medyan, kırpılmış ortalama ve negatif olmayan/toplamı bir ağırlıklarla birleştirme uygulanır. Bu son yöntemde ağırlıklar geçmiş mutlak hatayı küçültecek şekilde seçilir.

Bazı olasılıksal modellerin aralıkları geçmiş tahmin hatalarıyla genişletilir. Zaman bağımlılığı ve değişen veri dağılımı nedeniyle bu kalibrasyon gelecekte belirli kapsamayı garanti etmez.

### 3.5 Ekstra ne var?

Özel bir sıfırdan ağ icadından çok, hazır modellerin etrafında mali dönem/birim/veri zamanı kontrolleri, temsil ve eğitim penceresi deneyleri, tahmin birleştirme ve tekrar üretilebilirlik kontrolleri vardır. Chronos aktarımı ve residual hedef gibi standart ama önemli ek teknikler kullanılır. Başlıca çıktı EPS'dir; bütün bilançoyu birlikte üretmez.

## 4. Tüm finansal tablolar için ek örnek: chained GBM

[Forma deposundaki uygulama](https://github.com/forma-lab-mccombs/forma-release/blob/65074edf6f7baea5176ec53f3454325ec370f8cc/src/forma/models/chained_gbm.py), Geertsema–Lu–Ma yaklaşımını izleyen ayrı bir rakip modeldir. Forma'nın Transformer bloğunun içinde çalışmaz.

14 adımlı sırada LightGBM modelleri kurar. Önce ciro, sonra maliyet/alacak, sonra stok/ticari borç gibi kalemler tahmin edilir. Sonraki model, geçmiş özelliklere ek olarak önceki adımların hedef döneme ilişkin çıktılarını alır.

Eğitimde önceki basamakların gerçekleşmiş değerleri verilir (**teacher forcing**). Tahminde bu değerler bilinmediği için önceki basamakların tahminleri kullanılır (**cascade**). Böylece kalemler arasında ilişki kurulur; önceki adımın hatası sonraki adıma taşınabilir. Bu, finansal yapıdan yararlanmanın daha anlaşılır bir alternatifi. Muhasebe alt toplamlarını eşitliklerle oluşturma veya uzlaştırma yine ayrıca tanımlanmalıdır.

## 5. Diğer incelenen projeler hangi sınıfta?

Bu tablo önceki araştırmanın kaynak incelemesini özetler. İlk üç dışındaki bütün depoların bütün eğitim yolları yeniden denetlenmedi; ayrıntılı veri sınırları [değişken belgesinde](PROJELERIN_DEGISKENLERI.md).

| Proje | Model/işlem | Modelin çevresindeki ek mekanizma |
|---|---|---|
| FP&A ML Comparison | OLS, RF, XGBoost; gecikme ve ortalama baz modelleri | SEC/FRED verisi, kümülatif CFO'yu çeyreğe çevirme, ilerleyen eğitim doğrulaması |
| DeepEarnings | Finansal ve metin kollarında sinir ağı; fiyat kolunda çift yönlü LSTM | Oranlaştırma, sözlük duyarlılığı, KNN eksik doldurma; hedef beklentiyi aşma sınıfı |
| EPSBench | LLM ajanı + dinamik muhasebe hesaplayıcı | Belgelerden kanıt, şirkete özgü ara sürücüler, formül grafiğiyle EPS ve hata ayrıştırma |
| Streetbench | Farklı LLM/ajan araştırma kurulumları | Tarih kesimli web kanıtı, kaynaklı gerekçeler ve ortak EPS puanlaması |
| ForecastGPT | LLM + RAG | PDF'den metrik çıkarma ve deterministik değişim hesabı; nitel gelecek dönem raporu |
| JamesEzeilo SGD | SGDRegressor ile doğrusal regresyon | StandardScaler ve şirketler arası rastgele ayırma; zaman dışı gelecek dönem kanıtı yetersiz |
| Corporate Earnings Prediction | Doğrusal/ağaç/sinir ağı seçenekli demo | Sentetik veriler ve üretilmiş teknik/makro alanlar; uygulama hataları nedeniyle sonuçlar kanıt sayılmadı |
| Earnings Surprise Prediction Platform | XGBoost sınıflandırıcı | Gecikmeli sürprizler, haber duyarlılığı, rolling backtest, API; kısmen sentetik veri |
| Predicting PER | LSTM/RNN | Piyasa değeriyle ölçekleme ve ileri F/K bileşenleri; test tasarımı sınırlı |
| PSX Financial Health | Lasso, ElasticNet, XGBoost, Gradient Boosting, RF, ExtraTrees, KNN | Oran bazında model seçme ve özellik türetme; aynı dönem hedef bilgisini içeren girdiler var |
| Earnings Engine | LightGBM sınıflandırıcı + Platt kalibrasyonu | Walk-forward eğitim; geçmiş açıklama tepkileri; çıktı açıklama sonrası fiyat yönü |
| Moozzart EPS | RF ve ANN; kodda XGBoost denemeleri de var | EPS şoku, gecikmeler, finansal türevler ve analist kıyası; final girdi akışı tam sabitlenmemiş |
| DhirainVij Earnings | LSTM, GRU, CNN-LSTM, RNN | Net kârın dört gözlemlik pencereleri ve ölçekleme; okunan bütün kolonlar modele girmiyor |

## 6. Bizim proje için anlamı

Buradaki öneri, BIST üzerinde doğrulanmış sonuç değil, kaynaklardan türetilen bir tasarım seçeneğidir:

1. Aynı mali dönem/birim/yayın zamanında temiz bir şirket paneli oluşturmak.
2. Basit sezonluk tahmini ve standart boosting modellerini referans olarak kurmak.
3. Bağımsız hedefler, zincirlenmiş hedefler ve ortak çoklu çıktı modellerini aynı ileri dönemlerde kıyaslamak.
4. Bazı alt toplamları hesapla üretmek; kalan muhasebe eşitliklerini açık uzlaştırmayla sağlamak.
5. Kalem bazında hata ve tahmin aralığı kapsamını ayrı ölçmek.

Finansal yapının modelde veya hesap katmanında yer alması hedefimiz için önemlidir. “Transformer kullanıyor” veya “çok model birleştiriyor” tek başına başarı gerekçesi değildir.

## Geliştirici deneyimi: nokta tahmini ve aralık ayrı ölçülmeli

- 🔍 [Mistral shipped a time-series foundation model today. I measured its latency — and its confidence.](https://dev.to/frankchu/mistral-shipped-a-time-series-foundation-model-today-i-measured-its-latency-and-its-confidence-4mdd) [@frankchu](https://dev.to/frankchu) — Yazarın kendi küçük deneyinde nokta hatası iyileşirken aralık kapsamı zayıf kalıyor; bu bulgu burada anılan EPS modellerinin sonucuna genellenmeden, iki ölçüyü ayrı test etme gerekçesi olarak kullanıldı. 🔗 [Read Full Discussion on DEV](https://dev.to/frankchu/mistral-shipped-a-time-series-foundation-model-today-i-measured-its-latency-and-its-confidence-4mdd)

Yorumlarda log dönüşümünü ayrıca deneme önerisi var; doğrulanmış bir çözüm olarak sunulmadı. Bu topluluk notu proje kodlarının ve makalelerin yerine kullanılmadı.
