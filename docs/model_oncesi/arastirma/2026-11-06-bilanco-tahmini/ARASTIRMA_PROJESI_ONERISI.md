# Dört kişilik ekip için araştırma projesi önerisi

Tarih: **6 Kasım 2026**. Durum: **tartışma taslağı; uygulanmış model veya kanıtlanmış yenilik değil**. Süre, deneyim ve veri bütçesi henüz bilinmediğinden bir akademik dönem, temel Python/ML bilgisi ve sınırlı hesaplama bütçesi varsayılmıştır. BIST odağı bir öneridir.

## 1. Önerilen araştırma sorusu

**Şirketin geçmiş finansal tablolarına, tahmin tarihinde bilinen makro verileri ve şirketin bu değişimlere maruziyetini eklemek, gelecek çeyreğin ana finansal kalemlerini daha iyi tahmin ettiriyor mu?**

Örneğin aynı kur değişimi, ihracat ağırlığı yüksek bir şirket ile ithal girdi ağırlığı yüksek bir şirket için aynı anlamı taşımayabilir. Amaç, bu farklılığın tahmine katkısını ölçmek; ekonomik nedenselliği kanıtlamak değildir. Muhasebe tutarlılığı, bu ana soruya eşlik eden ikinci bir deney olabilir.

Önerilen çalışma başlığı: **BIST şirketlerinde makroekonomik maruziyete duyarlı ve muhasebe açısından tutarlı finansal tablo tahmini.**

Yeni bir sinir ağı mimarisi icat etmek şart değildir. Açıklama tarihleri doğrulanmış bir veri seti, açık bir araştırma sorusu, güçlü kıyaslar ve tekrar üretilebilir sonuçlar daha değerli bir ilk hedef olabilir. Bu kapsamın ders/bitirme araştırmasına uygunluğu ile hakemli yayın için özgünlüğü farklı değerlendirmelerdir; yayın iddiası ayrıca literatür taraması gerektirir.

## 2. Mevcut çalışmalarla dürüst karşılaştırma

| Çalışma | Zaten yaptığı | Bizim araştırabileceğimiz fark |
|---|---|---|
| [Forma: makale](https://arxiv.org/abs/2608.11327), [kod](https://github.com/forma-lab-mccombs/forma-release) | ABD verisinde 78 kalemi 1–20 çeyrek tahmin ediyor; belirsizlik, senaryo ve tahmin sonrası muhasebe düzeltmesini inceliyor. | Daha dar BIST örnekleminde, yayımlanmış makro veriler ve şirket maruziyetleriyle kısa vadeli tahmini sınamak. BIST'e aktarılabilirlik ölçülmeli. |
| [Dario](https://github.com/dario-disanto/quarterly-eps-forecast-study) | Geçmiş EPS ve muhasebe oranlarıyla sonraki EPS; doğrusal regresyon ve boosting. | Tek EPS yerine üç tablonun seçilmiş ana kalemleri; maruziyet özelliklerinin ek katkısı. |
| [Minsu](https://github.com/minsu0011/eps-forecasting) | EPS/TTM geçmişi, çeşitli modeller ve birleşimler; kullanılabilirlik tarihleri ve tahmin aralıkları üzerine kontroller. | Zaman kontrolünü koruyup EPS dışındaki finansal kalemleri ve makro maruziyetleri değerlendirmek. Tarih kontrolü veya aralık vermek tek başına yeni değil. |
| [Yılkı, Yelği, Apan — Optimized machine learning for BIST profitability prediction, 2026](https://link.springer.com/article/10.1007/s10791-026-10602-2) | BIST teknoloji şirketlerinin gelecek çeyrek ROA, ROE ve net kâr marjını; ağaç modelleri, ayar araması ve zamana göre değerlendirmeyle çalışıyor. | Oranlar yerine seçilmiş tablo tutarları ve şirket–makro etkileşimlerinin kontrollü karşılaştırması. “BIST'te ML” tek başına katkı değil. |
| [Koval, Andrews, Yan — Financial Forecasting from Textual and Tabular Time Series, 2024](https://aclanthology.org/2024.findings-emnlp.486/) | Muhasebe, makro ve metinle analist beklentisine göre gelecek kârı tahmin ediyor. | Makro eklemek genel literatürde yeni değil. Bizim soru, BIST'teki maruziyet farklarının çok kalemli tahmine ek katkısı. |

Bu tablo “başkaları yapamıyor, biz yapacağız” iddiası değildir. Bazı özellikler incelenen depoların ana deneylerinde yok; daha geniş literatürde hiç yapılmadıkları söylenemez.

## 3. İlk sürümün sınırları

- **Evren:** Veri pilotu başarılı olursa iki sektörde yaklaşık 20–40 finans dışı şirket. Banka/sigorta ve çok farklı tablo yapıları başlangıçta ayrı tutulur. Sektör ve örneklem seçim kuralı test sonuçları görülmeden yazılır.
- **Ufuk:** Bir çeyrek. Önce 20 çeyrek veya bütün şirketlere genelleme hedeflenmez.
- **Geçmiş:** Bulunabilirse en az 6–8 yıllık çeyrekler; özelliklerde son 8–12 çeyrek. Gerçek kapsam, kaynak ve birim denetiminden sonra belirlenir.
- **Çıktı:** Üç tablodan yaklaşık 15–20 ana kalem. Bu, bütün dipnotları ve bütün kalemleri tamamlanmış rapor değildir.
- **Hesaplama:** İlk deneyler CPU üzerinde yapılabilecek doğrusal regresyon ve ağaç modelleri. GPU gerektiren karşılaştırma, temel sonuçlar çıktıktan sonra isteğe bağlı.

Örnek 17 çıktı kalemi:

| Tablo | Seçilmiş çıktılar | Tanım notu |
|---|---|---|
| Gelir tablosu | Hasılat, satışların maliyeti, brüt kâr, esas faaliyet kârı, finansman gideri, vergi gideri/geliri, dönem net kârı | Brüt kâr, hasılat ve maliyetten hesaplanabilir. Net kârda konsolide dönem kârı/ana ortaklık payı karıştırılmaz. |
| Finansal durum tablosu (dar anlamda bilanço) | Nakit ve nakit benzerleri, ticari alacak, stok, toplam varlık, finansal borç, toplam yükümlülük, toplam özkaynak | Bunlar dönem sonu bakiyeleridir; çeyrek akışı gibi farkları alınarak hedef oluşturulmaz. |
| Nakit akışı tablosu | İşletme, yatırım ve finansman faaliyetlerinden nakit akışları | Kaynakların kümülatif mi yalnız çeyreğe ait mi olduğu doğrulanır. |

Bazı çıktılar hesaplanacağı için 17 çıktı, 17 bağımsız model zorunluluğu yaratmaz. Kalem listesi eksik veri oranına göre pilotta daraltılabilir; test sonucuna göre seçilmez.

## 4. Girdiler ve şirket özellikleri

| Blok | Örnekler | Kullanım gerekçesi ve sınır |
|---|---|---|
| Geçmiş finansallar | Yukarıdaki kalemlerin son açıklanan değerleri, geçen yıl aynı çeyrek, yıllık değişimler; marj, borç/aktif ve nakit dönüşümü | Güçlü temel kıyas. Eksik değer sıfır sayılmaz; gecikmeler gerçek çeyrek takvimine göre eşleştirilir. |
| Takvim ve ölçek | Çeyrek, sektör, önceki toplam varlık veya satış ölçeği | Mevsimsellik ve şirket büyüklüğü için. Dönüşümler sadece eğitim verisiyle öğrenilir. |
| Makro | Kurun ortalaması/değişimi/oynaklığı; TÜFE/ÜFE; faiz; ilgili üretim veya talep göstergesi | Yalnız tahmin anında yayımlanmış gözlemler. İlk deneyde küçük bir liste tutulur. |
| Maruziyet | Önceki rapordan ihracat/satış, döviz pozisyonu/aktif, finansal borç/aktif | Dipnotlardan güvenilir çıkarılabiliyorsa. Borç/aktif, değişken faizli borcun tam ölçüsü değildir. |
| Etkileşim | Kur değişimi × önceki ihracat payı; kur değişimi × önceki döviz pozisyonu/aktif; faiz değişimi × önceki borç/aktif | Şirket özelliklerine göre makro etkilerin tahmin değerini sınar. Katsayı veya SHAP sonucu nedensel etki diye sunulmaz. |

Önceki rapordaki döviz pozisyonu veya ihracat payı düzenli bulunamıyorsa bunları her şirket için elle tamamlama sözü verilmez. Sektör ve basit borç oranıyla küçük bir pilot yapılır; ayrıntılı maruziyet deneyinin kapsamı daraltılır. Bu karar ve kapsama kaybı kaydedilir.

## 5. Deney: her eklemenin katkısını ayrı ölçmek

Mevsimsel kıyas, geçen yılın aynı çeyreğini; son değer kıyası ise son bilinen uygun değeri kullanır. Her iki kıyas da öğrenen modellerle aynı bilgi tarihine uyar. Ayrıca Ridge doğrusal regresyonu ve **tek bir boosting ailesi** (örneğin LightGBM) kullanılır. Kalem başına modeller, bütün şirketlerin geçmiş şirket–çeyrek satırlarından birlikte öğrenebilir; şirket başına ayrı küçük model kurmak gerekmez.

| Deney | Bilgi | Soru |
|---|---|---|
| A | Geçmiş finansallar + takvim/sektör | ML, basit mevsimsel kıyası geçiyor mu? |
| B | A + yayımlanmış makro veriler | Makronun ek tahmin değeri var mı? |
| C | B + geçmiş şirket maruziyetleri | Şirket profili tek başına ne ekliyor? |
| D | C + önceden belirlenmiş makro–maruziyet etkileşimleri | Etkileşimlerin ek katkısı var mı? |
| E, ikincil | D + muhasebe tutarlılığı düzeltmesi | Tutarlılık iyileşirken kalem hataları nasıl değişiyor? |

A–D aynı model ailesi, aynı test gözlemleri ve benzer ayar bütçesiyle karşılaştırılır. Böylece model değişiminin etkisi, veri katkısıyla karıştırılmaz. C ve D'nin ayrılması önemlidir: maruziyet verisi eklemek ile çarpım özelliklerinin katkısı farklı sorulardır. Ağaçlar etkileşimleri zaten öğrenebildiği için D'nin ayrıca fayda sağlamaması mümkündür.

Muhasebe düzeltmesi yalnız tanımı doğrulanmış eşitliklerde uygulanır: örneğin varlık = yükümlülük + özkaynak. Brüt kâr doğrudan hesaplanabilir. Nakit akışları toplamının nakit bakiyesi farkına eşitliği, kur ve diğer mutabakat kalemleri eksikse zorla dayatılmaz. Net kâr köprüsündeki ara kalemler eksikse tam eşitlik kurulmuş gibi davranılmaz. Tek bir “diğer” kaleme hatayı yığmak çözüm sayılmaz.

Bu ilk sürüm, **standart ML + finansal özellik tasarımı + muhasebe kuralları** olarak tanımlanır. Birlikte çalışan tahmin hattı, kendiliğinden yeni bir ortak sinir ağı mimarisi anlamına gelmez.

## 6. Veri ve değerlendirme protokolü

1. **Tahmin anını sabitleyin.** Ana görev örneğin takvim çeyreğinin son günü itibarıyla, o çeyreğe ilişkin henüz açıklanmamış raporun tahmini olsun. Bu, tamamlanmış ancak açıklanmamış çeyreği kestirmedir. Çeyrek başlamadan yapılan tahmin, farklı bir görevdir; o deneyde hedef çeyreğin gerçekleşmiş makrosu kullanılamaz. Açıklamadan hemen önceki tahmin de farklı bilgi avantajı verir ve ayrı raporlanmalıdır.
2. **Kullanılabilirlik tarihi saklayın.** Her girdide dönem, ilk yayımlanma zamanı, alınan sürüm, birim ve kaynak bildirim kimliği bulunsun. Eğitim etiketleri de o eğitim tarihinde yayımlanmış olmalı. İlk açıklanan hedefi mi son düzeltilmiş hedefi mi tahmin ettiğiniz yazılmalı; öneri ilk açıklanan hedefi esas almaktır.
3. **En son değer, geçmişte bilinen değer değildir.** [KAP kılavuzu](https://www.kap.org.tr/tr/api/about/content-file/402832a195b3017d0195bd17e2e07e9a), kalem sorgusunun ilgili dönemin son yayımlanan tablosundaki cari sütunu verdiğini ve ayrıntılar için bildirimlere bakılması gerektiğini açıklıyor. Tek indirme, tarihsel sürüm sorununu çözmez.
4. **Muhasebe tabanını doğrulayın.** Konsolide/solo, TL/bin TL, kümülatif/çeyreklik ve işaret farkları kontrol edilir. Enflasyona göre düzeltilmiş tutarlar farklı satın alma gücü tarihlerinde olabilir. Farklı temellerdeki 6 aylık ve 3 aylık değerleri doğrudan çıkarmak güvenilir çeyrek üretmeyebilir. [KGK rehberi](https://www.kgk.gov.tr/ContentAssignmentDetail/5079/Enflasyon-Muhasebesi-Uygulama-Rehberinin-Gu%CC%88ncellenmesi) esas alınır; basit TÜFE bölmesi tam TMS 29 uygulaması olarak sunulmaz. Bu sorun çözülemiyorsa örneklem veya görev daraltılır.
5. **Zamana göre test edin.** Geçmişte eğitip sonraki çeyreklerde deneyin; şirket–çeyrek satırlarını rastgele bölmeyin. Bütün modeller aynı test çeyreklerini görsün. Özellik, ayar ve örneklem seçimi test sonuçlarına göre değiştirilmesin.
6. **Şirket büyüklüğünün ortalamayı ele geçirmesini önleyin.** Kalem bazında MAE ve eğitim verisinden belirlenmiş ölçekle normalize hata; basit kıyasa göre hata farkı; şirket/sektör/çeyrek kırılımları raporlanır. Zarar ve sıfıra yakın tutarlarda MAPE ana başarı ölçütü yapılmaz.
7. **İkinci ölçütleri ayırın.** Muhasebe eşitliği ihlali, düzeltme öncesi/sonrası hata ve çalışma maliyeti gösterilir. Tahmin aralığı eklenirse kapsama ile genişlik birlikte ölçülür; aralık vermek tek başına güvenilirlik kanıtı değildir.
8. **Küçük örneklemi dürüst gösterin.** Örneğin 30 şirket × 32 çeyrek, eksikler öncesi 960 şirket–çeyrek satırıdır; 17 hedef olması bunu 16.320 bağımsız örneğe dönüştürmez. Aynı çeyrekte şirketler ortak şok yaşayabilir. Hata farklarının belirsizliği çeyrek bloklarını koruyarak incelenir.

“Her kalemde üstünlük” veya belirli bir yüzde başarı garanti edilemez. Makro ya da etkileşimler fayda sağlamazsa da düzgün kurulmuş deney bir araştırma sonucu üretir. Başarı, gerçek koşullarda neyin işe yaradığını ölçebilmektir.

## 7. Dört kişinin ilk sürümde üstlenmemesi gereken işler

| Kapsam | Neden erteleyelim? | Sınırlı alternatif |
|---|---|---|
| Her ülke, her sektör, her şirket | Raporlama ve veri eşleme kapsamı aşırı büyür. | İki sektör ve açık seçim kurallı örneklem. |
| 78 kalem × 20 çeyrek; onlarca model | Çıktı ve deney sayısı büyür, ana araştırma sorusu kaybolur. | Yaklaşık 17 kalem × tek çeyrek; basit kıyaslar + Ridge + bir boosting ailesi. |
| Forma'nın büyük tarihsel Compustat evrenini bire bir kopyalamak | Lisanslı veri, eşleme ve hesaplama erişimi gerektirir. | Erişilebilir örneklemde uygun kıyas. Farklı veri setlerindeki skorlar doğrudan üstünlük kanıtı yapılmaz. |
| Sıfırdan genel amaçlı zaman serisi modeli veya yeni Transformer | Veri altyapısı tamamlanmadan mimari geliştirmek riski büyütür. | Gerekirse hazır küçük bir modeli sonradan tek ek kıyas olarak denemek. Forma'nın kendisi küçük bir modeldir; mesele “dört kişi eğitemez” değildir. |
| Aynı anda haber, sosyal medya, PDF ajanı ve bütün dipnotlar | Temizleme, zaman damgası, maliyet ve ek hata kaynakları. | Çekirdek deneyden sonra sınırlı, doğrulanabilir metin özellikleri. |
| Tam TMS 29 hesaplama motoru | Gerekli tarihsel dipnotlar ve işlem ayrıntıları eksik olabilir. | Raporlanmış verinin satın alma gücü temelini denetlemek; çözülemeyen kapsamı açıkça sınırlamak. |
| Canlı alım satım ve fiyat tahmini | Finansal rapor tahmininden farklı hedef ve ek ürün yükü. | Tahmin–gerçekleşen karşılaştırmasını gösteren basit bir rapor ekranı. |

Bunlar kişi sayısından dolayı kesinlikle imkânsız işler değildir. Bir dönemlik araştırmada beklenen katkılarına göre pahalı işlerdir.

## 8. İş bölümü ve ilk karar noktası

| Sorumluluk | Ana çıktı |
|---|---|
| Kişi 1 — Veri | Kaynak bildirimler, ilk açıklama zamanları, tekrar çalıştırılabilir veri çekme ve kaynak kaydı. |
| Kişi 2 — Muhasebe | Kalem sözlüğü, dönem/birim/enflasyon denetimi, maruziyet özellikleri ve geçerli eşitlikler. |
| Kişi 3 — Model | Basit kıyaslar, Ridge/boosting, A–D deneyleri; ortak eğitim arayüzü. |
| Kişi 4 — Değerlendirme | Tarihsel test düzeni, hata ve belirsizlik analizleri, deney kayıtları ve araştırma raporu. |

Herkes ortak küçük veri örneğini inceler; veri kontrolleri ve test tasarımı tek kişinin denetimine bırakılmaz. Dört kişinin dört farklı model kurup sonunda birleştirmesi önerilmez.

**İlk 1–2 haftanın somut hedefi:** 5–10 şirketin dört çeyreğinde, yaklaşık 17 kalemi kaynak bildirimine bağlayıp elle kontrol etmek; açıklama tarihlerini, birimleri, kümülatif dönemleri ve enflasyon temelini doğrulamak. Maruziyet dipnotlarının erişilebilirliğini ayrıca ölçmek. Bu küçük örnek model başarısını ölçmek için yeterli değildir; veri hattının yapılabilirliğini sınar.

Pilot başarılıysa önce geçmiş finansallarla A deneyi kurulur. Sonra B–D eklenir. Muhasebe düzeltmesi ve tahmin aralıkları, veri ve ana deney tamamlandıktan sonra gelir. İlk rapor teslimine kadar güçlü bir temel sonuç elde etmek, bütün ekleri yarım bırakmaktan daha değerlidir.

## 9. Geliştirici deneyimlerinden iki sınırlı gözlem

DevRelay Community Wisdom araştırmasında iki ilgili yazının tam metni ve yorumları incelendi. Bunlar akademik kanıt veya topluluk uzlaşısı değildir; ilki veri sağlayıcısının deneyimi, ikincisi tek bir zaman serisi denemesidir.

- 🗂️ [How to Build a Point-in-Time Fundamentals Database from SEC EDGAR (and When Not To)](https://dev.to/tradevodata/how-to-build-a-point-in-time-fundamentals-database-from-sec-edgar-and-when-not-to-2gn6) [@tradevodata](https://dev.to/tradevodata) — İlk açıklama, düzeltme sürümleri ve çeyrek/yıl eşleme hataları, veri mühendisliğine ayrı iş paketi ayırmamızı destekliyor. 🔗 [Read Full Discussion on DEV](https://dev.to/tradevodata/how-to-build-a-point-in-time-fundamentals-database-from-sec-edgar-and-when-not-to-2gn6)
- 📏 [Mistral shipped a time-series foundation model today. I measured its latency — and its confidence.](https://dev.to/frankchu/mistral-shipped-a-time-series-foundation-model-today-i-measured-its-latency-and-its-confidence-4mdd) [@frankchu](https://dev.to/frankchu) — Tek seride iyi nokta tahminiyle zayıf aralık kapsamasının birlikte görülmesi, aralıkların ayrıca test edilmesi gerektiğini hatırlatıyor; BIST veya Forma hakkında sonuç çıkarmıyor. 🔗 [Read Full Discussion on DEV](https://dev.to/frankchu/mistral-shipped-a-time-series-foundation-model-today-i-measured-its-latency-and-its-confidence-4mdd)

**Karar önerisi:** Önce doğrulanmış küçük veri pilotu; ardından aynı model üzerinde geçmiş finansal → makro → maruziyet → etkileşim karşılaştırması. En güçlü araştırma çıktısı, bu ilavelerin hangi kalem ve şirketlerde işe yaradığını veya yaramadığını açıkça göstermek olacaktır.
