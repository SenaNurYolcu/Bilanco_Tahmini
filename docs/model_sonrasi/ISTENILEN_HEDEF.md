# İstenilen hedef

Tarih: **6 Kasım 2026**. Bu belge kullanıcının tarif ettiği ürün deneyimini kaydeder. Çalışan uygulama veya eğitilmiş model bulunduğu anlamına gelmez. Mimari değerlendirme ve öneri [Sistem mimarisi](SISTEM_MIMARISI.md) belgesindedir.

Çalışma alanı: [model sonrası / ürün ve işletim](README.md). Bu ürüne verilecek modelin araştırma, eğitim ve doğrulaması [model öncesi](../model_oncesi/README.md) çalışma alanındadır.

## 1. Ürünün amacı

Kullanıcı bir web sitesine girer; Türkiye'de borsada listelenmiş hisseleri şirket adı, hisse kodu ve uygun etiketlerle bulur. Bir hisseyi seçtiğinde şirketin finansal verilerini ve henüz açıklanmamış dönem için üretilmiş finansal tahmin raporunu görür.

Tahmin kapsamı gelir tablosu, bilanço ve nakit akışının seçilmiş ana kalemleridir. Girdiler için [yaşayan değişken listesi](../model_oncesi/DEGISKEN_LISTESI.md) kullanılır. Şirketin sektör/faaliyet, coğrafya, finansman ve diğer maruziyet özellikleri ortak ekonomik olaylarla birlikte değerlendirilebilir.

## 2. Kullanıcının istediği temel deneyim

| ID | Gereksinim |
|---|---|
| H01 | Listelenmiş hisselerden oluşan bir katalog ve arama alanı bulunur. |
| H02 | Kodun yanında şirket adı/kısaltmasıyla da arama yapılabilir. Örneğin “THY” araması Türk Hava Yolları / THYAO sonucuna ulaşır. |
| H03 | Şirketin detaylı verisi henüz alınmamışsa ilk hazırlık işlemi başlatılabilir. |
| H04 | Veri ve rapor hazır olunca şirket sayfasından görüntülenebilir. |
| H05 | Hazırlanmış veri ve rapor sistem tarafında kalıcı olarak saklanır. |
| H06 | Sonraki ziyaretlerde hazır sonuç yeniden veri toplama ve tahmin işlemi beklenmeden gösterilir. |
| H07 | Veriler ve raporlar zaman içinde güncellenebilir. |
| H08 | İlk talepte hazırlama ve bütün hisseleri düzenli tarama seçenekleri mimari açıdan karşılaştırılır. |

“Tag” ifadesi bu taslakta hisse kodu ile arama/filtre etiketleri olarak ayrılır: **THYAO** bir hisse kodu; havacılık gibi ifadeler faaliyet etiketidir. Kesin etiket sözlüğü daha sonra belirlenebilir. THYAO eşlemesinin birincil kaynağı [şirketin yatırımcı ilişkileri sayfasıdır](https://investor.turkishairlines.com/tr/hisse-bilgileri/hisse-bilgileri).

## 3. Kullanıcının tarif ettiği iki seçenek

### A — İlk talepte hazırlama

1. Kullanıcı hisseyi arar ve seçer.
2. Sistem mevcut veri/rapor durumuna bakar.
3. İlk hazırlık gerekiyorsa veriler alınır, işlenir ve rapor üretilir.
4. Sonuç kalıcı olarak saklanır.
5. Daha sonraki ziyaretler saklanan sonucu gösterir.

Avantajı, ilk etapta talep gören hisselere kaynak ayırmasıdır. İlk ziyaret beklemesi ve zamanla eskiyen sonuçlar için çözüm gerekir.

### B — Düzenli toplu hazırlama

1. Sistem katalogdaki hisseleri belirli aralıklarla tarar; başlangıç fikri haftada birdir.
2. Gerekli veri ve rapor işlemleri hisseler bazında yürütülür.
3. Kullanıcı geldiğinde önceden hazırlanmış sonuçları görür.

Avantajı daha geniş hazır kapsama sağlamasıdır. Kullanılmayan hisseler için işlem maliyeti ve iki tarama arasındaki eskime değerlendirilmelidir. “Her hafta bütün geçmişi baştan indirmek” bu seçeneğin zorunlu bir parçası değildir; değişen verileri almak mümkündür.

## 4. Önerilen kullanıcı akışı

Bu bölüm kullanıcının iki fikrinden türetilen **mimari öneridir**:

- Hisse kataloğu baştan hazırdır; detaylı finansal verinin tamamının baştan indirilmiş olması gerekmez.
- Hisse seçildiğinde hazır rapor varsa gösterilir.
- Hazır rapor yoksa şirket için arka plan hazırlık işi oluşturulur; kullanıcı durumu görür.
- Aynı şirket için zaten işlem varsa yeni ziyaretçi aynı işlem durumunu takip eder.
- Daha sonra düzenli taramalar eksik/eski veriyi günceller; yeni rapor başarıyla tamamlanınca görünür sürüm değiştirilir.

Her hisse için ayrı bir web uygulaması kurulması gerekmez. **Tek web sitesi ve ortak şirket sayfası şablonu**, seçilen şirketin kayıtlarını gösterir. Şirket kataloğu, verinin hazır olması ve tahmin desteği ayrı durumlar olarak saklanır.

## 5. Sayfada anlaşılır biçimde gösterilecek bilgiler

- Şirket adı, hisse kodu ve faaliyet etiketleri.
- Geçmişte açıklanmış finansal sonuçlar ile geleceğe ilişkin tahminlerin ayrımı.
- Tahmin edilen mali dönem ve kullanılan bilginin tarihi.
- Raporun hazırlanma tarihi ve en son veri kontrol tarihi.
- Hazırlık sürüyorsa durum bilgisi.
- Yeni rapor hazırlanırken mevcut başarılı rapor varsa onun tarihiyle birlikte görüntülenmesi.
- Yetersiz veri veya henüz desteklenmeyen raporlama şeması varsa anlaşılır durum mesajı.

Kullanıcıya gerçekleşmemiş süre yüzdeleri veya kesin tamamlanma zamanı gösterilmez. Gerçek ölçüm yoksa “sırada / veri hazırlanıyor / tahmin hazırlanıyor” gibi durumlar kullanılır.

## 6. Katalog ve model kapsamı

**Ürün hedefi bütün listelenmiş hisselerin katalogda bulunmasıdır.** İlk araştırma sürümünün bütün sektörlerde doğrulanmış tahmin üretebilmesi ayrı bir aşamadır. Mevcut değişken sözlüğü finans dışı şirketler için tasarlanmıştır; bankalar ve sigortalar farklı tablo/model şemaları gerektirir.

Katalogda bulunmak, veri hazır olmak ve tahmin modelince desteklenmek aynı anlama gelmez. İlk sürümde kapsamı dar bir model kullanılırsa diğer hisseler katalogdan kaybolmaz; tahmin desteğinin durumu doğru gösterilir. Bu geçiş yaklaşımı tam katalog hedefini değiştirmez.

## 7. Başarı ölçütleri

1. Aynı hisseyi ikinci kez açmak dış veri kaynağından yeniden hazırlık işlemi bekletmez.
2. Bir hisseye aynı anda gelen ziyaretler aynı hazırlık işini paylaşabilir.
3. Uygulama yeniden başlasa da başarılı raporlar korunur.
4. Güncelleme başarısız olduğunda önceki başarılı rapor kaybolmaz.
5. Yeni raporda bilgi tarihi, model ve veri sürümü izlenebilir.
6. Yayınlanmış sonuç, tahmin diye sunulmaz; hedef dönem gerçekleşince eski tahmin arşivlenip gerçekleşenle karşılaştırılabilir.
7. Yeni hisse, isim/kod değişimi ve kapsam değişiklikleri katalog güncellemesiyle yönetilebilir.

## 8. İlgili belgeler

- [Önerilen sistem mimarisi](SISTEM_MIMARISI.md)
- [Yeni veri ve model yaşam döngüsü](MODEL_YASAM_DONGUSU.md)
- [Güncellenebilir değişken listesi](../model_oncesi/DEGISKEN_LISTESI.md)
- [Değişken kayıtları](../model_oncesi/degiskenler.json)
- [Araştırma projesi önerisi](../model_oncesi/arastirma/2026-11-06-bilanco-tahmini/ARASTIRMA_PROJESI_ONERISI.md)
