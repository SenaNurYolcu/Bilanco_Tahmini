# DeepEarnings: bütün finansal adaylar

Kaynaklar: [ölçeklenen alanlar](https://github.com/alexanderpei/DeepEarnings/blob/master/list_my_quarterly_features.txt), [diğer alanlar](https://github.com/alexanderpei/DeepEarnings/blob/master/list_my_quarterly_features_nonorm.txt).

Aşağıdaki 236 alan tanımlanmış aday listesidir. Kullanılan veride tümü eksik sütunlar sonradan düşer; nihai modelin 236 etkin özelliği olduğu iddia edilmiyor. Kodlar küçük harfe çevrilerek gösterildi.

`q` genellikle çeyrek/dönem sonu; `y` akım kalemlerinde çoğunlukla mali yıl başından itibaren kümülatif; `12` son 12 aylık ölçümdür. Birim, EPS/temettü oranı veya sermaye oranı gibi istisnalar dışında çoğunlukla para tutarıdır. Kaynak tanımı esas alınmalı; her q alanının üç aylık akım olduğu varsayılmamalı.

## 199 alan: önce piyasa değeriyle bölünenler

| Kod | Türkçe anlamı |
|---|---|
| `acomincq` | Birikmiş diğer kapsamlı gelir/gider |
| `acoq` | Diğer dönen varlıklar |
| `actq` | Toplam dönen varlıklar |
| `altoq` | Diğer uzun vadeli varlıklar |
| `amcy` | Nakit akışındaki itfa gideri; yıl başından birikimli gösterim |
| `ancq` | Toplam duran varlıklar |
| `aolochy` | Diğer varlık ve yükümlülüklerin net değişimi; yıl başından birikimli gösterim |
| `aoq` | Diğer varlıklar |
| `apq` | Ticari borçlar |
| `atq` | Toplam aktifler |
| `capsq` | Sermaye yedekleri / ihraç primleri |
| `capxy` | Yatırım harcamaları; yıl başından birikimli gösterim |
| `cdvcy` | Adi hisselere ödenen nakit temettü; yıl başından birikimli gösterim |
| `ceqq` | Adi hissedarlara ait özkaynak |
| `chechy` | Nakit ve nakit benzerlerindeki değişim; yıl başından birikimli gösterim |
| `cheq` | Nakit ve kısa vadeli yatırımlar |
| `chq` | Nakit |
| `cibegniq` | Kapsamlı gelir hesabının başlangıç net kârı |
| `cibegniy` | Kapsamlı gelir hesabının başlangıç net kârı; yıl başından birikimli gösterim |
| `cicurrq` | Kapsamlı gelirde döviz çevrim düzeltmesi |
| `cicurry` | Kapsamlı gelirde döviz çevrim düzeltmesi; yıl başından birikimli gösterim |
| `ciderglq` | Kapsamlı gelirde türev kazanç/kayıpları |
| `cidergly` | Kapsamlı gelirde türev kazanç/kayıpları; yıl başından birikimli gösterim |
| `cimiiq` | Kapsamlı gelirde kontrol gücü olmayan paylar |
| `cimiiy` | Kapsamlı gelirde kontrol gücü olmayan paylar; yıl başından birikimli gösterim |
| `ciotherq` | Kapsamlı gelirde diğer düzeltmeler |
| `ciothery` | Kapsamlı gelirde diğer düzeltmeler; yıl başından birikimli gösterim |
| `ciq` | Toplam kapsamlı gelir |
| `ciy` | Toplam kapsamlı gelir; yıl başından birikimli gösterim |
| `cisecglq` | Kapsamlı gelirde menkul kıymet kazanç/kayıpları |
| `cisecgly` | Kapsamlı gelirde menkul kıymet kazanç/kayıpları; yıl başından birikimli gösterim |
| `citotalq` | Ana ortaklığa ait kapsamlı gelir |
| `citotaly` | Ana ortaklığa ait kapsamlı gelir; yıl başından birikimli gösterim |
| `cogsq` | Satışların maliyeti |
| `cogsy` | Satışların maliyeti; yıl başından birikimli gösterim |
| `cshiq` | İhraç edilmiş adi hisse sayısı |
| `cshopq` | Çeyrekte geri alınan hisse sayısı |
| `cstkeq` | Adi hisse eşdeğerlerine ilişkin dolar cinsinden tasarruf |
| `cstkey` | Adi hisse eşdeğerlerine ilişkin dolar cinsinden tasarruf; yıl başından birikimli gösterim |
| `cstkq` | Adi hisse sermayesi |
| `dcomq` | Ertelenmiş ücret / çalışan tazminatı |
| `dd1q` | Bir yıl içinde ödenecek uzun vadeli borç |
| `depcy` | Nakit akışındaki amortisman ve tükenme payı; yıl başından birikimli gösterim |
| `deracq` | Kısa vadeli türev varlıklar |
| `deraltq` | Uzun vadeli türev varlıklar |
| `derhedglq` | Türev ve riskten korunma kazanç/kayıpları |
| `derhedgly` | Türev ve riskten korunma kazanç/kayıpları; yıl başından birikimli gösterim |
| `derlcq` | Kısa vadeli türev yükümlülükler |
| `derlltq` | Uzun vadeli türev yükümlülükler |
| `dlcchy` | Kısa vadeli borç değişimi; yıl başından birikimli gösterim |
| `dlcq` | Kısa vadeli yükümlülüklerdeki finansal borç |
| `dltisy` | Yeni uzun vadeli borçlanma; yıl başından birikimli gösterim |
| `dltry` | Uzun vadeli borç geri ödemesi; yıl başından birikimli gösterim |
| `dlttq` | Uzun vadeli finansal borç |
| `doq` | Durdurulan faaliyetler |
| `doy` | Durdurulan faaliyetler; yıl başından birikimli gösterim |
| `dpactq` | Birikmiş amortisman, itfa ve tükenme payı |
| `dpcy` | Nakit akışındaki amortisman ve itfa; yıl başından birikimli gösterim |
| `dpq` | Amortisman ve itfa gideri |
| `dpy` | Amortisman ve itfa gideri; yıl başından birikimli gösterim |
| `drcq` | Kısa vadeli ertelenmiş gelir |
| `drltq` | Uzun vadeli ertelenmiş gelir |
| `dteaq` | Borç kapatmanın vergi sonrası etkisi |
| `dteay` | Borç kapatmanın vergi sonrası etkisi; yıl başından birikimli gösterim |
| `dtedq` | Borç kapatmanın seyreltilmiş EPS etkisi |
| `dtedy` | Borç kapatmanın seyreltilmiş EPS etkisi; yıl başından birikimli gösterim |
| `dteepsq` | Borç kapatmanın temel EPS etkisi |
| `dteepsy` | Borç kapatmanın temel EPS etkisi; yıl başından birikimli gösterim |
| `dtepq` | Borç kapatmanın vergi öncesi etkisi |
| `dtepy` | Borç kapatmanın vergi öncesi etkisi; yıl başından birikimli gösterim |
| `dvintfq` | Alınacak temettü ve faiz |
| `dvpq` | İmtiyazlı hisse temettüsü |
| `dvpy` | İmtiyazlı hisse temettüsü; yıl başından birikimli gösterim |
| `dvpspq` | Ödeme tarihine göre hisse başına temettü |
| `dvpsxq` | Hak kullanım tarihine göre hisse başına temettü |
| `dvy` | Nakit temettüler; yıl başından birikimli gösterim |
| `esubcy` | Nakit akışında iştirak kâr/zarar payı; yıl başından birikimli gösterim |
| `esubq` | Konsolide edilmeyen iştiraklerin kâr payı |
| `esuby` | Konsolide edilmeyen iştiraklerin kâr payı; yıl başından birikimli gösterim |
| `ffoq` | GYO için faaliyetlerden yaratılan fon |
| `ffoy` | GYO için faaliyetlerden yaratılan fon; yıl başından birikimli gösterim |
| `fopty` | Faaliyetlerden yaratılan toplam fon; yıl başından birikimli gösterim |
| `fsrcty` | Toplam fon kaynakları; yıl başından birikimli gösterim |
| `fusety` | Toplam fon kullanımları; yıl başından birikimli gösterim |
| `gdwlamq` | Şerefiye itfası |
| `gdwlamy` | Şerefiye itfası; yıl başından birikimli gösterim |
| `gdwlq` | Net şerefiye |
| `ibadj12` | Adi hisse eşdeğerleri için düzeltilmiş olağanüstü kalem öncesi kâr; 12 aylık gösterim |
| `ibadjq` | Adi hisse eşdeğerleri için düzeltilmiş olağanüstü kalem öncesi kâr |
| `ibadjy` | Adi hisse eşdeğerleri için düzeltilmiş olağanüstü kalem öncesi kâr; yıl başından birikimli gösterim |
| `ibcomq` | Adi hissedarlara ait olağanüstü kalem öncesi kâr |
| `ibcomy` | Adi hissedarlara ait olağanüstü kalem öncesi kâr; yıl başından birikimli gösterim |
| `ibcy` | Nakit akışında olağanüstü kalem öncesi kâr; yıl başından birikimli gösterim |
| `ibmiiq` | Olağanüstü kalemler ve azınlık payı öncesi kâr |
| `ibmiiy` | Olağanüstü kalemler ve azınlık payı öncesi kâr; yıl başından birikimli gösterim |
| `ibq` | Olağanüstü kalem öncesi kâr |
| `iby` | Olağanüstü kalem öncesi kâr; yıl başından birikimli gösterim |
| `icaptq` | Toplam yatırılmış sermaye |
| `intaccq` | Tahakkuk etmiş faiz |
| `intanoq` | Diğer maddi olmayan duran varlıklar |
| `intanq` | Toplam maddi olmayan duran varlıklar |
| `intpny` | Net ödenen faiz; yıl başından birikimli gösterim |
| `invchy` | Stoklardaki azalış/artışın nakit etkisi; yıl başından birikimli gösterim |
| `invfgq` | Mamul stokları |
| `invoq` | Diğer stoklar |
| `invrmq` | Hammadde stokları |
| `invtq` | Toplam stoklar |
| `invwipq` | Yarı mamul / devam eden üretim stokları |
| `itccy` | Net yatırım vergi kredisi; yıl başından birikimli gösterim |
| `ivacoy` | Diğer yatırım faaliyetleri; yıl başından birikimli gösterim |
| `ivaeqq` | Özkaynak yatırımları ve avanslar |
| `ivaoq` | Diğer yatırımlar ve avanslar |
| `ivchy` | Yatırımlardaki artış; yıl başından birikimli gösterim |
| `ivltq` | Toplam uzun vadeli yatırımlar |
| `ivncfy` | Yatırım faaliyetlerinden net nakit akışı; yıl başından birikimli gösterim |
| `ivstchy` | Kısa vadeli yatırımlardaki değişim; yıl başından birikimli gösterim |
| `ivstq` | Toplam kısa vadeli yatırımlar |
| `lcoq` | Diğer kısa vadeli yükümlülükler |
| `lctq` | Toplam kısa vadeli yükümlülükler |
| `lltq` | Toplam uzun vadeli yükümlülükler |
| `mkvaltq` | Toplam piyasa değeri |
| `pncy` | Temel emeklilik düzeltmesi; yıl başından birikimli gösterim |
| `prstkccy` | Adi hisse geri alımı; yıl başından birikimli gösterim |
| `prstkcy` | Adi ve imtiyazlı hisse geri alımı; yıl başından birikimli gösterim |
| `prstkpcy` | İmtiyazlı hisse geri alımı; yıl başından birikimli gösterim |
| `pstknq` | Geri çağrılamayan imtiyazlı hisse sermayesi |
| `pstkq` | Toplam imtiyazlı hisse sermayesi |
| `rdipaq` | Devam eden Ar-Ge'nin vergi sonrası gider etkisi |
| `rdipay` | Devam eden Ar-Ge'nin vergi sonrası gider etkisi; yıl başından birikimli gösterim |
| `rdipdq` | Devam eden Ar-Ge'nin seyreltilmiş EPS etkisi |
| `rdipdy` | Devam eden Ar-Ge'nin seyreltilmiş EPS etkisi; yıl başından birikimli gösterim |
| `rdipepsq` | Devam eden Ar-Ge'nin temel EPS etkisi |
| `rdipepsy` | Devam eden Ar-Ge'nin temel EPS etkisi; yıl başından birikimli gösterim |
| `rdipq` | Devam eden Ar-Ge gideri |
| `rdipy` | Devam eden Ar-Ge gideri; yıl başından birikimli gösterim |
| `recchy` | Alacaklardaki azalış/artışın nakit etkisi; yıl başından birikimli gösterim |
| `recdq` | Şüpheli alacak tahmini |
| `rectaq` | Birikmiş diğer kapsamlı gelirde döviz çevrim düzeltmesi |
| `rectoq` | Vergi iadeleri dahil diğer kısa vadeli alacaklar |
| `rectq` | Toplam alacaklar |
| `rectrq` | Ticari alacaklar |
| `recubq` | Faturalanmamış alacaklar |
| `req` | Birikmiş / dağıtılmamış kârlar |
| `retq` | Toplam gayrimenkul varlığı |
| `reunaq` | Düzeltilmemiş dağıtılmamış kârlar |
| `revtq` | Toplam gelir |
| `revty` | Toplam gelir; yıl başından birikimli gösterim |
| `rllq` | Kredi / varlık zarar karşılığı |
| `rstcheltq` | Uzun vadeli kısıtlı nakit ve yatırımlar |
| `rstcheq` | Kısa vadeli kısıtlı nakit ve yatırımlar |
| `saleq` | Net satışlar |
| `saley` | Net satışlar; yıl başından birikimli gösterim |
| `scstkcy` | Adi hisse ihracından sağlanan nakit; yıl başından birikimli gösterim |
| `seqoq` | Diğer özkaynak düzeltmeleri |
| `seta12` | Dava/sigorta uzlaşmasının vergi sonrası etkisi; 12 aylık gösterim |
| `setaq` | Dava/sigorta uzlaşmasının vergi sonrası etkisi |
| `setay` | Dava/sigorta uzlaşmasının vergi sonrası etkisi; yıl başından birikimli gösterim |
| `setd12` | Dava/sigorta uzlaşmasının seyreltilmiş EPS etkisi; 12 aylık gösterim |
| `setdq` | Dava/sigorta uzlaşmasının seyreltilmiş EPS etkisi |
| `setdy` | Dava/sigorta uzlaşmasının seyreltilmiş EPS etkisi; yıl başından birikimli gösterim |
| `seteps12` | Dava/sigorta uzlaşmasının temel EPS etkisi; 12 aylık gösterim |
| `setepsq` | Dava/sigorta uzlaşmasının temel EPS etkisi |
| `setepsy` | Dava/sigorta uzlaşmasının temel EPS etkisi; yıl başından birikimli gösterim |
| `setpq` | Dava/sigorta uzlaşmasının vergi öncesi etkisi |
| `setpy` | Dava/sigorta uzlaşmasının vergi öncesi etkisi; yıl başından birikimli gösterim |
| `sivy` | Yatırımların satışı; yıl başından birikimli gösterim |
| `sstky` | Adi ve imtiyazlı hisse ihracı; yıl başından birikimli gösterim |
| `txdbcaq` | Kısa vadeli ertelenmiş vergi varlığı |
| `txdbclq` | Kısa vadeli ertelenmiş vergi yükümlülüğü |
| `txdbq` | Finansal durum tablosunda ertelenmiş vergi |
| `txdcy` | Nakit akışında ertelenmiş vergi; yıl başından birikimli gösterim |
| `txdiq` | Ertelenmiş gelir vergisi |
| `txditcq` | Ertelenmiş vergi ve yatırım vergi kredisi |
| `txdiy` | Ertelenmiş gelir vergisi; yıl başından birikimli gösterim |
| `txpdy` | Ödenen gelir vergisi; yıl başından birikimli gösterim |
| `txpq` | Ödenecek gelir vergisi |
| `txtq` | Toplam gelir vergisi gideri |
| `txty` | Toplam gelir vergisi gideri; yıl başından birikimli gösterim |
| `uddq` | Kamu hizmeti şirketlerinin tahvil borcu |
| `udfccy` | Kamu hizmeti şirketlerinde ertelenmiş yakıt maliyeti nakit değişimi; yıl başından birikimli gösterim |
| `udmbq` | İpotekli tahvil borcu |
| `udoltq` | Diğer uzun vadeli kamu hizmeti şirketi borcu |
| `udpcoq` | Kirlilik kontrolü finansman yükümlülükleri |
| `ugiq` | Faiz gideri öncesi brüt gelir |
| `ulcoq` | Diğer kısa vadeli kamu hizmeti şirketi yükümlülükleri |
| `utemq` | Toplam bakım gideri |
| `utfdocy` | Faaliyetlerden yaratılan toplam fon; yıl başından birikimli gösterim |
| `utfoscy` | Dış kaynaklardan sağlanan toplam fon; yıl başından birikimli gösterim |
| `xaccq` | Tahakkuk etmiş giderler |
| `xidoq` | Olağanüstü kalemler ve durdurulan faaliyetler |
| `xidoy` | Olağanüstü kalemler ve durdurulan faaliyetler; yıl başından birikimli gösterim |
| `xintq` | Faiz ve ilişkili giderler |
| `xinty` | Faiz ve ilişkili giderler; yıl başından birikimli gösterim |
| `xiq` | Olağanüstü kalemler |
| `xiy` | Olağanüstü kalemler; yıl başından birikimli gösterim |
| `xoprq` | Toplam faaliyet giderleri |
| `xopry` | Toplam faaliyet giderleri; yıl başından birikimli gösterim |
| `xrdq` | Ar-Ge gideri |
| `xrdy` | Ar-Ge gideri; yıl başından birikimli gösterim |

## 37 alan: piyasa değeriyle bölünmeyenler

| Kod | Türkçe anlamı |
|---|---|
| `capr1q` | Risk ağırlıklı birinci kuşak sermaye oranı |
| `capr2q` | Risk ağırlıklı ikinci kuşak sermaye oranı |
| `glaq` | Vergi sonrası kazanç/kayıp |
| `glay` | Vergi sonrası kazanç/kayıp; yıl başından birikimli gösterim |
| `glcea12` | Çekirdek kâra göre düzeltilmiş satış kazanç/kaybı: vergi sonrası; 12 aylık gösterim |
| `glceaq` | Çekirdek kâra göre düzeltilmiş satış kazanç/kaybı: vergi sonrası |
| `glceay` | Çekirdek kâra göre düzeltilmiş satış kazanç/kaybı: vergi sonrası; yıl başından birikimli gösterim |
| `glced12` | Çekirdek kâra göre düzeltilmiş satış kazanç/kaybı: seyreltilmiş EPS etkisi; 12 aylık gösterim |
| `glcedq` | Çekirdek kâra göre düzeltilmiş satış kazanç/kaybı: seyreltilmiş EPS etkisi |
| `glcedy` | Çekirdek kâra göre düzeltilmiş satış kazanç/kaybı: seyreltilmiş EPS etkisi; yıl başından birikimli gösterim |
| `glceeps12` | Çekirdek kâra göre düzeltilmiş satış kazanç/kaybı: temel EPS etkisi; 12 aylık gösterim |
| `glceepsq` | Çekirdek kâra göre düzeltilmiş satış kazanç/kaybı: temel EPS etkisi |
| `glceepsy` | Çekirdek kâra göre düzeltilmiş satış kazanç/kaybı: temel EPS etkisi; yıl başından birikimli gösterim |
| `glcepq` | Çekirdek kâra göre düzeltilmiş satış kazanç/kaybı: vergi öncesi |
| `glcepy` | Çekirdek kâra göre düzeltilmiş satış kazanç/kaybı: vergi öncesi; yıl başından birikimli gösterim |
| `gldq` | Kazanç/kaybın seyreltilmiş EPS etkisi |
| `gldy` | Kazanç/kaybın seyreltilmiş EPS etkisi; yıl başından birikimli gösterim |
| `glepsq` | Kazanç/kaybın temel EPS etkisi |
| `glepsy` | Kazanç/kaybın temel EPS etkisi; yıl başından birikimli gösterim |
| `glivq` | Yatırım kazanç/kayıpları |
| `glivy` | Yatırım kazanç/kayıpları; yıl başından birikimli gösterim |
| `glpq` | Vergi öncesi kazanç/kayıp |
| `glpy` | Vergi öncesi kazanç/kayıp; yıl başından birikimli gösterim |
| `optvolq` | Opsiyon değerlemesinde varsayılan oynaklık |
| `optvoly` | Opsiyon değerlemesinde varsayılan oynaklık; yıl başından birikimli gösterim |
| `epsf12` | Olağanüstü kalemler hariç seyreltilmiş EPS; 12 aylık gösterim |
| `epsfi12` | Olağanüstü kalemler dahil seyreltilmiş EPS; 12 aylık gösterim |
| `epsfiq` | Olağanüstü kalemler dahil seyreltilmiş EPS |
| `epsfiy` | Olağanüstü kalemler dahil seyreltilmiş EPS; yıl başından birikimli gösterim |
| `epsfxq` | Olağanüstü kalemler hariç seyreltilmiş EPS |
| `epsfxy` | Olağanüstü kalemler hariç seyreltilmiş EPS; yıl başından birikimli gösterim |
| `epspi12` | Olağanüstü kalemler dahil temel EPS; 12 aylık gösterim |
| `epspiq` | Olağanüstü kalemler dahil temel EPS |
| `epspiy` | Olağanüstü kalemler dahil temel EPS; yıl başından birikimli gösterim |
| `epspxq` | Olağanüstü kalemler hariç temel EPS |
| `epspxy` | Olağanüstü kalemler hariç temel EPS; yıl başından birikimli gösterim |
| `epsx12` | Olağanüstü kalemler hariç temel EPS; 12 aylık gösterim |

