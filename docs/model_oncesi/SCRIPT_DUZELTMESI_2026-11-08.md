# Script hata düzeltmesi — 8 Kasım 2026

Önceki PR sürümü: `67a250cbc55e03c92aad9a6119b5dfe2aae34acf`.

## Doğrulanan hatalar

1. Gelir tablosunda cari YTD boş olduğunda dolu cari üç aylık değerler atlanıyordu. Sütunlar bağımsız okunuyor. İlk çeyreğin üç aylık değeri hem ilk çeyrek hem de aynı kapsamdaki ikinci çeyrek farkı için kullanılabiliyor.
2. Eski raporlardaki bazı nihai nakit akışı toplamlarının satır adları tanınmıyordu. Kaynakta doğrulanan adlar eklendi. ARCLK gibi bazı kayıtlarda ara toplamın yerine nihai toplam alındı.
3. Vergi öncesi kâr, geniş etiket eşlemesi nedeniyle vergi gideri olarak okunuyordu. Hariç tutuldu. Ana vergi toplamı boşsa yalnız hem dönem vergisi hem ertelenmiş vergi açıkça raporlandığında toplam hesaplanıyor.

## Yeniden üretim sonucu

| Sütun | Önce eksik | Sonra eksik |
|---|---:|---:|
| T01_hasilat_ceyrek | 8 | 2 |
| T07_donem_net_kari_ceyrek | 8 | 2 |
| T15_isletme_nakit_akisi_ceyrek | 101 | 56 |
| T06_vergi_gideri_geliri_ceyrek | 8 | 24 |

1.320 satır, 205 sütun. Kaynak kalite uyarısı: 15. Denetim: 22/22. Python: 28 test geçti; PHP: 37 bağımsız kontrol ve sözdizimi kontrolü geçti.

Konsolide/solo kapsam kontrolleri korunmuştur. Hasılat ve net kârda kalan iki çeyrek, CEMTS 2011Q4 ve NETAS 2011Q4 için önceki çeyreğin farklı rapor kapsamından gelmesiyle ilgilidir. Eksik bileşenler sıfır sayılmadı. Bütün değişkenlerin tamamlandığı veya verinin model eğitimine hazır olduğu iddia edilmez.

Kanonik CSV SHA256: `c8846a42cfcc729c2b8034f3bb4970e3e4875737596c22e49bbbdbd871920251`.
