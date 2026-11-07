# Veri kapsamı ve toplama planı

İnceleme tarihi: **7 Kasım 2026**. Tanım kaynağı: [`degiskenler.json`](degiskenler.json), sürüm **0.1.0**. Aşağıdaki “eski” değerlendirmeleri **91a7d0e** commitindeki kodu anlatır; bu çalışma sırasında üretilen yeni CSV’nin ölçülmüş kapsaması veya yeni dalın başarı raporu değildir.

Belgede **51 özellik ailesi ve 17 hedef** var. Bir aile birden çok ham tutar, pay, gecikme ve dönüşüm içerebilir; 51 aileyi 51 sütun saymak veya tabloda bir sütun bulunduğu için aileyi tamamlandı saymak doğru değildir. Sözlük halen aday listesidir: P0 pilot, P1 kaynak uygunsa ek, P2 daha kapsamlı dipnot/olay çalışmasıdır. Hepsinin aynı modelde kullanılması kararı alınmış değildir.

## Kapsamı tamamlandı sayma koşulu

Her şirket/dönem/ham alan için değer kadar kaynak bildirimi, orijinal birim, çarpan, para birimi, konsolidasyon, dönem türü, sürüm, gerçek açıklanma zamanı ve satın alma gücü tarihi de gerekir. Yeni indirilmiş bir tablo güncel sürümü gösterebilir; ilk raporun tarihi bu revize tabloya yapıştırılamaz. Açıklanma/sürüm doğrulanmadıysa `unavailable_vintage`, henüz çıkarılmadıysa `not_extracted` yazılır. `not_disclosed` ancak kaynak incelenip açıklanmadığı görüldüğünde; `not_applicable` ise kapsam gereği uygulanmadığı doğrulandığında kullanılmalıdır. Eksik değer sıfır değildir.

Tahmin örneği ayrı bir kayıt olmalıdır: `ticker`, hedef çeyrek `q`, sabit bilgi kesimi `t0`, hedef alanlar ve yalnız `available_at <= t0` olan girdiler. Referans `q−1` henüz yayımlanmadıysa gelecekte yayımlanmış değerle doldurulmaz. Hedefin `q−4` mevsimsel referansı ile son bilinen `r` çeyreğinin `r−4` yıllık değişimi ayrı değişkenlerdir. Kaynak sürümü belirsiz kayıtların bulunması, bu kayıtlardan eğitim üretme izni değildir.

## Hedeflerin ham kaynak eşlemesi

Bütün hedeflerde ana kaynak KAP kaynak finansal raporudur. Akışlarda YTD ve doğrudan raporlanan 3 aylık değer ayrı saklanır. YTD farkı ancak aynı şirket, konsolidasyon, para birimi ve satın alma gücü temeli arasında alınır; karşılaştırma raporu düzeltilmişse aynı sürüm temeli gerekir. Bakiyelerde YTD farkı alınmaz.

| ID | Hedef | Tür | Alınacak ham kalem ve özel kontrol |
|---|---|---|---|
| T01 | Hasılat | akış | Gelir tablosunda hasılat; finans sektörü gelirleri sessiz ikame edilmez. |
| T02 | Satışların maliyeti | akış | Satışların maliyeti; rapor işareti korunur, standart gider işareti dönüşümü kaydedilir. |
| T03 | Brüt kâr | türetilmiş akış | Raporlanan brüt kâr ve ayrıca hasılat/maliyet uzlaşması; aynı dönem ve işaret temeli. |
| T04 | Esas faaliyet kârı | akış | Esas faaliyet sonucu; FAVÖK ile aynı alan değildir. |
| T05 | Finansman gideri | akış | Finansman giderleri; finansman gelirinden ayrı, faiz gideri varsa ayrıca. |
| T06 | Vergi gideri/geliri | akış | Dönemin vergi gideri/geliri; cari ve ertelenmiş vergi ile uzlaşma mümkünse korunur. |
| T07 | Dönem net kârı | akış | Toplam dönem net kârı; ana ortaklık payı ayrı yardımcı alandır, birbirine kopyalanmaz. |
| T08 | Nakit ve nakit benzerleri | dönem sonu bakiye | Nakit ve nakit benzerleri dönem sonu bakiyesi; kısıtlı nakit/kapsam ayrıca. |
| T09 | Ticari alacak | dönem sonu bakiye | Kısa ve uzun vadeli ticari alacak; toplam ile bileşenler çifte sayılmaz; eksik vade sıfır değildir. |
| T10 | Stok | dönem sonu bakiye | Stoklar dönem sonu; faaliyet ve konsolidasyon kapsamı korunur. |
| T11 | Toplam varlık | dönem sonu bakiye | Toplam varlık; dönen+duran uzlaşması ve birim tutarlılığı. |
| T12 | Finansal borç | dönem sonu bakiye | Kısa/uzun vadeli finansal borç ve uzun borcun kısa vadeli kısmı; ana toplam/alt kalem çifte sayılmaz. |
| T13 | Toplam yükümlülük | dönem sonu bakiye | Toplam yükümlülük; finansal borç değildir. Kısa/uzun toplamlar eksikse kısmi toplam tam diye sunulmaz. |
| T14 | Toplam özkaynak | dönem sonu bakiye | Toplam özkaynak; ana ortaklık payı ve kontrol gücü olmayan paylar ayrı. |
| T15 | İşletme faaliyetlerinden nakit akışı | akış | İşletme faaliyetlerinden toplam net nakit akışı; bölümdeki son dolu satır otomatik toplam değildir. |
| T16 | Yatırım faaliyetlerinden nakit akışı | akış | Yatırım faaliyetlerinden toplam net nakit akışı; nakit CAPEX değildir. |
| T17 | Finansman faaliyetlerinden nakit akışı | akış | Finansman faaliyetlerinden toplam net nakit akışı; borç bakiyesi değildir. |

FAVÖK, EPS, CAPEX ve nakitte net değişim üst README'de anılır; bunlar 17 kayıt hedefiyle bire bir aynı liste değildir. Eklenirken bağımsız tanım gerekir. Ödenmiş sermayeye bölünen net kâr, dönem içi sermaye değişimi ve ağırlıklı ortalama pay sayısı doğrulanmadan raporlanmış EPS diye adlandırılamaz.

## 51 ailenin kaynak ve engel eşlemesi

“İlk temsil” ve “ilgili hedefler” yetkili JSON’dan aktarılmıştır. Kaynak maddeleri toplama rotasıdır; bu rapor bütün bağlantılardan veri indirilmiş veya tarihsel sürüm doğrulanmış olduğunu iddia etmez. Akademik dayanaklar veri sağlayıcısı yerine gösterilmemiştir.

### Finansal yapı ve geçmiş

**F01 · P0 — Şirket ölçeği**

- Ham alanlar: `total_assets`.
- İlk temsil: Bilinen aktif; ölçek ayrıca korunur. İlgili hedefler: T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13, T14, T15, T16, T17.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Ham tutar eşlemesi var; birim, konsolidasyon, kaynak sürümü ve açıklanma zamanı doğrulanmadan girdi kabul edilmez. Hedef dönemin aktif değeri ölçek olarak kullanılamaz.

**F02 · P0 — Hasılat geçmişi**

- Ham alanlar: `revenue`.
- İlk temsil: q−1 / q−4; sınırlı yıllık değişim. İlgili hedefler: T01, T03, T04, T07, T09, T10.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Ham tutar eşlemesi var; birim, konsolidasyon, kaynak sürümü ve açıklanma zamanı doğrulanmadan girdi kabul edilmez. Sıfır/negatif paydada büyüme oranı zorlanmaz.

**F03 · P0 — Satış maliyeti ve brüt marj**

- Ham alanlar: `cost_of_sales`, `gross_margin`.
- İlk temsil: Maliyet/aktif; (hasılat−maliyet)/hasılat. İlgili hedefler: T02, T03, T04, T07.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Satış maliyetinin işareti ve aynı dönem hasılatı doğrulanmalı; brüt kâr aynı iki bileşenden türetilir. Giderin işareti standartlaştırılmalı; brüt kâr aynı bilgiden türetilir.
- Bağımlılıklar: F01, F02; politika: `all`.

**F04 · P0 — Faaliyet kârı ve marjı**

- Ham alanlar: `operating_income`, `operating_margin`.
- İlk temsil: Kâr/aktif ve faaliyet marjı. İlgili hedefler: T04, T07, T15.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Ham tutar eşlemesi var; birim, konsolidasyon, kaynak sürümü ve açıklanma zamanı doğrulanmadan girdi kabul edilmez. Şirketlerin esas faaliyet/FAVÖK tanımları karıştırılmaz.
- Bağımlılıklar: F01, F02; politika: `all`.

**F05 · P0 — Dönem net kârı**

- Ham alanlar: `net_income`.
- İlk temsil: q−1 / q−4; değişim/bilinen aktif. İlgili hedefler: T07, T14, T15.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Konsolide toplam kâr ile ana ortaklık payı ayrı tutulmalı; biri eksik diye diğeri kopyalanmaz. Ana ortaklık kârı ile toplam konsolide dönem kârı ayrılır.
- Bağımlılıklar: F01; politika: `all`.

**F06 · P0 — İşletme nakit akışı ve tahakkuk**

- Ham alanlar: `operating_cash_flow`, `accrual_proxy`.
- İlk temsil: CFO/aktif; (net kâr−CFO)/aktif. İlgili hedefler: T07, T08, T15.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Eski nakit akışı bölüm sonu yedeği herhangi bir alt satırı toplam sayabiliyor; açık toplam ve aynı dönem/kapsam gerekir. Kâr/CFO aynı dönem ve konsolidasyonda olmalı; basit fark tam tahakkuk ayrıştırması değildir.
- Bağımlılıklar: F01, F05; politika: `all`.

**F07 · P0 — Vergi gideri/geliri**

- Ham alanlar: `income_tax_expense`.
- İlk temsil: Tutar/aktif; aktif ölçekli yıllık değişim. İlgili hedefler: T06, T07.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Eski CSV F07 öneki finansman geliri için de kullanılmış; sözlükte F07 vergi ailesidir. Kimlik ve alan eşlemesi düzeltilmeli. Efektif vergi oranı sıfıra yakın vergi öncesi kârda kullanılmaz.
- Bağımlılıklar: F01; politika: `all`.

**F08 · P0 — Finansman ve faiz giderleri**

- Ham alanlar: `finance_cost`, `interest_expense_if_separate`.
- İlk temsil: Ayrı raporlanan tutarlar/aktif. İlgili hedefler: T05, T07, T17.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Finansman gideri var; ayrıca raporlanmış faiz gideri için dipnot eşlemesi eksik. Faiz ve toplam finansman aynı şey değildir. Finansman gideri faizden daha geniş olabilir; gelirlerle körlemesine netlenmez.
- Bağımlılıklar: F01; politika: `all`.

**F09 · P0 — Nakit ve nakit benzerleri**

- Ham alanlar: `cash_and_equivalents`.
- İlk temsil: Bakiye/aktif; önceki karşılaştırılabilir dönem. İlgili hedefler: T08, T12, T15.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Ham tutar eşlemesi var; birim, konsolidasyon, kaynak sürümü ve açıklanma zamanı doğrulanmadan girdi kabul edilmez. Bakiye bir çeyrek akışı değildir; kısıtlı nakit kapsamı kaydedilir.
- Bağımlılıklar: F01; politika: `all`.

**F10 · P0 — Ticari alacak**

- Ham alanlar: `trade_receivables`.
- İlk temsil: Alacak/aktif; sınırlı değişim; alacak/satış aday. İlgili hedefler: T08, T09, T15.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Ham tutar eşlemesi var; birim, konsolidasyon, kaynak sürümü ve açıklanma zamanı doğrulanmadan girdi kabul edilmez. Sözleşme varlığı ile koşulsuz ticari alacak aynı değildir.
- Bağımlılıklar: F01, F02; politika: `all`.

**F11 · P0 — Stok**

- Ham alanlar: `inventories`.
- İlk temsil: Stok/aktif ve yıllık değişim. İlgili hedefler: T02, T08, T10, T15.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Ham tutar eşlemesi var; birim, konsolidasyon, kaynak sürümü ve açıklanma zamanı doğrulanmadan girdi kabul edilmez. Stok/maliyet oranı stok ve akış döneminin tanımı korunarak üretilir.
- Bağımlılıklar: F01; politika: `all`.

**F12 · P0 — Ticari borç**

- Ham alanlar: `trade_payables`.
- İlk temsil: Bakiye/aktif ve değişim. İlgili hedefler: T08, T13, T15.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Ham tutar eşlemesi var; birim, konsolidasyon, kaynak sürümü ve açıklanma zamanı doğrulanmadan girdi kabul edilmez. Finansal borçla aynı hesap sayılmaz.
- Bağımlılıklar: F01; politika: `all`.

**F13 · P0 — Finansal borç ve vade dağılımı**

- Ham alanlar: `short_term_financial_debt`, `long_term_financial_debt`, `financial_debt_to_assets`.
- İlk temsil: Borç/aktif; kısa vadeli borç/aktif. İlgili hedefler: T05, T08, T12, T17.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Kısa/uzun vadeli kalemler ve uzun borcun kısa vadeli kısmı çifte sayılmamalı; açıklanmayan bileşen sıfır değildir. Toplam yükümlülük finansal borç değildir; kısa vadeye aktarılan uzun borç doğru eşlenir.
- Bağımlılıklar: F01; politika: `all`.

**F14 · P0 — Yükümlülük ve özkaynak**

- Ham alanlar: `total_liabilities`, `total_equity`.
- İlk temsil: Ayrı bakiyeler/aktif. İlgili hedefler: T11, T13, T14.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Toplam özkaynak ile ana ortaklık özkaynağı ayrı; toplamdan kopyalama ile ana ortaklık değeri üretilmez. Kontrol gücü olmayan pay kapsamı ve bilanço eşitliği tanımları tutarlı olmalı.
- Bağımlılıklar: F01; politika: `all`.

**F15 · P1 — Yatırım, duran varlık ve amortisman**

- Ham alanlar: `cash_capex`, `property_plant_equipment`, `depreciation`.
- İlk temsil: CAPEX/aktif; PPE/aktif; amortisman ayrı. İlgili hedefler: T02, T04, T11, T16.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: CAPEX, maddi duran varlık ve amortisman ayrı alınmalı; T16 yatırım nakit akışı CAPEX yerine geçmez. Nakit CAPEX toplam yatırım nakit akışı veya toplam yatırım taahhüdüyle aynı değildir.
- Bağımlılıklar: F01; politika: `all`.

**F16 · P1 — Faaliyet giderleri ve Ar-Ge**

- Ham alanlar: `selling_expense`, `administrative_expense`, `expensed_rd`, `capitalized_rd`.
- İlk temsil: Satış veya aktif ölçekli, ayrı kalemler. İlgili hedefler: T04, T07, T11, T16.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Eski çıkarıcıda ayrı alan yok; kaynak dipnot ve tablo bağlamı ile çıkarım/eşleme gerekir. Ar-Ge aktifleştirmesi kâr ve nakdi farklı etkiler; aynı kalem gibi toplanmaz.
- Bağımlılıklar: F01, F02; politika: `all`.

**F17 · P1 — Sözleşme varlığı**

- Ham alanlar: `contract_assets`.
- İlk temsil: Bakiye/aktif ve değişim. İlgili hedefler: T01, T08, T09, T15.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: TFRS 15 dönemleri ve eski avans/alacak adlandırmaları karşılaştırılmalı; ticari alacak otomatik vekil değildir. Proje sektörlerinde önemli aday; ticari alacağa otomatik eklenmez.
- Bağımlılıklar: F01; politika: `all`.

**F18 · P1 — Müşteri avansı ve sözleşme yükümlülüğü**

- Ham alanlar: `contract_liabilities`, `customer_advances`.
- İlk temsil: Ayrı bakiyeler/aktif ve değişim. İlgili hedefler: T01, T08, T13, T15.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Kısa/uzun vade ve ifa kapsamı eşlenmeli; avans gelir sayılmaz. Avans nakit yaratabilir; aynı anda gelir veya kâr sayılmaz.
- Bağımlılıklar: F01; politika: `all`.

**F19 · P1 — Net döviz pozisyonu**

- Ham alanlar: `net_fx_position`, `fx_sensitivity`.
- İlk temsil: İşareti korunmuş pozisyon/aktif; mümkünse para birimi ayrımı. İlgili hedefler: T05, T07, T08, T12.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Döviz riski dipnotundan para birimi, türev dahil/hariç kapsam ve duyarlılık senaryosu gerekir. Türev/korunma kapsamı korunur; finansal araç duyarlılığı tüm operasyonel etki değildir.
- Bağımlılıklar: F01; politika: `all`.

**F20 · P2 — Borç koşulları ve korunma**

- Ham alanlar: `floating_rate_debt_share`, `debt_currency_mix`, `debt_maturity`, `hedging_terms`.
- İlk temsil: Önceki açıklanmış paylar ve koşullar. İlgili hedefler: T05, T07, T08, T12, T17.
- Kaynak: KAP kaynak finansal raporu; gerekiyorsa aynı bildirimin dipnotları ([KAP](https://kap.org.tr/tr/icerik/Diger/yardim)).
- Engeller/kontrol: Borç dipnotundan faiz türü, para birimi, vade ve korunma şartları; her şirket/dönem açıklamayabilir. Türev nominali ekonomik korunma oranı değildir; net değer/vade temelleri farklı olabilir.
- Bağımlılıklar: F13; politika: `all`.

### Türkiye makrosu ve sektör koşulları

**M01 · P0 — USD/TL değişimi**

- Ham alanlar: `usdtry`.
- İlk temsil: İlk aday: son bilinen 90 günlük değişim. İlgili hedefler: T01, T02, T05, T07, T12.
- Kaynak: [TCMB EVDS](https://evds3.tcmb.gov.tr/); ilgili seri için [TÜİK veri takvimi](https://tuik.gov.tr/Kurumsal/Veri_Takvimi) ve seri metaverisi.
- Engeller/kontrol: Eski seri Yahoo kaynaklı; resmi alış/satış kuru seçimi, 90 takvim günü tanımı, eksik gün ve yayım zamanı doğrulanmalı. Gelecek çeyrek gerçekleşmiş kuru kullanılamaz; satış ve bilanço etkileri farklıdır.

**M02 · P0 — EUR/TL değişimi**

- Ham alanlar: `eurtry`.
- İlk temsil: İlk aday: son bilinen 90 günlük değişim. İlgili hedefler: T01, T02, T05, T07, T12.
- Kaynak: [TCMB EVDS](https://evds3.tcmb.gov.tr/); ilgili seri için [TÜİK veri takvimi](https://tuik.gov.tr/Kurumsal/Veri_Takvimi) ve seri metaverisi.
- Engeller/kontrol: Eski seri Yahoo kaynaklı; EUR/TL için ayrı resmi seri ve 90 takvim günü karşılaştırması gerekir. Dolar ve avro maruziyetleri birbirinin yerine varsayılmaz.

**M03 · P0 — Ticari kredi faizi**

- Ham alanlar: `try_commercial_loan_rate`.
- İlk temsil: Son yayımlanan seviye ve tek değişim özeti. İlgili hedefler: T05, T07, T12, T17.
- Kaynak: [TCMB EVDS](https://evds3.tcmb.gov.tr/); ilgili seri için [TÜİK veri takvimi](https://tuik.gov.tr/Kurumsal/Veri_Takvimi) ve seri metaverisi.
- Engeller/kontrol: Sözlük ticari kredi faizi ister. Politika veya bankalararası faiz sessiz ikame olamaz; EVDS ticari kredi seri kimliği ve erişim anahtarı doğrulanmalı. Şirketin gerçek kredi marjı/faiziyle aynı değildir; EVDS seri kodu eşlenecek.

**M04 · P0 — TÜFE**

- Ham alanlar: `cpi_yoy`.
- İlk temsil: Son yayımlanmış aylık yıllık değişim. İlgili hedefler: T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13, T14, T15, T16, T17.
- Kaynak: [TCMB EVDS](https://evds3.tcmb.gov.tr/); ilgili seri için [TÜİK veri takvimi](https://tuik.gov.tr/Kurumsal/Veri_Takvimi) ve seri metaverisi.
- Engeller/kontrol: TCMB/TÜİK yıllık TÜFE mevcut olsa bile gözlem ayı yayım ayı değildir; gerçek tarih ve eski sürüm gerekir. Fiyat endeksi girdisi, TMS 29 raporlama temelinin otomatik düzeltilmesi değildir.

**M05 · P0 — Yİ-ÜFE**

- Ham alanlar: `domestic_ppi_yoy`.
- İlk temsil: Son yayımlanmış aylık yıllık değişim. İlgili hedefler: T01, T02, T03, T04.
- Kaynak: [TCMB EVDS](https://evds3.tcmb.gov.tr/); ilgili seri için [TÜİK veri takvimi](https://tuik.gov.tr/Kurumsal/Veri_Takvimi) ve seri metaverisi.
- Engeller/kontrol: ÜFE/Yİ-ÜFE kapsamı ve tarihsel baz geçişleri doğrulanmalı; yayım ve revizyon kaydı gerekir. Sektörün gerçek girdi sepetini tam temsil etmeyebilir.

**M06 · P0 — Sanayi üretimi**

- Ham alanlar: `industrial_production_yoy`.
- İlk temsil: Son yayımlanmış yıllık değişim ve gözlem yaşı. İlgili hedefler: T01, T02, T10, T15.
- Kaynak: [TCMB EVDS](https://evds3.tcmb.gov.tr/); ilgili seri için [TÜİK veri takvimi](https://tuik.gov.tr/Kurumsal/Veri_Takvimi) ve seri metaverisi.
- Engeller/kontrol: Takvim/mevsim düzeltme türü ile endeks/yıllık değişim ayrılmalı; güncel revize seri eski tahminde bilinmiş sayılamaz. Açıklama gecikmesi ve mevsimsel revizyonlar var; hedef aya göre doldurulmaz.

**M07 · P1 — İlgili emtia fiyatı**

- Ham alanlar: `sector_commodity_price_change`.
- İlk temsil: Sektör için önceden seçilmiş az sayıda emtia değişimi. İlgili hedefler: T01, T02, T03, T10, T15.
- Kaynak: [TCMB EVDS](https://evds3.tcmb.gov.tr/); ilgili seri için [TÜİK veri takvimi](https://tuik.gov.tr/Kurumsal/Veri_Takvimi) ve seri metaverisi.
- Engeller/kontrol: Sözlük tek emtia seçmiyor; ilgili sektör/ürün başına az sayıda resmi emtia serisi önceden tanımlanmalı. Bir emtia bütün sektörleri aynı yönde etkilemez; uygun tarihsel kaynak eşlenecek.

**M08 · P1 — Sektör talep ve faaliyet göstergesi**

- Ham alanlar: `sector_demand_index`, `sector_activity_index`.
- İlk temsil: Önceden belirlenen tek/az sayıda yayımlanmış gösterge. İlgili hedefler: T01, T04, T10, T15.
- Kaynak: [TCMB EVDS](https://evds3.tcmb.gov.tr/); ilgili seri için [TÜİK veri takvimi](https://tuik.gov.tr/Kurumsal/Veri_Takvimi) ve seri metaverisi.
- Engeller/kontrol: Sözlük seri kimliğini açık bırakıyor; sektörün üretim/talep göstergesi seçilip yayın takvimi doğrulanmalı. Hangi seri olduğu pilotta eşlenir; her sektörde aynı gösterge kullanılmaz.

### Küresel risk

**R01 · P0 — GPR: jeopolitik risk**

- Ham alanlar: `global_gpr`, `country_gpr_optional`.
- İlk temsil: Son yayımlanmış aylık küresel seviye; ülke serileri profil uzantısında. İlgili hedefler: T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13, T14, T15, T16, T17.
- Kaynak: [Caldara–Iacoviello resmi GPR verisi ve arşivi](https://www.matteoiacoviello.com/gpr.htm).
- Engeller/kontrol: Eski dosyada güncel seri var; gözlem dönemi, gerçek yayım ve veri sürümü ayrı saklanmalı. Ülke GPR kapsamı ayrıca çıkarılmalı. Aylık ay başı, günlük küresel seri haftalık güncellenir; gözlem/yayım ve eski sürüm ayrılır.

**R02 · P0 — GEPU: ekonomik politika belirsizliği**

- Ham alanlar: `gepu_ppp`.
- İlk temsil: Son yayımlanmış aylık seviye; tek tanımlı sürüm. İlgili hedefler: T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13, T14, T15, T16, T17.
- Kaynak: [GEPU resmi aylık veri kaynağı](https://policyuncertainty.com/global_monthly.html).
- Engeller/kontrol: PPP ağırlıklı sürüm sabitlenmeli; tarihsel ilk yayım tarihi/sürümü olmadan sabit gecikme uydurulmaz. Tarihsel ilk yayımlanma saati/sabit gecikme varsayılmaz; arşiv veya snapshot gerekir.

**R03 · P0 — OFR FSI: finansal stres**

- Ham alanlar: `ofr_fsi_global`.
- İlk temsil: Bilinen son 60 işlem günü ortalaması. İlgili hedefler: T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13, T14, T15, T16, T17.
- Kaynak: [OFR resmi Financial Stress Index](https://www.financialresearch.gov/financial-stress-index/).
- Engeller/kontrol: İki iş günü gecikme ve veri sürümü doğrulanmalı; 60 işlem günü ortalaması takvim günlük ileri doldurulmuş ortalama değildir. İki iş günü geriden gelir; negatif değer alabilir; revizyonlar kaydedilir.

**R04 · P1 — GPR tehdit / gerçekleşen eylem ayrımı**

- Ham alanlar: `gpr_threats`, `gpr_acts`.
- İlk temsil: GPRT / GPRA; toplam GPR’ye alternatif veya kontrollü ek. İlgili hedefler: T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13, T14, T15, T16, T17.
- Kaynak: [Caldara–Iacoviello resmi GPR verisi ve arşivi](https://www.matteoiacoviello.com/gpr.htm).
- Engeller/kontrol: Eski dosyada güncel seri var; gözlem dönemi, gerçek yayım ve veri sürümü ayrı saklanmalı. Ülke GPR kapsamı ayrıca çıkarılmalı. Aynı haber bilgisini çoğaltabilir; ek katkı test edilmeden birlikte tutulmaz.
- Bağımlılıklar: R01; politika: `all`.

### Şirket profili

**C01 · P0 — Tarihsel sektör ve faaliyet kategorisi**

- Ham alanlar: `historical_industry`, `business_role`.
- İlk temsil: Kaynaklı kategori; çok faaliyetli yapı ayrıca işaretlenir. İlgili hedefler: T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13, T14, T15, T16, T17.
- Kaynak: KAP aynı tarihte yayımlanmış yıllık/ara dönem raporu, dipnot ve faaliyet raporu; şirket yatırımcı ilişkileri asıl raporu.
- Engeller/kontrol: Eski 30 şirket listesinde bugünkü sabit sektör etiketleri var; geçmiş sektör/faaliyet sürümü ve kategori kaynağı yok. Bugünkü sektör geçmişe taşınmaz; kategori gelir payı değildir.

**C02 · P1 — Ürün / faaliyet gelir karması**

- Ham alanlar: `segment_revenue_shares`.
- İlk temsil: Son açıklanmış faaliyet gelir payları ve kapsama. İlgili hedefler: T01, T02, T03, T04, T07.
- Kaynak: KAP aynı tarihte yayımlanmış yıllık/ara dönem raporu, dipnot ve faaliyet raporu; şirket yatırımcı ilişkileri asıl raporu.
- Engeller/kontrol: Segment hasılatı/toplam hasılat ve faaliyet tanımları dönem bazında çıkarılmamış. Şirket isminden sayısal pay tahmin edilmez. Şirket ismi veya sektör etiketiyle sayısal pay uydurulmaz; kategori ve pay ayrılır.
- Bağımlılıklar: C01; politika: `all`.

**C03 · P1 — Yurtdışı gelir ve ihracat payları**

- Ham alanlar: `foreign_revenue_share`, `export_revenue_share`.
- İlk temsil: Kaynakta ayrı açıklanıyorsa iki ayrı pay. İlgili hedefler: T01, T02, T07, T09.
- Kaynak: KAP aynı tarihte yayımlanmış yıllık/ara dönem raporu, dipnot ve faaliyet raporu; şirket yatırımcı ilişkileri asıl raporu.
- Engeller/kontrol: İhracat ve yurtdışı hasılat payı ayrı çıkarılmalı; yabancı iştirakin yerel satışı ihracat değildir. Yabancı iştirakin yerel satışı Türkiye’den ihracat değildir.

**C04 · P1 — Satış coğrafyası ve yoğunlaşma**

- Ham alanlar: `geographic_revenue_shares`, `geographic_concentration`.
- İlk temsil: Açıklanmış paylar; kapsama; uygun yoğunlaşma. İlgili hedefler: T01, T04, T07, T09.
- Kaynak: KAP aynı tarihte yayımlanmış yıllık/ara dönem raporu, dipnot ve faaliyet raporu; şirket yatırımcı ilişkileri asıl raporu.
- Engeller/kontrol: Satış ülke/bölge tutarları ve açıklanan kapsam çıkarılmamış; bölge bilgisi ülkeye keyfi dağıtılmaz. TFRS 8 tam ülke matrisi garanti etmez; bölgeden ülke payı üretilmez; satış coğrafyası tedarik değildir.

**C05 · P2 — Müşteri türü ve yoğunlaşması**

- Ham alanlar: `public_customer_share`, `largest_customer_share`.
- İlk temsil: Kaynaklı kategori/pay; açıklanmadıysa eksik. İlgili hedefler: T01, T07, T09, T15.
- Kaynak: KAP aynı tarihte yayımlanmış yıllık/ara dönem raporu, dipnot ve faaliyet raporu; şirket yatırımcı ilişkileri asıl raporu.
- Engeller/kontrol: Kamu müşterisi payı ve büyük müşteri payı raporlanıyorsa alınır; raporlanmayan kimlik/pay eksik kalır. Büyük müşteri kimliği zorunlu olmayabilir; ilişkili taraf payı kamu payı değildir.

**C06 · P2 — Tedarik ve ithal girdi profili**

- Ham alanlar: `imported_input_share`, `supplier_geography`, `supplier_concentration`.
- İlk temsil: Açıklanmış pay veya kaynaklı nitel kategori. İlgili hedefler: T02, T03, T10, T15.
- Kaynak: KAP aynı tarihte yayımlanmış yıllık/ara dönem raporu, dipnot ve faaliyet raporu; şirket yatırımcı ilişkileri asıl raporu.
- Engeller/kontrol: İthal girdi, tedarikçi coğrafyası ve yoğunlaşma hazır toplu finansal tabloda yok; açıklanmış dipnot/rapor bilgisi gerekir. Genel panelde hazır tedarik matrisi beklenmez; satış ülkesi yerine kullanılamaz.

**C07 · P1 — Enerji / emtia üretici-tüketici rolü**

- Ham alanlar: `commodity_role`, `energy_cost_share_optional`.
- İlk temsil: Kaynaklı rol kategorisi; maliyet payı varsa ayrı. İlgili hedefler: T01, T02, T03, T04.
- Kaynak: KAP aynı tarihte yayımlanmış yıllık/ara dönem raporu, dipnot ve faaliyet raporu; şirket yatırımcı ilişkileri asıl raporu.
- Engeller/kontrol: Kaynaklı üretici/tüketici/karma rolü ve varsa enerji maliyet payı çıkarılmamış; sektör etiketinden oran uydurulmaz. Sektör kategorisi gerçek enerji maliyet oranı değildir; korunma ve ürün karması etkiyi değiştirebilir.
- Bağımlılıklar: C01; politika: `all`.

**C08 · P2 — Sözleşme fiyatlama yapısı**

- Ham alanlar: `fixed_price_share`, `indexed_price_share`, `contract_currency`.
- İlk temsil: Kaynakta açıklanan şartlar ve varsa paylar. İlgili hedefler: T01, T02, T03, T04, T07.
- Kaynak: KAP aynı tarihte yayımlanmış yıllık/ara dönem raporu, dipnot ve faaliyet raporu; şirket yatırımcı ilişkileri asıl raporu.
- Engeller/kontrol: Sabit/endeksli fiyat payı ve sözleşme para birimi çoğu tabloda yok; açıklanmayan ticari şartlar eksik kalır. Fiyatlama gücü doğrudan gözlenmeyebilir; marj geçmişi bunun kesin ölçüsü değildir.

**C09 · P1 — Sipariş ve ifa görünürlüğü**

- Ham alanlar: `order_intake`, `backlog`, `book_to_bill`, `performance_schedule`.
- İlk temsil: Backlog/TTM satış; book-to-bill=yeni sipariş_q/satış_q; ifa aralığı. İlgili hedefler: T01, T03, T07, T08, T15.
- Kaynak: KAP aynı tarihte yayımlanmış yıllık/ara dönem raporu, dipnot ve faaliyet raporu; şirket yatırımcı ilişkileri asıl raporu.
- Engeller/kontrol: Yeni sipariş, bakiye sipariş ve ifa aralığı aynı ölçüm temelinde çıkarılmamış; KAP yeni iş bildirimi toplam sipariş evreni değildir. Bakiye ve TTM satış aynı para/ölçüm temelinde olmalı; book-to-bill pay ve paydası aynı çeyreğe ait olmalı. İmza anında otomatik gelir yok; bildirimler bütün siparişleri kapsamayabilir.
- Bağımlılıklar: F02; politika: `all`.

**C10 · P1 — Üretim kapasitesi, hacim ve birim fiyat**

- Ham alanlar: `capacity_utilization`, `sales_volume`, `unit_price`, `capacity_expansion`.
- İlk temsil: Sektöre uygun açıklanmış hacim/kapasite; büyüme. İlgili hedefler: T01, T02, T03, T10, T16.
- Kaynak: KAP aynı tarihte yayımlanmış yıllık/ara dönem raporu, dipnot ve faaliyet raporu; şirket yatırımcı ilişkileri asıl raporu.
- Engeller/kontrol: Sektöre özgü hacim, kapasite ve birim fiyat şirket raporundan alınmalı; birimler ve kapasite değişim tarihi farklıdır. Şirketler arasında ölçü birimleri farklıdır; talep kapasite doluyken hemen satışa dönüşmeyebilir.

### Olay bağlamı

**E01 · P2 — Olay türü, coğrafyası ve ekonomik kanalı**

- Ham alanlar: `event_type`, `affected_geography`, `affected_products`, `event_first_known_at`.
- İlk temsil: Önceden tanımlı etiketler; kaynak ve ilk açıklama zamanı. İlgili hedefler: T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13, T14, T15, T16, T17.
- Kaynak: KAP olay bildirimleri ve olayın resmi ilk duyuru kaynağı; ayrı kaynaklı olay envanteri.
- Engeller/kontrol: Olay/profil veri altyapısı yok; GPR tek başına olay türü, ürün ve coğrafya etiketi sağlamaz. İlk bilinen tarih gerekir. GPR tek başına olayın bütün ayrıntısını içermez. Haber/LLM toplama ayrı iş; sonradan bilinen sonuç etiketlenmez.

### Etkileşimler

**X01 · P1 — Kur × net döviz pozisyonu**

- Ham alanlar: `fx_change_x_net_fx_position`.
- İlk temsil: Uygun para birimi değişimi × önceki net FX/aktif. İlgili hedefler: T05, T07, T08, T12.
- Kaynak: Yeni bağımsız kaynak yok; aşağıdaki bağımlılıkların zaman ve kapsam açısından doğrulanmış gözlemlerinden hesaplanır.
- Engeller/kontrol: Eski çıkarıcı üretmiyor; gerekli bileşenlerden biri eksikse çarpım da eksik kalmalı, sıfır üretilmemeli. Toplam net pozisyon ile tek kur yalnız vekildir; işaret dayatılmaz.
- Bağımlılıklar: M01, M02, F19, F01; politika: `channel_specific`.

**X02 · P0 — Faiz × finansal borçluluk**

- Ham alanlar: `rate_change_x_financial_leverage`.
- İlk temsil: Faiz değişimi × önceki finansal borç/aktif. İlgili hedefler: T05, T07, T12, T17.
- Kaynak: Yeni bağımsız kaynak yok; aşağıdaki bağımlılıkların zaman ve kapsam açısından doğrulanmış gözlemlerinden hesaplanır.
- Engeller/kontrol: Eski CSV’de sütun var; eşleştirilen bileşenler hedef dönemin finansalı/güncel revize makrosu olduğu için hazır tahmin girdisi değildir. Toplam borç ilk vekildir; değişken faizli borç varsa ayrı geliştirilir; bileşenleri de modelde tut.
- Bağımlılıklar: M03, F13, F01; politika: `all`.

**X03 · P0 — Finansal stres × kısa vadeli borç**

- Ham alanlar: `fsi_x_short_term_debt`.
- İlk temsil: OFR FSI × önceki kısa vadeli finansal borç/aktif. İlgili hedefler: T05, T08, T12, T17.
- Kaynak: Yeni bağımsız kaynak yok; aşağıdaki bağımlılıkların zaman ve kapsam açısından doğrulanmış gözlemlerinden hesaplanır.
- Engeller/kontrol: Eski CSV’de sütun var; eşleştirilen bileşenler hedef dönemin finansalı/güncel revize makrosu olduğu için hazır tahmin girdisi değildir. Vade/likidite profili eksikse sıfır sayılmaz; risk artışı otomatik sonuç etiketi olmaz.
- Bağımlılıklar: R03, F13, F01; politika: `all`.

**X04 · P1 — Jeopolitik risk × faaliyet karması**

- Ham alanlar: `gpr_x_activity_share`.
- İlk temsil: GPR × açıklanmış faaliyet payları; tehdit/eylem ayrımı ayrı deney. İlgili hedefler: T01, T02, T03, T04, T07.
- Kaynak: Yeni bağımsız kaynak yok; aşağıdaki bağımlılıkların zaman ve kapsam açısından doğrulanmış gözlemlerinden hesaplanır.
- Engeller/kontrol: Eski çıkarıcı üretmiyor; gerekli bileşenlerden biri eksikse çarpım da eksik kalmalı, sıfır üretilmemeli. Savunma gibi bir faaliyet için etki zorla pozitif yapılmaz; kategoriyle etkileşim ayrıca açık vekil olarak denenebilir.
- Bağımlılıklar: R01, C02; politika: `all`.

**X05 · P1 — Coğrafi satış ağırlıklı ülke riski**

- Ham alanlar: `sales_weighted_country_gpr`.
- İlk temsil: Toplam: bilinen satış payı × normalize ülke GPR. İlgili hedefler: T01, T04, T07, T09.
- Kaynak: Yeni bağımsız kaynak yok; aşağıdaki bağımlılıkların zaman ve kapsam açısından doğrulanmış gözlemlerinden hesaplanır.
- Engeller/kontrol: Eski çıkarıcı üretmiyor; gerekli bileşenlerden biri eksikse çarpım da eksik kalmalı, sıfır üretilmemeli. Eksik ülke payı yeniden 1’e normalize edilerek kapsama gizlenmez; bu tedarik riski değildir.
- Bağımlılıklar: R01, C04; politika: `all`.

**X06 · P1 — Emtia × üretici/tüketici profili**

- Ham alanlar: `commodity_change_x_business_role`.
- İlk temsil: Emtia değişimi × rol/pay; güvenilir maliyet payı varsa ayrıca. İlgili hedefler: T01, T02, T03, T04, T10.
- Kaynak: Yeni bağımsız kaynak yok; aşağıdaki bağımlılıkların zaman ve kapsam açısından doğrulanmış gözlemlerinden hesaplanır.
- Engeller/kontrol: Eski çıkarıcı üretmiyor; gerekli bileşenlerden biri eksikse çarpım da eksik kalmalı, sıfır üretilmemeli. Aynı emtia artışı iki rolde farklı ilişki kurabilir; işaret ve gecikme öğrenilir.
- Bağımlılıklar: M07, C07; politika: `all`.

**X07 · P1 — Kur × ihracat / yurtdışı satış**

- Ham alanlar: `fx_change_x_export_share`, `fx_change_x_foreign_revenue_share`.
- İlk temsil: İki farklı payla ayrı etkileşimler. İlgili hedefler: T01, T03, T07, T09.
- Kaynak: Yeni bağımsız kaynak yok; aşağıdaki bağımlılıkların zaman ve kapsam açısından doğrulanmış gözlemlerinden hesaplanır.
- Engeller/kontrol: Eski çıkarıcı üretmiyor; gerekli bileşenlerden biri eksikse çarpım da eksik kalmalı, sıfır üretilmemeli. İhracat payı net kur kazancı değildir; ithal maliyet ve korunma başka kanallar.
- Bağımlılıklar: M01, M02, C03; politika: `channel_specific`.

**X08 · P2 — Olay bağlamı × ilgili şirket profili**

- Ham alanlar: `event_x_business_geography_supply`.
- İlk temsil: Önceden seçilmiş az sayıda olay/profil etkileşimi. İlgili hedefler: T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13, T14, T15, T16, T17.
- Kaynak: Yeni bağımsız kaynak yok; aşağıdaki bağımlılıkların zaman ve kapsam açısından doğrulanmış gözlemlerinden hesaplanır.
- Engeller/kontrol: Eski çıkarıcı üretmiyor; gerekli bileşenlerden biri eksikse çarpım da eksik kalmalı, sıfır üretilmemeli. Tam çapraz çarpım veya olaydan sonra kazanan etiketi yok; kaynaklı bağ ve zaman gerekir.
- Bağımlılıklar: E01, C02, C04, C06; politika: `channel_specific`.

## Toplama ve teslim sırası

1. **Ham kaynak envanteri:** Mevcut 30 şirket × 44 çeyrek korunur; her dosyanın özeti ve kaynak kimliği kaydedilir. Bu kapsam güncel bütün BIST için kapsama kanıtı değildir. Yeni indirme, eski dosyanın kaynağını veya bildirim sürümünü değiştirmeden arşivlenir.
2. **Çekirdek finansal doğrulama:** T01–T17 ve F01–F14 ham alanları; bilanço eşitliği, gelir tablosu uzlaşması, birim, çeyrek/YTD ve kaynak sürümü kontrolü. Şüpheli tutar komşu çeyreğe bakılarak otomatik çarpılmaz.
3. **Makro ve risk:** Gerçek seri kimliği ve yayım metaverisi; ticari kredi faizinin başka faizle ikame edilmemesi; günlük ve aylık gözlemlerin yayın anına göre bağlanması. Erişim anahtarı veya tarihsel sürüm yoksa değer uydurulmaz, eksiklik raporlanır.
4. **Şirket profili:** Yıllık ve ara dönem kaynaklardan F15–F20, C01–C10; tek tek kaynak sayfası/dipnot, kapsam ve geçerlilik aralığı. Önce farklı faaliyetlerden küçük doğrulama pilotu yapılır. Yeni yıllık profil geçmişe taşınmaz.
5. **Olay ve etkileşim:** E01 kaynak envanteri; X01–X08 yalnız bileşenlerinin tarihsel kullanılabilirliği doğrulandıktan sonra. İlk etkileşim bütçesi sözlükte 3–5 aileyle sınırlı; tamamı modele zorunlu değil.
6. **Tekrar üretilebilir teslim:** Tek kanonik finansal CSV; ayrı uzun biçimli kaynak/gözlem tablosu; aile bazında ham alan ve tarihsel kullanılabilirlik kapsaması; karantina/sorun listesi; bağımsız denetim çıktısı. `rebuild` çıktısı ile eski CSV’ler karşılaştırılır. Eğitim hazır kararı ancak bilgi kesimlerine göre hazırlanmış veri ve kalite kontrolleri geçince verilir.

## Gözlem şeması

Sözlükte istenen alanlar: `feature_id`, `entity_id`, `observation_period`, `first_published_at`, `available_at`, `vintage`, `value_and_unit`, `period_type`, `consolidation`, `price_level_date`, `source_document_id_url`, `page_or_note`, `coverage_ratio`, `age_days`, `is_proxy`, `missing_reason`, `extraction_method_reviewer`.

CSV’de pratik kullanım için `value` ve `unit`, ayrıca `source_document_id` ve `source_url` ayrı sütunlar olabilir; bu ayrım anlamı değiştirmez. Türetilen her değerde bileşen kayıtları/kimlikleri izlenebilmeli. Kaynak dosyası veya takvim bilinmiyorsa alanın boş olması açık eksikliktir; yapay tarih yazılarak tamamlanmış sayılmaz.
