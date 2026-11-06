# Forma: 78 kalemin tamamı

Kaynak: [hesap haritası](https://github.com/forma-lab-mccombs/forma-release/blob/main/src/forma/metadata/account_id_map.csv), [makale Ek A.3](https://arxiv.org/html/2608.11327v1).

Etkin hedef evreni [pf_full yapılandırmasından](https://github.com/forma-lab-mccombs/forma-release/blob/main/configs/feature_sets.yaml) doğrulandı. Embedding haritası 82 ad içerir; `scale`, `dvcq`, `dvpq`, `neiq` kanonik 78 hedefe dahil değildir. `scale`, bugünkü şirket büyüklüğünü taşıyan ek girdi olarak kullanılır; gelecekte tahmin edilen hesap değildir.
Her kalemin geçmişi girdi, gelecekteki değeri hedef olabilir. Nakit akışının kümülatif raporlandığı kaynaklar tek çeyreğe çevrilir. Türkçe adlar bu araştırmanın açıklayıcı karşılıklarıdır; bire bir TFRS etiket eşlemesi değildir.

| Kod | Türkçe anlamı |
|---|---|
| `acomincq` | Birikmiş diğer kapsamlı gelir/gider |
| `acoq` | Diğer dönen varlıklar |
| `actq` | Toplam dönen varlıklar |
| `ancq` | Toplam duran varlıklar |
| `aoq` | Diğer varlıklar |
| `aoq_ex_intanq` | Maddi olmayan varlıklar hariç diğer varlıklar |
| `apq` | Ticari borçlar |
| `aqcq` | Şirket satın alma harcaması |
| `atq` | Toplam aktifler |
| `capsq` | Sermaye yedekleri / ihraç primleri |
| `capxq` | Yatırım harcamaları |
| `ceqq` | Adi hissedarlara ait özkaynak |
| `cheq` | Nakit ve kısa vadeli yatırımlar |
| `cogsq` | Satışların maliyeti |
| `cstkq` | Adi hisse sermayesi |
| `dlcchq` | Kısa vadeli borç değişimi |
| `dlcq` | Kısa vadeli yükümlülüklerdeki finansal borç |
| `dltisq` | Yeni uzun vadeli borçlanma |
| `dltrq` | Uzun vadeli borç geri ödemesi |
| `dlttq` | Uzun vadeli finansal borç |
| `dpactq` | Birikmiş amortisman, itfa ve tükenme payı |
| `dpq` | Amortisman ve itfa gideri |
| `drcq` | Kısa vadeli ertelenmiş gelir |
| `drltq` | Uzun vadeli ertelenmiş gelir |
| `dvq` | Nakit temettüler |
| `exreq` | Kur değişiminin nakit üzerindeki etkisi |
| `fcfq` | Serbest nakit akışı: CFO eksi yatırım harcaması |
| `fiaoq` | Diğer finansman faaliyetleri |
| `fincfq` | Finansman faaliyetlerinden net nakit akışı |
| `fopoq` | Faaliyet fonlarında diğer kalemler |
| `gdwlq` | Net şerefiye |
| `gpq` | Brüt kâr: gelir eksi satış maliyeti |
| `ibq` | Olağanüstü kalem öncesi kâr |
| `intanoq` | Diğer maddi olmayan duran varlıklar |
| `intanq` | Toplam maddi olmayan duran varlıklar |
| `invtq` | Toplam stoklar |
| `ivacoq` | Diğer yatırım faaliyetleri |
| `ivchq` | Yatırımlardaki artış |
| `ivncfq` | Yatırım faaliyetlerinden net nakit akışı |
| `ivstchq` | Kısa vadeli yatırımlardaki değişim |
| `lcoq` | Diğer kısa vadeli yükümlülükler |
| `lctq` | Toplam kısa vadeli yükümlülükler |
| `loq` | Diğer yükümlülükler |
| `loq_ex_dr` | Ertelenmiş gelir hariç diğer yükümlülükler |
| `ltq` | Toplam yükümlülükler |
| `mibtq` | Finansal durum tablosunda kontrol gücü olmayan paylar |
| `miiq` | Kâr hesabında kontrol gücü olmayan paylar |
| `niq` | Net kâr |
| `nopiq` | Faaliyet dışı gelir |
| `oancfq` | İşletme faaliyetlerinden net nakit akışı |
| `oiadpq` | Amortisman sonrası faaliyet kârı / EBIT |
| `oibdpq` | Amortisman öncesi faaliyet kârı / EBITDA |
| `piq` | Vergi öncesi kâr |
| `ppegtq` | Brüt maddi duran varlıklar |
| `ppentq` | Net maddi duran varlıklar |
| `prstkcq` | Adi ve imtiyazlı hisse geri alımı |
| `pstkq` | Toplam imtiyazlı hisse sermayesi |
| `rectq` | Toplam alacaklar |
| `req` | Birikmiş / dağıtılmamış kârlar |
| `revtq` | Toplam gelir |
| `seqq` | Toplam hissedar özkaynağı |
| `sivq` | Yatırımların satışı |
| `spiq` | Özel / istisnai kalemler |
| `sppeq` | Maddi duran varlık satışından nakit girişi |
| `sstkq` | Adi ve imtiyazlı hisse ihracı |
| `stkcoq` | Hisse bazlı ücret gideri |
| `tstkq` | Geri alınmış hisse sermayesi |
| `txbcofq` | Hisse opsiyonlarının vergi faydası |
| `txditcq` | Ertelenmiş vergi ve yatırım vergi kredisi |
| `txpq` | Ödenecek gelir vergisi |
| `txtq` | Toplam gelir vergisi gideri |
| `wcapq` | Çalışma sermayesi: dönen varlık eksi kısa yükümlülük |
| `xidoq` | Olağanüstü kalemler ve durdurulan faaliyetler |
| `xintq` | Faiz ve ilişkili giderler |
| `xoprq` | Toplam faaliyet giderleri |
| `xrdq` | Ar-Ge gideri |
| `xsgaq` | Satış/genel/idari gider |
| `xsgaq_ex_rd` | Ar-Ge hariç satış/genel/idari gider |
