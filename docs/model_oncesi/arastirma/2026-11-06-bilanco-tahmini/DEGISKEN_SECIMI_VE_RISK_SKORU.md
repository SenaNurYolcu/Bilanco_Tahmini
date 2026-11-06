# Değişken seçimi ve şirkete özgü risk özellikleri

Güncellenebilir uygulama adayları [yaşayan değişken listesinde](../../DEGISKEN_LISTESI.md) ve [JSON kaydında](../../degiskenler.json) tutulur. Bu belge model geliştirme/eğitim tarafındaki araştırma gerekçelerini korur.

İnceleme tarihi: **6 Kasım 2026**. Bu belge, dört kişilik bir ekibin BIST'te açıklanmamış çeyreğe ilişkin ana finansal kalemleri tahmin etmesi için bir **deney taslağıdır**. Aşağıdaki liste kanıtlanmış bir “en iyi değişken kümesi” değildir. Makalelerin bulguları, hazır risk ölçüleri ve bizim test önerilerimiz ayrılmıştır.

## 1. Ana öneri

Önce geçmiş muhasebe kalemleriyle güçlü bir temel tahmin kurun. Türkiye makrosunu, küresel risk göstergelerini ve şirketin bunlara maruziyetini ayrı deney blokları olarak ekleyin. Tek bir belirsiz dünya riski puanının bütün bilgiyi taşımasını beklemeyin.

Önerilen araştırma sorusu: **Küresel ve yerel ekonomik değişkenlerin, şirketin önceden açıklanmış finansal/coğrafi özellikleriyle birlikte kullanılması, sonraki finansal sonuçların tahminini iyileştiriyor mu?**

Satış, stok veya borcun geçmiş değeri **girdi**, açıklanmamış hedef dönemdeki değeri **çıktıdır**. Gelecekte gerçekleşmiş bir risk endeksi ise tahmin anında bilinmiyorsa girdi olamaz. Muhasebe tutarlılığı ayrıca değerlendirilir; bir finansal tablonun eşitliklere uyması doğru tahmin edildiğini göstermez.

## 2. Makaleler neyi destekliyor?

| Kaynak | İncelenen bulgu | Bizim çalışmamız için sınır |
|---|---|---|
| [Cao ve You, 2021 açık taslak; çalışma 2024'te yayımlandı](https://business.columbia.edu/sites/default/files-efs/imce-uploads/CEASA/Cao%20and%20You%2020210120.pdf) | §5.3'te geçmiş kâr, faaliyet nakit akışı, vergi giderinin seviyesi/değişimi öne çıkıyor; özkaynak, aktif ve alacak değişimleri de kullanışlı. | Yıllık kâr tahmini ve taslak sürümün bulguları; BIST'te çeyreklik tüm kalemlerde aynı önem sırası kanıtlanmış değil. |
| [Koval, Andrews, Yan, EMNLP 2024](https://aclanthology.org/2024.findings-emnlp.486/) | Tablo 2'de finansal geçmişe toplantı ve rapor metinleri eklenince MSE 1,60'tan 1,44'e; sonradan makro eklenince 1,42'ye iniyor. Makro son adımda yaklaşık %1,4 ek düşüş sağlıyor. | Hedef analist beklentisine göre kâr sürprizi; net kâr tutarı veya tam rapor değil. Son makro adımının anlamlılığına ilişkin ayrı bir yıldız yok; her ilaveyi kesin kazanç sayamayız. |
| [Scherrmann ve Elsas, 2023](https://arxiv.org/abs/2311.10756) | Muhasebe geçmişiyle piyasa özetlerini birleştiriyor; daha karmaşık ikinci piyasa RNN'si basit piyasa özetlerini geçmiyor. | Daha karmaşık veya daha çok özellik otomatik üstünlük sağlamıyor. EPS bulguları diğer hedefler için ayrıca sınanmalı. |
| [Forma, 2026](https://arxiv.org/abs/2608.11327) | Geçmiş finansallar ve sektörle çok kalemli tahmin; bir çeyrek ufkunda RF'nin R²'si 0,398, Forma'nın 0,390. | Küçük BIST panelinde Transformer'la başlama zorunluluğu yok. Bu, RF'nin bizim verimizde kesin en iyi olacağı anlamına da gelmiyor. |
| [Caldara ve Iacoviello, AER 2022](https://www.matteoiacoviello.com/gpr_files/GPR_PAPER.pdf) | Haber tabanlı jeopolitik risk; sektör/şirket maruziyetiyle yatırım ilişkilerini inceliyor. | Gelecek EPS veya bütün finansal tabloların tahmininin iyileştiğini kanıtlamıyor; risk özellikleri için ekonomik gerekçe sağlıyor. |
| [Exploring corporate geopolitical risk exposure — a heterogeneous geographic segment perspective, 2026](https://doi.org/10.1016/j.jaccpubpol.2026.107407) | Yayınevi özeti/girişinde ülke riskini şirketin coğrafi satışlarıyla ağırlıklandıran ölçü ve şirket performansıyla ilişkisi anlatılıyor. | Tam metin incelenmedi; bu taramada yayınevi özeti ve girişine erişildi. Coğrafi satış ağırlıklı risk fikri zaten mevcut; yeni yöntem diye sunulamaz. |

Önemli ayrım: Bir özelliğin bir modelde yüksek önem puanı alması, eklenmesinin test hatasını mutlaka azalttığını veya nedensel etkisini göstermez. Asıl karar, aynı ileri dönemlerde yapılan blok ekleme/çıkarma deneyinden gelir.

## 3. İlk finansal girdi listesi

Son açıklanmış finansallardan başlayın. Aşağıdaki ana kalemlerin bir kısmı hedef listesiyle aynı olabilir; kullanılan değerler geçmişe ait olmalıdır.

| Grup | Başlangıç girdileri | Açıklama |
|---|---|---|
| Kâr ve satış | Hasılat, satışların maliyeti, brüt kâr, esas faaliyet kârı, dönem net kârı | Kârın bileşenleri ve devamlılığı. Konsolide dönem kârı/ana ortaklık kârı ayrımı sabitlenir. |
| Vergi ve finansman | Vergi gideri/geliri, finansman gideri; varsa tutarlı ayrıştırılmış faiz gideri | Faaliyet dışı bileşenleri ayırmak için. Vergi ve finansman kalemlerinin işaretleri belgelenir. |
| Nakit | İşletme nakit akışı, yatırım harcaması veya tutarlı yatırım nakit akışı; nakit bakiyesi | Kârın nakitle desteklenmesi ve yatırım ihtiyacı. Yatırım harcaması ile toplam yatırım nakit akışı aynı kavram değildir. |
| İşletme sermayesi | Ticari alacak, stok, ticari borç | Satışın tahsilata, stok ve ödemelere dönüşümü. |
| Finansal yapı | Toplam varlık, toplam yükümlülük, özkaynak, kısa/uzun vadeli finansal borç | Şirket ölçeği, kaldıraç ve finansman ihtiyacı. Toplam yükümlülük ile finansal borç ayrılır. |
| Takvim/veri durumu | Mali çeyrek, sektör, gözlem eksikliği, son açıklamanın yaşı | Mevsimsellik ve eski/eksik bilgi. Şirket başına tek başına model kurmak yerine şirketler birlikte öğrenilebilir. |

Her kalemin bütün olası dönüşümlerini ilk günden üretmeyin. Önce son bilinen seviye, hedef dönemin geçen yılki karşılığı ve az sayıda yıllık değişim kullanın. Yeterli veri varsa son 8–12 çeyreğin ek katkısı ayrı sınanır. Dönem boşluğu varsa bir önceki satır otomatik “önceki çeyrek” değildir.

Az sayıda anlamlı oran ekleyin: brüt/faaliyet marjı, işletme nakit akışı/aktif, finansal borç/aktif, alacak/satış ve stok/satış. Paydası sıfır veya çok küçük olan oranların politikası önceden yazılır. Negatif kârın logu alınmaz; dönüşümler ve uç değer sınırları yalnız eğitimden öğrenilir. Aynı tutarı farklı ölçeklerle tekrar tekrar eklemek veri miktarını artırmaz.

## 4. Türkiye makrosu ve sektör göstergeleri

İlk deney için küçük bir aday listesi:

- USD/TL ve EUR/TL değişimi; gerekirse kur oynaklığı.
- TÜFE ve Yİ-ÜFE değişimleri.
- Faiz seviyesi/değişimi; mümkünse şirket finansmanına daha yakın bir kredi faizi.
- Yayımlanmış sanayi üretimi veya seçilen sektörün talep göstergesi.
- İlgili sektörlerde Brent veya uygun girdi emtiasının değişimi.

Kaynak adayları [TCMB EVDS](https://evds3.tcmb.gov.tr/) ve [TÜİK veri portalı](https://data.tuik.gov.tr/). Seri tanımı, kapsamı, ilk yayımlanma saati ve revizyonları uygulanmadan önce tek tek doğrulanmalıdır. Bu listede sayılması, her serinin tarihsel gerçek zaman sürümünün hazır bulunduğu anlamına gelmez.

Faiz, kur ve fiyat endeksleri farklı mekanizmaları temsil eder. Hepsini önceden keyfî ağırlıklarla “Türkiye riski” başlığına sıkıştırmak yerine, model girdilerinde ayrı tutmak daha açıklayıcı bir başlangıçtır.

## 5. “Dünya riski” için hazır ölçüler

| Gösterge | Ölçtüğü | Zamanlama ve kullanım notu |
|---|---|---|
| [GPR — Geopolitical Risk](https://www.matteoiacoviello.com/gpr.htm) | Savaş, çatışma, terör ve jeopolitik gerilimlerle ilgili haber yoğunluğu | Aylık küresel/ülke serileri; küresel günlük seri de var. Aylık güncelleme ay başında, günlük veri güncellemesi haftalık. Eski sürüm arşivi ve revizyon notları mevcut. |
| [GEPU — Global Economic Policy Uncertainty](https://policyuncertainty.com/global_monthly.html) | Ekonomik politika belirsizliğiyle ilgili ülke haber endekslerinin küresel özeti | Aylık. İlgili ayın son günü yayımlanmış olduğu varsayılmaz. Seçilen sürüm ve ağırlıklandırma kaydedilir. |
| [OFR Financial Stress Index](https://www.financialresearch.gov/financial-stress-index/) | Küresel finansal piyasa stresi; kredi, finansman, değerleme, güvenli varlık ve oynaklık kanalları | Günlük, 33 piyasa değişkeni; yayımlanan veri iki iş günü geriden gelir. Revizyonlar var. |
| [WUI — World Uncertainty Index](https://worlduncertaintyindex.com/data/) | Ülke raporlarındaki genel belirsizlik | Çeyreklik ana serinin Q1 güncellemesi nisan sonu gibi gecikmeli; aylık veri seti de var. İlk sürümde diğerlerinin üstüne otomatik eklemek yerine alternatif olarak sınanabilir. |

Bu ölçüler aynı kavram değildir ve olasılık değildir. GPR yüksekliği, ekonomik politika belirsizliği ve piyasa stresi farklı yönlerde hareket edebilir. Birini “dünya %80 tehlikeli” diye yorumlamak doğru olmaz.

İlk denemede üç çekirdek ölçüyü **ayrı sütunlar** olarak kullanın: GPR, GEPU ve OFR FSI. Aynı finansal stres bilgisini tekrar taşıyan başka göstergeleri ancak ek değerleri varsa tutun.

## 6. İstenirse basit birleşik skor

Aşağıdaki formül bir **bizim kıyas önerimizdir**; yayımlanmış standart bir dünya risk skoru değildir:

```text
küresel_stres_özeti = [z(GPR) + z(GEPU) + z(OFR_FSI)] / 3
z(x) = (x - eğitim_ortalaması) / eğitim_standart_sapması
```

Önce her seri tahmin anında kullanılabilir, ortak bir geriye dönük pencereye özetlenir. Sonra ölçekler yalnız eğitim verisiyle eşitlenir. Model seçimi aşamasında GPR/GEPU gibi sağa çarpık serilerde `log1p` dönüşümü ayrıca sınanabilir; OFR negatif değer alabildiğinden aynı dönüşüm ona körlemesine uygulanmaz.

Ham endekslerin doğrudan ortalaması alınmaz; farklı ölçekler birini istemeden baskın yapabilir. Test dönemini de kullanarak normalizasyon, PCA veya ağırlık öğrenmek geleceğe bakıştır. Birleşik skorun daha iyi olması garanti değildir; ayrı girdilerle, eşit ağırlıklı skorla ve risk içermeyen modelle karşılaştırılmalıdır. Model zaten etkileşim öğrenebildiği için çarpım özelliklerinin katkısı da garanti değildir.

Arayüz için 0–100 gösterim gerekirse eğitim referansındaki yüzdelik sıra kullanılabilir. Bu gösterim, kârın düşme olasılığı olarak etiketlenmez. İlk sürüm için PCA, öğrenilmiş ağırlıklar ve LLM skoru aynı anda eklenmez.

## 7. Daha güçlü aday: şirkete özgü maruziyet

Ortak bir küresel değer, aynı tarihte bütün şirketlere aynıdır. Farklılık yaratabilecek girdiler, **önceden açıklanmış şirket özellikleriyle etkileşimlerdir**:

| Aday özellik | Yapı | Sınır |
|---|---|---|
| Coğrafi satış risk ölçüsü | Ülkeler üzerinden: son açıklanmış ülke satış payı × o ülkenin normalize edilmiş risk endeksi; sonra toplam | Ülke/bölge ayrımı tutarlı olmalı. Bölge verisinden bilinmeyen ülke payları uydurulmaz; kapsama oranı saklanır. Bu bir satış kanalı göstergesidir, bütün tedarik zinciri riski değildir. |
| Kur maruziyeti | Kur değişimi × önceki net döviz pozisyonu/aktif | Net döviz pozisyonunun işareti korunur; rapordaki türev/korunma kapsamı belgelenir. Gelecek dönem pozisyonu kullanılamaz. |
| İhracat kanalı | Kur veya dış talep değişimi × önceki ihracat/satış | İhracat payı tek başına net kur kazancını ölçmez; ithal maliyet ve korunma farklı olabilir. |
| Faiz maruziyeti | Faiz değişimi × önceki değişken faizli borç/aktif | Ayrıntı yoksa finansal borç/aktif yalnız kaba bir vekildir. Vade ve sabit/değişken faiz ayrımı kaybolur. |
| Girdi maliyeti | Emtia değişimi × önceki enerji/girdi maliyet payı; veri yoksa önceden tanımlanmış sektör etkileşimi | Şirketlere elle keyfî hassasiyet puanı atamak yerine ölçülebilir özellik tercih edilir. |

Coğrafi ölçünün araştırma formülü:

```text
şirket_coğrafi_risk(i, t) = Σ_c [satış_payı(i, c, t'den_önce_yayımlanan) × z_eğitim(GPR(c, t'de_bilinen))]
```

Ülke endekslerinin farklı bazları bulunduğundan karşılaştırılabilir ölçek seçimi ve alternatif normalizasyon duyarlılığı belgelenir. Yıllık açıklanan satış payı, yeni açıklama gelene kadar eski bilgi olarak kullanılır; geriye sonradan doldurulmaz. Eksik ülke riski sıfır risk demek değildir. Kapsanan satış payı azsa ölçü eksik bırakılır veya ayrı kısıtlı örneklem deneyi yapılır.

Bir şirketin ihracat, borç veya coğrafi yapısı riske açıklığını gösterir; etkinin kârı kesin olarak düşürdüğünü söylemez. Savunma, enerji üretimi ve enerji tüketimi gibi faaliyetlerde işaretler farklı olabilir. Etkiyi önceden bütün şirketler için negatif sabitlemeyin. [Fed'in sektör çalışması](https://www.federalreserve.gov/econres/notes/feds-notes/measuring-geopolitical-risk-exposure-across-industries-a-firm-centered-approach-20250829.html) bu heterojenliğe örnek verir; hedefi hisse tepkileridir, bizim finansal tahmin başarımız değildir.

## 8. Metin ve LLM hangi aşamada?

Önceki faaliyet raporlarından sipariş, kapasite, satış hacmi, enerji, finansman ve tedarik açıklamaları çıkarılabilir. Bu, tek bir olumlu/olumsuz duygu sayısından daha belirli ekonomik kanalları hedefleyen bir öneridir. Açıklanan geçmiş sayıları çıkarmak ile geleceğe ilişkin beklentiyi çıkarmak ayrı etiketlenmelidir.

İlk sürümde haberleri LLM'ye verip açıklamasız bir 0–100 risk puanı üretmek önerilmez. Sonradan denenirse:

- Sabit tarih penceresi, haber kaynakları ve tekrar haber temizliği.
- Önceden tanımlı risk türleri, kaynak metne bağlı kanıt cümleleri ve insan kontrolü.
- Model/prompt sürümü ve erişim anı kaydı.
- Mevcut GPR/GEPU/FSI üzerinde ek katkı ölçümü.
- Tarihsel haberleri daha yeni bir dil modeliyle okumada geçmiş sonuca dair model bilgisinin sızabileceğinin değerlendirilmesi; ileriye dönük yeni veriyle teyit.

Şirket metninden siyasi risk çıkarımı zaten [Hassan ve diğerlerinin firm-level risk çalışmaları](https://www.firmlevelrisk.com/home) ve başka araştırmalarda var. Salt LLM veya duygu puanı eklemek kendiliğinden özgün katkı oluşturmaz.

## 9. Zamanlama: en önemli veri sözleşmesi

Ana deneyin tahmin anı sabitlenir. Örneğin **30 Eylül kapanışında henüz açıklanmamış Q3 sonuçlarını tahmin etmek**, Q3 başlamadan tahmin yapmaktan farklıdır. İlkinde gerçekleşmiş ancak henüz raporlanmamış çeyreği kestiriyoruz; ikincisinde Q3 boyunca gerçekleşecek kur/risk değerlerini bilemeyiz.

Her kaynak gözleminde en az şu alanlar bulunmalı:

```text
series_or_item, company_or_country, observation_period,
first_published_at, available_at, vintage_or_version,
value, unit, source_url, retrieved_at
```

Bir özellik yalnız `available_at <= tahmin_anı` ise kullanılabilir. Son açıklanan seviye, mevcut gözlemlerin son 90 gündeki ortalaması veya değişimi gibi az sayıda özetle başlayın. Tam çeyrek verisi bulunmadığında varmış gibi üç aylık ortalama oluşturmayın; kapsama/eskilik alanı taşıyın. Büyük şokları saklayan ortalamaya karşı tepe değeri ayrı bir küçük deney olabilir.

Örnek: WUI'nin Q3 ana serisi ekim sonunda güncelleniyorsa 30 Eylül tahmininde Q3 WUI kullanılamaz. GPR'nin günlük gözleminin tarihi, haftalık yayımlanma tarihiyle aynı değildir. Güncel dosyayı indirmek eski sürümü çözmez. Risk endeksinin yöntemi veya kendisi sonradan oluşturulmuşsa, geçmiş dönem testi “o tarihte canlı kullanılabilirdi” diye sunulmaz; geriye dönük gösterge deneyi olarak etiketlenir ve mümkünse sonraki dönemlerde teyit edilir.

Finansal kalemlerde ayrıca konsolidasyon, TL/bin TL, çeyrek/kümülatif ve enflasyona göre düzeltmenin satın alma gücü tarihi korunur. Farklı enflasyon temellerindeki kümülatif tutarlar doğrudan çıkarılarak çeyreklik akış üretilmez.

## 10. İlk model ve deney sırası

İlk etapta güçlü basit kıyaslar, Ridge ve RF/tek boosting modeli yeterlidir. Ağaç ailesi seçimini eğitim/doğrulama döneminde sınırlı bütçeyle yapın; testte en iyi görüneni seçmeyin. Ayrı kalem modellerine aynı risk girdileri verilebilir; model her kalem için farklı ilişkiler öğrenir. Bu aşama yeni bir ağ mimarisi gerektirmez.

| Deney | Eklenen bilgi | Ölçülecek katkı |
|---|---|---|
| A | Geçmiş finansallar + takvim/sektör | Basit sezonluk kıyasın üstüne tahmin değeri |
| B | A + Türkiye makrosu | Yerel makronun katkısı |
| C | B + ayrı küresel risk göstergeleri | Küresel bilginin ek değeri |
| C-alternatif | B + birleşik stres özeti | Tek skor, ayrı bileşenleri geçiyor mu? |
| D | C + geçmiş şirket maruziyetleri | Şirket profili tek başına ne katıyor? |
| E | D + risk–maruziyet etkileşimleri / coğrafi ağırlıklı ölçü | Şirkete özgü risk özelliklerinin ek katkısı |
| F, sonraki aşama | E + doğrulanmış metin/faaliyet özellikleri | Temiz sayısal bilgilerin üstüne metnin ek değeri |

Karşılaştırmalar aynı şirket–çeyrek–hedef gözlemlerinde yapılır. Coğrafi veri yalnız bazı firmalarda varsa hem ortak örneklemde performans hem toplam kapsama raporlanır. İyileşme, daha kolay şirketlerin seçilmesinden kaynaklanmamalı.

Zamana göre eğitim/doğrulama/test; veri dönüşümleri ve skor ağırlıkları yalnız geçmişte öğrenilir. Kalem bazında MAE, ölçeklenmiş hata ve basit kıyasa göre fark ölçülür. SHAP, blok katkısı deneyinin yerine geçmez ve nedensellik göstermez. Test dönemi krizleri sonuç görülmeden tanımlanır; tek bir krizi iyi yakalamak genel başarı sayılmaz.

**Ortak risk serisi veri sayısını şirket sayısıyla çoğaltmaz:** 50 şirkette aynı 40 çeyreğin risk değerini kullanmak, 2.000 bağımsız makro gözlem yaratmaz. Bu nedenle tarih dışı test ve çeyrek bloklarını koruyan belirsizlik hesabı önemlidir.

## 11. İlk uygulanabilir karar

İlk veri pilotunda şu üç soruyu yanıtlayın: Finansal kalemlerin tarih/birimleri doğru mu? Üç risk serisinin o tarihte erişilebilir sürümü bulunabiliyor mu? Şirketlerin döviz/borç veya ülke satış paylarından en az biri tutarlı çıkarılabiliyor mu?

Pilot başarılıysa A–C karşılaştırmasını kurup, yalnız güvenilir maruziyetlerde D–E'ye geçin. Genel risk özetinin ve coğrafi ölçünün başarısını önceden varsaymayın. Araştırma katkısı, BIST'te hangi kalemlerde ve koşullarda ek bilgi sağladıklarını göstermektir.

Yerel ek: [Caldara–Iacoviello, Measuring Geopolitical Risk (2022)](makaleler/caldara-iacoviello-gpr-2022.pdf). İndirme ve SHA-256 kaydı [kaynak manifestosunda](kaynak-manifestosu.json). 2026 coğrafi satış çalışmasının tam PDF'si bu taramada arşivlenmedi.
