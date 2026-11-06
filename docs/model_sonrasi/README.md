# Model sonrası: ürün, tahmin ve işletim

Bu çalışma alanı, [geliştirme/eğitim tarafının](../model_oncesi/README.md) hazırladığı model paketini kullanıcıya hizmet veren sisteme dönüştürür. Site, API, veri yenileme, yeni tahmin, rapor saklama ve model performansının izlenmesi burada yer alır.

## Yapılacak işler

1. Hisse kataloğu, arama ve şirket sayfasını sunmak.
2. İlk talepte eksik veriyi arka planda hazırlamak; hazır raporu kalıcı kayıttan göstermek.
3. Yeni finansal/makro veriyi almak ve modelin sabit girdi sözleşmesine göre işlemek.
4. Mevcut model sürümüyle yeni tahmin ve rapor üretmek.
5. Zamanlayıcı, iş kuyruğu, tekrar deneme ve sürüm takibini yürütmek.
6. Gerçek sonuçlar açıklanınca eski tahminin hatasını ölçmek; gerekirse yeni model adayı için eğitim tarafına geri beslemek.

## Belgeler

| Belge | Kullanımı |
|---|---|
| [İstenilen Hedef](ISTENILEN_HEDEF.md) | Ürün amacı, kullanıcı akışı ve temel gereksinimler |
| [Sistem Mimarisi](SISTEM_MIMARISI.md) | İlk talep, kalıcı rapor, arka plan çalışanı ve artımlı güncelleme |
| [Model Yaşam Döngüsü](MODEL_YASAM_DONGUSU.md) | Yeni veriyle tahmin, performans izleme, yeniden eğitim ve sürüm geçişi |

## Yeni veriye uyarlama ne demek?

| Durum | İşlem |
|---|---|
| Yeni kur/risk değeri veya finansal rapor geldi | Uyumlu yeni girdiyi hazır modelden geçirip yeni tahmin üret. |
| Tahmin edilen dönem gerçekleşti | Eski tahmini koru; gerçekleşenle karşılaştır ve sonraki hedefi belirle. |
| Girdi ilişkileri değişiyor veya hata artıyor | Veriyi ve performansı incele; gerekiyorsa eğitim tarafında aday model hazırla. |
| Kullanılan girdi tanımı veya model mimarisi değişecek | Yeni sürümü geliştirme/eğitim tarafında doğrula; sonra kullanıma al. |

İlk satır mevcut modelle **tahmin üretmektir**. Son iki satır yeni model geliştirme/yeniden eğitim sürecine bağlanır. Veri yenileme, rapor yenileme ve model eğitimi farklı takvimlerde çalışabilir.

Şirketler arası olay/maruziyet farkları için [ortak değişken listesi](../model_oncesi/DEGISKEN_LISTESI.md) ve [kayıtlar](../model_oncesi/degiskenler.json) kullanılır. Listeye yeni aday eklemek aktif modelin girdi şemasını kendiliğinden değiştirmez.
