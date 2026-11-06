# İncelenen tüm projelerin değişken sözlüğü

Tarih: **2026-11-06**. Kapsam: ana raporda değerlendirilen **16 proje**. Bu belge GitHub'daki bütün projelerin envanteri değildir. Forma'nın yardımcı `proforma-20q` deposu aynı proje ailesidir.

**Okuma kuralı:** bir dosyada bulunan sütun, otomatik olarak model girdisi değildir. Aşağıda **gerçek girdi**, **aday girdi**, **ara hedef**, **son hedef**, **kimlik/tarih** ve **yalnızca raporda okunan alan** ayrılmıştır. Koddan tam liste çıkarılamayan yerlerde eksiklik yazılmıştır; muhtemel girdiler uydurulmamıştır.

## Ortak terimler

| Terim | Anlamı |
|---|---|
| EPS | Hisse başına kâr. Basic/temel ve diluted/seyreltilmiş farklı tanımlardır. |
| GAAP / adjusted | Raporlama standardındaki değer ile şirket/analist tarafından düzeltilmiş değer; birbirinin yerine kullanılamaz. |
| TTM | Son dört çeyreklik dönem. Hisse sayısı ve dönem tanımı tutarlı değilse dört EPS'yi toplamak aynı hedefi vermeyebilir. |
| `lag1`, `lag4` | Hedef döneme göre bir ve dört dönem önceki değer. Bir yılda dört çeyrek varsayılır. Minsu'daki `lag_0` ise tahmin anında bilinen en güncel değerdir. |
| YoY | Geçen yılın aynı dönemiyle karşılaştırma; genellikle `x_t/x_(t-4)-1`. |
| QoQ | Önceki çeyrekle karşılaştırma; tutar farkı veya büyüme oranı olabilir. Proje kodu esas alınmalıdır. |
| CFO / OCF | İşletme faaliyetlerinden nakit akışı. Kümülatif sunulan tutar, tek çeyrek tutarına çevrilmelidir. |
| Accruals / tahakkuk | Kâr ile nakit temelli sonuç arasındaki bileşenler. Her projedeki formül aynı değildir. |
| EBIT / EBITDA | Faiz ve vergi öncesi kâr / ayrıca amortisman öncesi kâr. |
| SG&A | Satış, genel yönetim ve idari giderler. |
| ROA / ROE | Aktif kârlılığı / özkaynak kârlılığı. Payda dönem sonu veya ortalama değer olabilir. |
| Mask | Bir gözlemin mevcut olup olmadığını söyleyen 0/1 işareti. Sıfır kârla eksik veriyi ayırır. |
| bps | Baz puan; 100 baz puan bir yüzde puandır. Büyüme oranıyla karıştırılmamalıdır. |
| Point-in-time | Yalnızca tahmin anında gerçekten açıklanmış bilgi. Eski dönemin sonradan düzeltilmiş verisi bunu tek başına sağlamaz. |

## 1. Forma — 78 kalemin geçmişi ve sektör

[Depo](https://github.com/forma-lab-mccombs/forma-release) · [Kanonik ayar](https://github.com/forma-lab-mccombs/forma-release/blob/main/configs/r13_forma_fgrid_seed60.yaml) · [78 kalemin tamamı ve Türkçe anlamları](EK_FORMA_78.md).

**Son hedefler:** 78 kalemin gelecek 1–20 çeyrek değerleri. **Gerçek girdiler:** aynı 78 kalemin geçmiş 12 çeyrekte raporlanmış değerleri; hesap kimliği; göreli çeyrek konumu; FF48 sektör kodu. Ayrıca başlangıç tarihindeki şirket büyüklüğünü taşıyan bir `scale` belirteci girer; bu 78 hedefin dışında bir yardımcı girdidir ve gelecekte tahmin edilmez. Hesap ve çeyrek kodu, muhasebe tutarının hangi hesaba/hangi döneme ait olduğunu belirtir. Şirket/ticker model özelliği olarak kullanılmaz.

| Grup | Örnekler ve anlamları |
|---|---|
| Gelir/maliyet/kâr | `revtq` ciro; `cogsq` satış maliyeti; `gpq` brüt kâr; `xsgaq` SG&A; `xrdq` Ar-Ge; `oiadpq` EBIT; `oibdpq` EBITDA; `niq` net kâr |
| Faiz/vergi/özel kalem | `xintq` faiz; `txtq` vergi gideri; `piq` vergi öncesi kâr; `spiq` özel kalemler |
| Varlıklar | `cheq` nakit/kısa yatırımlar; `rectq` alacak; `invtq` stok; `ppentq` net maddi duran varlık; `atq` toplam aktif |
| Finansman | `dlcq` kısa borç; `dlttq` uzun borç; `apq` ticari borç; `ltq` yükümlülükler; `seqq` özkaynak |
| Nakit akışı | `oancfq` işletme nakdi; `capxq` yatırım harcaması; `ivncfq` yatırım nakdi; `fincfq` finansman nakdi; `dvq` temettü |
| Türetilmiş | `fcfq` serbest nakit akışı; `wcapq` çalışma sermayesi; bazı alt toplamlar ve ayrıştırmalar |

Kanonik modelde makro, haber, fiyat ve analist konsensüsü yok. `proforma-20q` tabular görünümündeki alternatif modeller dört yakın seviye ve sekiz yıllık değişim kanalı ile sektör göstergeleri kullanır; bu görünüm Forma'nın üçlü girdisiyle aynı kodlama değildir. Ölçekleme/tarih ayrıntıları makale Ek A'da.

## 2. Dario — sekiz gerçek girdi

[Depo](https://github.com/dario-disanto/quarterly-eps-forecast-study) · [Girdi üretimi](https://github.com/dario-disanto/quarterly-eps-forecast-study/blob/main/src/epsforecast/features.py).

**Son hedef:** `epsfxq`, olağanüstü kalemler hariç seyreltilmiş çeyreklik EPS.

| Model girdisi | Formülü / anlamı |
|---|---|
| `epsfxq_lag1` | Önceki çeyreğin EPS'si; kısa vadeli süreklilik. |
| `epsfxq_lag4` | Geçen yıl aynı çeyreğin EPS'si; mevsimsellik. |
| `cfo_lag1` | Bir çeyrek gecikmeli `oancfq/atq`; işletme nakit akışı/aktif. |
| `accruals_lag1` | Bir çeyrek gecikmeli `ibq/atq - oancfq/atq`; nakit dışı kârlılık bileşeni. |
| `gross_margin_lag1` | Bir çeyrek gecikmeli `(saleq-cogsq)/saleq`; brüt marj. |
| `asset_turnover_lag1` | Bir çeyrek gecikmeli `saleq/atq`; aktif devir hızı. |
| `sales_growth_lag1` | Önceki çeyrekte ölçülen `saleq/saleq_lag4-1`; yıllık satış büyümesi. |
| `lev_lag1` | Bir çeyrek gecikmeli `(ltq-lctq)/atq`; uzun vadeli yükümlülük/aktif. **Yalnızca faizli borç oranı değildir.** |

Ham kalemler: `ibq` olağanüstü kalem öncesi kâr, `oancfq` CFO, `atq` aktif, `lctq` kısa yükümlülük, `ltq` toplam yükümlülük, `saleq` satış, `cogsq` satış maliyeti. `gvkey`, `datadate`, `fyearq`, `fqtr` şirket/mali dönem eşleştirmesi içindir. `sic` örneklemi tanımlamak için kullanılmış; modele girmez.

## 3. Minsu — V2 tablo girdisi 88 sütun

[Depo](https://github.com/minsu0011/eps-forecasting) · [Kesin giriş fonksiyonu](https://github.com/minsu0011/eps-forecasting/blob/main/research/eps_model_lab_v2/model_common.py) · [Sıra modeli girdisi](https://github.com/minsu0011/eps-forecasting/blob/main/research/eps_model_lab_v2/sequence.py).

**Son hedefler:** `h1`–`h4` gelecek dört native mali çeyreğin EPS'si; `ttm` ise dördüncü çeyrek ilerideki native TTM hedefi. Aynı hedef değiller.

| Girdi ailesi | Sütun sayısı | Anlamı |
|---|---:|---|
| `eps_lag_0` … `eps_lag_31` | 32 | En güncel bilinen EPS ve 31 eski mali çeyrek. Ölçeklenir. |
| `ttm_lag_0` … `ttm_lag_7` | 8 | Güncel ve yedi eski TTM EPS gözlemi. Ölçeklenir. |
| Yukarıdaki değerlerin `isfinite` maskeleri | 40 | Her gecikmenin gerçekten mevcut olması; eksik değeri sayısal sıfırdan ayırır. |
| `eps_growth` | 1 | EPS büyüme/değişim ölçüsü; ayrıca örnek ölçeğine bölünür. |
| `eps_acceleration` | 1 | EPS değişiminin hızlanma/yavaşlama ölçüsü. |
| `eps_volatility` | 1 | EPS geçmişindeki değişkenlik. |
| `eps_negative` | 1 | Zarar işareti. |
| `fiscal_sin`, `fiscal_cos` | 2 | Mali çeyreğin döngüsel mevsim kodları. |
| `history_observed` | 1 | Geçmişte gözlenmiş veri miktarı. |
| `eps_staleness_quarters` | 1 | En yakın mevcut EPS'nin kaç mali çeyrek eskidiği. |

Tablo modelindeki toplam: **40 değer + 40 maske + 3 türev + 5 sabit = 88**. `scale`, değerleri karşılaştırılabilir hale getiren bölen; bu fonksiyonda ayrıca bir ham özellik olarak eklenmiyor.

Sıra modelleri EPS ve TTM kanallarını, mevcutluk/eskilik ve mali çeyrek bilgilerini kendi veri yapısıyla işliyor; “her model aynı 88 girdiyi kullanıyor” denemez. V1'de araştırılan çok daha geniş model/finansal kanal listesi, V2'nin etkin girdi listesi değildir. V2 muhasebe kanalı Track A veri doğrulama yetersizliği nedeniyle bloke edilmiş. Fiyat, F/K ve kaynak kimlikleri çıktıda/entegrasyonda bulunabilir; `native_features` girdisinde yok.

## 4. Financial Forecasting FP&A ML Comparison

[Depo ve notebook](https://github.com/alpdemiroz1994/financial-forecasting-fpa-ml-comparison).

**Son hedef:** ayrı modellerde `OperatingIncome` faaliyet kârı ve `OperatingCashFlow_quarterly` tek çeyreklik CFO.

| Girdi | Anlamı / hangi model |
|---|---|
| `OperatingIncome_lag1` | Önceki çeyrek faaliyet kârı; iki modelde de. |
| `OperatingIncome_lag4` | Geçen yıl aynı çeyrek faaliyet kârı; faaliyet kârı modelinde. |
| `OperatingCashFlow_quarterly_lag1` | Önceki tek çeyrek CFO; CFO modelinde. |
| `Revenue_lag1`, `Assets_lag1` | Önceki çeyrek ciro ve aktif büyüklüğü; iki modelde. |
| `inflation_rate_lag1` | Bir çeyrek gecikmeli CPI yıllık artışı. |
| `gdp_growth_lag1` | Bir çeyrek gecikmeli GDP yıllık artışı. |
| `unemployment_rate_lag1` | Bir çeyrek gecikmeli işsizlik oranı. |
| `fed_funds_rate_lag1` | Bir çeyrek gecikmeli ABD politika/faiz serisi. |
| `Q_2`, `Q_3`, `Q_4` | Çeyrek göstergeleri; ilk çeyrek referans. |
| `sector_Technology` | Teknoloji sektörünü imalat grubundan ayıran gösterge. |

Her modelin final listesi 12 girdiden oluşur. Dört çeyreklik hareketli ortalama ayrıca karşılaştırma tahmini; onu kendiliğinden final RF/XGBoost girdisi saymıyoruz. Ciro/aktifler kaynak tablo kalemleri, diğer birçok indirilen XBRL etiketi final listede yok.

## 5. DeepEarnings

[Depo](https://github.com/alexanderpei/DeepEarnings) · [236 tanımlanmış finansal adayın tamamı](EK_DEEPEARNINGS.md).

**Son hedef:** `Reported > Estimate`, yani açıklanan EPS'nin analist beklentisinden yüksek olup olmadığı. Tutar regresyonu değil. Üç deney kolu ayrı:

- **Finansal kol:** `list_my_quarterly_features.txt` içinde 199, `list_my_quarterly_features_nonorm.txt` içinde 37 aday. İlk grup dönem piyasa değeri `mkvaltq` ile bölünüyor. Kod daha sonra tümü eksik sütunları düşürdüğü için **236 = tanımlanmış aday sayısı**, nihai eğitilmiş kolon sayısı değil. Nihai sütun listesi kullanılan veriyle birlikte değişiyor.
- **Piyasa kolu:** açıklama öncesi 30 gözlem boyunca açılış, yüksek, düşük, kapanış ve hacim (OHLCV). Bu kol finansal kolun girdilerine otomatik eklenmiş değil.
- **Metin kolu:** 10-Q/10-K metninden aşağıdaki sayımlar; karakter sayısına bölme sonrası `CharCnt` sütunu çıkarılıyor, böylece 10 alan kalıyor.

| Metin alanı | Anlamı |
|---|---|
| `CharCnt` | Karakter sayısı; ölçekleme paydası, son metin matrisinde çıkarılır. |
| `ComplexWordCnt` | Karmaşık sözcük sayısı. |
| `lmDictCnt` | Loughran–McDonald finans sözlüğü eşleşme sayısı. |
| `lmNegCnt`, `lmPosCnt` | Finans sözlüğündeki olumsuz ve olumlu sözcük sayımları. |
| `lmStrongCnt`, `lmModCnt`, `lmWeakCnt` | Güçlü, orta ve zayıf modal ifadeler. |
| `lmUncerCnt` | Belirsizlik sözcükleri. |
| `lmLitigCnt` | Hukuki/dava çağrışımlı sözcükler. |
| `harvNegCnt` | Harvard sözlüğüne göre olumsuz sözcükler. |

**Kod uyarısı:** standardizasyon ve KNN imputasyon train/test ayrımından önce; bu test bilgisi sızdırabilir. `shuffle=False` tek başına doğru zaman bölmesi yapmaz: veriyi hazırlayan kod şirketleri ardışık bloklar halinde yazar. Kaynaklar: `trn_PrepDataCompustat.py`, `trn_NetCompustat.py`, `trn_PrepDataSentiment.py`.

## 6. EPSBench — şirket özelinde ara hedefler

[Depo](https://github.com/chuyuxu/EPSBench) · [Bütün 149 şemanın sürücüleri](EK_EPSBENCH_SURUCULERI.md).

**Son hedef:** GAAP diluted EPS. **Asıl girdiler:** bilgi kesim tarihinden önceki raporlar, önceki sonuç toplantısı, haberler ve geçmiş muhasebe dayanak değerleri. **LLM'nin tahmin ettiği ara hedefler:** şirketin gelir ve gider sürücüleri. Bunlar tabular modele önceden bilinen sayılar olarak verilen sabit özellikler değildir.

| Sürücü türü | Anlamı |
|---|---|
| `*_yoy` | Geçen yıl aynı döneme göre ilgili kalemin büyümesi. |
| `*_margin_delta_bps` / `type=bps` | İlgili maliyetin belirlenmiş gelir paydasına oranında baz puan değişimi. |
| `*_abs` / `type=absolute` | Hedef dönemin doğrudan tutarı veya hisse sayısı. |
| `tax_rate`, `type=rate_override` | Hedef efektif vergi oranını doğrudan belirleme; her şirkette kullanılmaz. Baz puan değişimi değildir. |
| `tax_amount`, `income_taxes_abs` | Vergi tutarı; özellikle zarar/sıfıra yakın vergi öncesi kârda oran yerine. |
| `shares_abs` | Seyreltilmiş ağırlıklı ortalama hisse sayısı. |

Örnek MSFT şeması: ürün geliri, hizmet/diğer gelir büyümeleri; COGS marj değişimi; Ar-Ge; satış/pazarlama; genel/idari giderler; diğer net gider; vergi; seyreltilmiş hisse sayısı. Farklı dönem şemalarında isimler de değişebiliyor. Banka veya sigorta şeması bundan farklı. `formulas` alanı ara tahminlerden faaliyet kârı → vergi öncesi kâr → net kâr → EPS hesaplar. `target_fq_eps` gibi `_validation` alanları değerlendirme gerçeğidir, kullanılabilir gelecek girdisi sayılmaz.

## 7. Streetbench — sabit sayısal girdi listesi yok

[Depo](https://github.com/fundamental-research-labs/streetbench).

**Son hedef:** belirlenen çeyreğin normalize seyreltilmiş EPS'si. **Asıl girdiler:** önceki finansal geçmiş, yönetim yönlendirmesi, raporlar, şirket/sektör araştırması ve tarih kesimi uygulanmış web kanıtları. `case_id`, şirket, mali dönem ve kesim zamanı görevi tanımlar; finansal faktör değildir.

Raporlarda ele alınan ekonomik kalemler gelir, maliyet/gider, vergi ve hisse sayısıdır; ajan bunları her olayda farklı kanıtlarla değerlendirebilir. Bu nedenle bütün ajanlara ortak “17 girdi kolonu” gibi bir liste yok. Açıklanan hedef EPS ve final konsensüs puanlama için; forecasting task'a doğrudan verilmiş girdiler olarak sayılmadı. Sonuçlar geriye dönük benchmark'tır.

## 8. ForecastGPT — nitel rapor üretimi

[Depo](https://github.com/abhay-yemekar/forecastgpt-financial-outlook-agent) · [Çıkarım kodu](https://github.com/abhay-yemekar/forecastgpt-financial-outlook-agent/blob/main/app/tools/financial_extractor.py).

**Son çıktı:** gelecek çeyreğe ilişkin nitel görünüm ve gerekçeler. **Belge girdileri:** son finansal sonuç PDF'leri ve sonuç toplantıları; RAG ile yönetim yönlendirmesi, risk ve fırsatlar. Düzenli denetimli sayısal tahmin modeli yok.

| Çıkarılan alan | Anlamı |
|---|---|
| `total_revenue_inr_cr` | Toplam gelir; INR crore. |
| `net_profit_inr_cr` | Net kâr. |
| `operating_profit_inr_cr` | Faaliyet kârı. |
| `ebitda_inr_cr` | EBITDA/FAVÖK. |
| `operating_margin_pct`, `ebitda_margin_pct`, `net_margin_pct` | Faaliyet, EBITDA ve net kâr marjları. |
| `net_interest_income_inr_cr`, `net_interest_margin_pct` | Bankalar için net faiz geliri ve net faiz marjı. |
| QoQ/YoY değişimleri | Mevcut/geçmiş çıkarılmış rakamların değişimleri. |
| `price_inr` | En güncel piyasa fiyatı; yardımcı bağlam, kanıtlanmış EPS regresyon özelliği değil. |

Şirket kimliği/rapor dönemi metrikleri doğru belgeye bağlamak için kullanılır. Crore = 10 milyon. Girdi eksikse modelin rakam uydurması yerine eksikliği raporlama tasarımı bulunur.

## 9. JamesEzeilo — EPS Forecasting ML SGD

[Depo](https://github.com/JamesEzeilo/eps-forecasting-ml-sgd). Aşağıdaki liste README'deki X seçimine dayanır; dış Excel dosyası arşivde yok.

**Son hedef:** `Earns Per Share` mevcut EPS.

| Girdi | Anlamı |
|---|---|
| `1 Year Growth Total Sales` | Yıllık toplam satış büyümesi. |
| `Gross Income Margin` | Brüt kâr marjı. |
| `3y Price Volatility` | Üç yıllık fiyat oynaklığı. |
| `EBITDA Oper Income` | EBITDA niteliğindeki faaliyet sonucu; dış veri sağlayıcı tanımı gerekli. |
| `Total L T & S T Debt` | Uzun ve kısa vadeli toplam borç. |
| `Total Inven` | Toplam stok. |
| `Net Account Receiv` | Net alacaklar. |
| `Capital Expend CF` | Nakit akış tablosundaki yatırım harcaması. |
| `Selling General & Admin Expense` | Satış/genel/idari gider. |
| `Earns Per Share 1y back`, `2y back`, `5y back` | Bir, iki ve beş yıl önceki EPS. |

Toplam 12 tahmin girdisi. Rastgele şirket bölmesi, mevcut döneme ait diğer finansal tutarlarla bilinmeyen EPS'yi kestirme ve gelecek raporu tahmin etme arasındaki farkı çözmez.

## 10. Corporate Earnings Prediction

[Depo](https://github.com/kryptologyst/Corporate-Earnings-Prediction) · [Varsayılan girdi seçimi](https://github.com/kryptologyst/Corporate-Earnings-Prediction/blob/main/configs/default.yaml) · [Üretim kodu](https://github.com/kryptologyst/Corporate-Earnings-Prediction/blob/main/src/features/engineering.py).

**Son hedef:** `target_eps`. **Veri:** sentetik demo. Varsayılan listede 15 aday girdi:

| Grup | Değişkenler ve anlamları |
|---|---|
| Finansal, 7 | `revenue_growth` satış büyümesi; `profit_margin` net marj; `debt_to_equity` borç/özkaynak; `current_ratio` cari oran; `roe` özkaynak kârlılığı; `pe_ratio` F/K; `pb_ratio` PD/DD. |
| Teknik, 4 | `price_momentum_3m`, `price_momentum_12m` fiyat momentumu; `volatility_3m` oynaklık; `volume_trend` hacim sapması. |
| Makro, 4 | `gdp_growth`, `inflation_rate`, `interest_rate`, `market_sentiment`: büyüme, enflasyon, faiz, piyasa duyarlılığı. |

Kod ayrıca `price_momentum_6m`, `price_volume_ratio` fiyat/hacim, `asset_turnover` ciro/aktif, `equity_multiplier` aktif/özkaynak, `gross_margin`, `revenue_growth_rate`, `eps_growth_rate`, `real_interest_rate`, `yield_curve_slope`, `credit_spread` üretir; bunlar **varsayılan final listeyle aynı şey değil**. Bazıları rastgele simüle edilir. `volatility_3m` adı altında son 20 gözlem kullanılıyor; momentum pencereleri günlük seride gerçekten ay saymıyor. Tüm serinin sonundan referans almak geçmiş satırlarda ileri bilgi kullanabilir. Alan ismine bakarak ekonomik ölçüm doğruluğu varsayılmamalı.

## 11. Earnings Surprise Prediction Platform

[Depo](https://github.com/AnanmayS/Earnings-Surprise-Prediction-Platform) · [Kesin liste](https://github.com/AnanmayS/Earnings-Surprise-Prediction-Platform/blob/main/backend/ml/config.py).

**Son hedef:** `beat_miss`. 16 sayısal ve 1 kategorik girdi:

| Girdi | Anlamı |
|---|---|
| `return_5d_pre_earnings`, `return_20d_pre_earnings`, `return_60d_pre_earnings` | Açıklama öncesi 5/20/60 gün getiri. |
| `volatility_20d_pre_earnings` | Açıklama öncesi 20 günlük oynaklık. |
| `volume_change_20d_pre_earnings` | Açıklama öncesi 20 günlük hacim değişimi. |
| `news_sentiment_pre_earnings` | Açıklama öncesi haber duyarlılığı. |
| `revenue_growth_last_reported`, `eps_growth_last_reported` | Son açıklanan satış/EPS büyümesi. |
| `analyst_revision_trend` | Analist tahminlerindeki revizyon yönü. |
| `pe_ratio`, `debt_to_equity`, `profit_margin` | F/K, borç/özkaynak, net marj. |
| `prior_eps_surprise` | Önceki açıklamanın EPS sürprizi. |
| `eps_surprise_mean_4q` | Önceki dört çeyreğin ortalama sürprizi. |
| `trailing_beat_rate_4q` | Önceki dört çeyrekte beklenti aşma sıklığı. |
| `days_since_last_earnings` | Son açıklamadan itibaren geçen gün. |
| `sector` | Sektör kategorisi. |

Tarihsel eğitim verisi kısmen sentetik; canlı eksik alanlar tahminî yedek değerlere dönebilir. Bunların gözlenmiş gerçek girdilerle aynı kabul edilmesi uygun değil.

## 12. Predicting PER

[Depo](https://github.com/my2582/predicting-per). Liste README'deki bağımlı/bağımsız değişkenlerden; ham WRDS/CRSP verileri gerektirir.

**Hedefler:** piyasa değeri `mkvaltq` ve olağanüstü kalem öncesi kâr `ibq`; çalışmanın amacı ileri F/K. **Girdiler:**

| Kod | Anlamı |
|---|---|
| `saleq` | Satış. |
| `cogsq` | Satış maliyeti; README'deki `Coqsq` yazımı için bu standart karşılık kullanıldı. |
| `xsgaq` | Satış/genel/idari gider. |
| `oiadpq` | Amortisman sonrası faaliyet kârı. |
| `cheq`, `rectq`, `invtq`, `acoq` | Nakit/kısa yatırım, alacak, stok, diğer dönen varlık. |
| `ppentq`, `aoq` | Net maddi duran varlık, diğer varlık. |
| `dlcq`, `apq`, `txpq` | Kısa vadeli borç, ticari borç, ödenecek vergi. |
| `ltq` | Toplam yükümlülük; README bunu “other current liabilities” diye etiketliyor. **Kaynak içinde tanım çelişkisi var.** |
| `Mom3m`, `Mom6m`, `Mom9m` | 3, 6, 9 aylık fiyat momentumu. |

Piyasa değeriyle ölçekleme ve dönüşümler kullanılıyor. Bu hedef setini doğrudan sonraki rapor net kâr modeliyle eşitlememeli.

## 13. Financial Health Forecasting PSX

[Depo](https://github.com/UmerMuzaffar/financial-health-forecasting-psx) · [Notebook](https://github.com/UmerMuzaffar/financial-health-forecasting-psx/blob/main/Financial_Health_Forecasting.ipynb).

**Son hedef:** ayrı ayrı 30 yıllık finansal oran. Çeyreklik EPS değil.

| Oran grubu | Hedef/girdi geçmişi olarak kullanılan oranlar ve anlamları |
|---|---|
| Kârlılık, 8 | Gross Profit Ratio brüt marj; Operating Profit Ratio faaliyet marjı; EBT/Sales vergi öncesi marj; EAT/Sales vergi sonrası marj; Net Profit Ratio net marj; ROE, ROA; ROCE kullanılan sermaye kârlılığı. |
| Likidite, 3 | Current Ratio dönen varlık/kısa yükümlülük; Acid Test Ratio stok hariç likidite; Cash Ratio nakit oranı. |
| Kaldıraç, 4 | Debt to Equity, Debt to Total Assets, Debt to Capital: borcun özkaynak/aktif/toplam sermayeye oranları; Interest Coverage faiz karşılama. |
| Etkinlik, 8 | Inventory, Payable, Receivable, Asset ve Fixed Asset Turnover: stok/borç/alacak/aktif/duran varlık devirleri; Avg Collection Period tahsilat günü; Avg Payment Days ödeme günü; Operating Cycle faaliyet döngüsü. |
| Çalışma sermayesi, 1 | Cash Conversion Cycle nakit dönüşüm süresi. |
| Piyasa/diğer, 6 | P/E F/K; Price to Book PD/DD; Price to Sales fiyat/satış; Book Value per Share hisse başına defter değeri; Sales per Share hisse başına satış; Days Inventory Outstanding stok tutma günü. |

**113 adayın üretim kuralı:** 30 oranın bir ve iki yıllık gecikmesi = 60; üç yıllık hareketli ortalama = 30; brüt/net marj, ROE, cari oran, borç/özkaynak, faiz karşılama değişimleri = 6; aşağıdaki 10 finansal özellik; dört makro; iki etkileşim; yıl = 113.

10 finansal özellik: `yoy_sales`, `yoy_profit`, `yoy_assets`, `yoy_equity`, `yoy_cogs`, `yoy_cfo` yıllık değişimler; `n_debt_ratio` borç/aktif; `n_cfo_margin` CFO/satış; `n_capex_ratio` yatırım harcaması/aktif; `n_profit_mgn` net kâr/satış.

Makro: `pkr_usd` Pakistan rupisi/dolar; `inflation` enflasyon; `policy_rate` politika faizi; `oil_brent` Brent. Etkileşim: `risk_debt_coverage` borç/özkaynak oranının faiz karşılamaya bölümü; `momentum_profit` brüt marj değişimi × gecikmiş brüt marj. `year` yıl.

**Etkin son 60 sütun**, eksiklik filtresi ve eğitim verisinde `SelectKBest` sonucuyla seçiliyor. Sabit bir 60 isim listesi kodda yazılı değil; yayımlanmayan nihai listeyi uydurmadık. **Önemli kod bulgusu:** trendler ve `roll3` aynı yılın değerini de içeriyor; `n_profit_mgn` mevcut yıl net marj hedefiyle aynı bilgiyi taşıyabilir. Bunlar bir çeyrek/yıl henüz açıklanmamışken bilinmez. Zaman bölmesi bu hedef sızıntısını tek başına düzeltmez.

## 14. Earnings Engine

[Depo](https://github.com/chandewardnyanesh/earnings-engine) · `earnings_engine/features/price_features.py`, `earnings_features.py`, `dataset.py`.

**Son hedef:** açıklama tarihinin etrafında `close(T+1)/close(T-1)-1` getirisinin işareti. **16 gerçek girdi:**

| Girdi | Anlamı |
|---|---|
| `ret_5d`, `ret_21d`, `ret_63d` | Önceki 5/21/63 işlem gününün getirileri. |
| `vol_21d` | Son 21 günlük getirilerin standart sapması. |
| `vol_ratio_5d_63d` | Kısa/uzun pencere oynaklık oranı. |
| `volume_ratio_5d_63d` | 5 ve 63 günlük ortalama hacimlerin oranı. |
| `abs_ret_mean_21d` | 21 günlük mutlak getirilerin ortalaması; günlük hareketlilik. |
| `dist_52w_high`, `dist_52w_low` | Fiyatın en fazla 252 gözlemdeki tepe/dibe göre konumu. |
| `n_past_events` | Şirketin önceki açıklama sayısı. |
| `past_reaction_mean`, `past_reaction_std` | Geçmiş açıklama tepkilerinin ortalaması ve standart sapması. |
| `past_up_rate` | Geçmiş açıklamalarda yükseliş oranı. |
| `last_reaction_return` | Önceki açıklamanın fiyat tepkisi. |
| `last_surprise_pct` | Önceki açıklamanın EPS sürprizi yüzdesi. |
| `is_in_market` | Hindistan piyasası ise 1; diğerinde 0. Piyasa getirisi değildir. |

Son hedef bilanço tutarı olmadığı için ilk üç dışında. Yol haritasındaki opsiyon ve analist revizyonu özellikleri mevcut 16 girdiye dahil edilmedi.

## 15. Moozzart — US Firm EPS Prediction

[Depo](https://github.com/Moozzart/Beating-Analysts-Predictions-Using-Machine-Learning-Algorithms-to-predict-EPS-of-US-Firms) · `VariableCreation_and_Model.py` ve README.

README üç deneyden bahsediyor: EPS geçmişi; makro+EPS; finansal kalem+EPS. Belirtilen EPS özellikleri son çeyrek, geçen yıl aynı çeyrek, yıllık EPS değişimi ve `EPS_(t-1)-ortalama(EPS_(t-2),EPS_(t-3),EPS_(t-4))` şokudur.

Kodda dönüşüm uygulanan ana kalemler: `ceqq` özkaynak; `prccq` kapanış fiyatı; `req` birikmiş kâr; `xoprq` faaliyet gideri; `dp` amortisman; `ppe` maddi duran varlık; `txt` vergi; `csh` nakit; `cogs` satış maliyeti; `sales` satış; `at` aktif; `ni` net kâr; `ib` olağanüstü kalem öncesi kâr. `qoq_*` ve `yoy_*` önceki çeyrek/yıl değerlerini; `del_*` ve `diff_*` türevlerini oluşturmak için kullanılıyor. `ACTUAL` gerçekleşen EPS; `Volatility` oynaklık.

Analist alanları `NUMEST` tahmin sayısı, `MEDEST` medyan, `MEANEST` ortalama, `HIGHEST` en yüksek, `LOWEST` en düşük tahmin. Bazı çağrılarda düşürülüyor; akışta farklı X/X1 tanımları ve notebook'tan taşınmış hücre sırası sorunları var. Final bütün-model girdi listesi tek bir sabit sözleşmede tutulmuyor. Ayrıca bazı fiyat/oynaklık alanları `shift(-1)` ile ileri taşınıyor; her sürüm için bilgi zamanının yeniden denetlenmesi gerekir.

**Sınır:** FRED makrolarının tam isimleri incelenen README/ana kodda sabit bir liste olarak doğrulanamadı. Bu nedenle “CPI/GDP kesin kullanılmıştır” gibi bir liste eklenmedi. Bu projeye ait belge, doğrulanabilen değişken aileleri ve açık belirsizlik kaydıdır.

## 16. DhirainVij — Earnings Prediction

[Depo](https://github.com/DhirainVij/earnings-prediction) · `prediction.ipynb`, `earnings_prediction.ipynb`.

Dosyadan okunan alanlar: Revenue ciro; Cost of Revenue satış maliyeti; Gross Profit brüt kâr; Depreciation/Amortization amortisman; Total Operating Expense toplam faaliyet gideri; Operating Income faaliyet kârı; Net Income net kâr; Normalized EBITDA düzeltilmiş FAVÖK; GDP growth rate büyüme oranı.

**Ancak incelenen model yolunda:** `df['Net Income']` tek sütun olarak seçiliyor, MinMax ölçeklemesi yapılıyor ve varsayılan dört gözlem uzunluğunda pencereler LSTM/GRU/CNN-LSTM/RNN'ye veriliyor. Yani gerçek model girdisi **son dört net kâr gözlemi**, son hedef bir sonraki net kâr. Diğer sekiz alanın okunması modelde kullanıldıkları anlamına gelmiyor. README'deki ciro tahmini iddiası için aynı şekilde açık bir bağımsız ciro giriş/çıkış yolu bu incelemede doğrulanmadı.

## Bu sözlükten uygulanabilir sonuç

En sık tekrar eden çekirdek geçmiş EPS/kâr ve mevsimsellik. Ondan sonra nakit akışı, tahakkuk, marj, vergi ve sermaye yapısı geliyor. Sıklık bir başarı kanıtı değildir: değişkenin işe yarayıp yaramadığı aynı zaman dışı testte bloklar çıkarılarak ölçülmeli.

Her gözlem için şirket kimliği, mali dönem, ilk yayın zamanı, birim/para birimi, konsolide kapsam ve revizyon sürümünü de saklamak gerekir. Bunlar her zaman tahmin özelliği değildir; tahminin doğru ve karşılaştırılabilir olmasını sağlayan veri sözleşmesidir.
