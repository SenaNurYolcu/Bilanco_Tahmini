# Öğretim üyesinin önerdiği makale ve projeye katkısı

Kaynak: Necip Bulut, Saber Shakeri, Seçil Yüzük ve Mehmet S. Aktaş (2019), **Öznitelik Çıkarım Yöntemleri ve Makine Öğrenmesi Kullanarak Şirket Bilanço Verilerine Dayalı İflas Riski Tahmini**, TBV Bilgisayar Bilimleri ve Mühendisliği Dergisi, 12(2), 20–29. [Resmî PDF](https://dergipark.org.tr/tr/download/article-file/885999); yerel kaynak `885999.pdf`.

## Çalışmanın kapsamı

Makale, gelecek çeyreğin finansal tutarlarını değil iflas riski sınıfını inceler. Etiketler gözlenmiş iflas olayları yerine ağırlıkla Ohlson skorundan üretilir; metin Altman etiketlemesinden de söz eder. Dolayısıyla skor etiketini ayırt etme başarısı, gerçek gelecek iflasını öngörme başarısı değildir.

Yazarlar 150 BIST şirketinin 2000–2018 çeyreklik verilerini, 297 kalemlik ham havuzu; ikinci deneyde 230 öznitelik ve 10.800 bilanço kaydını bildirir. İlk deney sekiz şirkette 739 kayıt kullanır. Boyut azaltmada PCA ve bilgi kazancı, ardından LDA; sınıflandırmada lojistik regresyon, rassal orman ve SVM denenir. İlk deneyde beş katlı çapraz doğrulama, ikinci deneyde %80/%20 ayırma açıklanır. Takvim sırasına göre ayrılmış bağımsız gelecek dönem testi açıkça kurulmaz. Ayrıntılar PDF s.5–9, basılı s.24–28; tablo ve değişken listesi görsel olarak da kontrol edildi.

## Bizim veri toplama işine uygulama

Bu proje için çıkarımımız: geniş ham kalem havuzu kaynaklarıyla saklanmalı, kullanılacak az sayıdaki değişken eğitim dönemi içinde seçilmelidir. Ham dosyalardaki bütün mevcut satırlar bu nedenle `financial_source_rows.csv` içinde korunur. Makalenin öne çıkardığı kalemler için aşağıdaki ek ham eşlemeler yapıldı. Bunlar otomatik seçilmiş veya performansı kanıtlanmış model girdileri değildir.

| Makaledeki kalem | Bizim çıktıdaki karşılık / durum |
|---|---|
| Uzun vadeli yükümlülükler | `uzun_vadeli_yukumlulukler` |
| Ertelenen vergi varlığı | `paper2019_ertelenmis_vergi_varliklari` |
| Ana ortaklık dışı özsermaye | `paper2019_kontrol_gucu_olmayan_paylar`; toplam özkaynakla doldurulmaz |
| Diğer faaliyet zarar/giderleri | `paper2019_diger_faaliyet_giderleri_ytd` |
| Net dönem kârı/zararı | `T07_donem_net_kari_ytd`; ana ortaklık kârı ayrıdır |
| Finansal duran varlıklar | `paper2019_finansal_duran_varliklar`; güncel finansal yatırım etiketine kör eşlenmez |
| Vergi öncesi kâr/zarar | `paper2019_vergi_oncesi_kar_ytd` |
| Ödenecek vergi/yasal yükümlülük | `paper2019_odenecek_vergi_yasal_yukumlulukler`; vergi gideri değildir |
| Kısa vadeli ticari alacak | `F10_kisa_vadeli_ticari_alacaklar` |
| Ticari borçlar | Kısa/uzun ayrı; toplam yalnız iki bileşen biliniyorsa |

Makalenin sınıflandırma skorlarını, eşiklerini ve doğruluk yüzdelerini bu projenin finansal tutar tahminine taşımıyoruz. Ohlson/Altman skoru ya da yeni bir iflas modeli bu çalışma kapsamında eklenmedi. PCA ileride yalnız eğitim diliminde öğrenilen bir alternatif olabilir; sınıf etiketine dayanan LDA regresyon problemine doğrudan uygulanmaz. SVM denemesi gerekirse regresyon karşılığı SVR ayrı değerlendirilir. İlk kıyaslar son bilinen değer ve geçen yılın aynı çeyreği; sonraki yöntemler aynı gelecek tarih bloklarında karşılaştırılmalıdır. Henüz model eğitilmedi.
