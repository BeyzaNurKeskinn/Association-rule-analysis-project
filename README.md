## Market Alışveriş Verileri ile FP-Growth Analizi
Bu proje, market alışveriş fişlerinden alınan veriler üzerinde FP-Growth algoritmasını kullanarak sık öğe kümesi analizi yapar. Veriler, bir FP-Tree (Sıklık Örüntü Ağacı) yapısında organize edilir, böylece sık tekrarlanan öğe kümeleri minimum destek değeri kullanılarak belirlenir.

## Proje İçeriği
Veri Yükleme: CSV formatında market alışveriş verilerini yükler.

FP-Tree Yapısı: Her işlemdeki öğe kümesini kullanarak FP-Tree oluşturur.

Ağaç Güncelleme ve Bağlantılar: Sık öğelerle ağaç yapısını günceller ve aynı öğe kümelerini birbirine bağlar.

Minimum Destek Değeri Girişi: Kullanıcıdan minimum destek değeri alır ve bu değere göre sık öğe kümelerini belirler.

Sonuç Görüntüleme: Kullanıcı belirli bir öğeyi arayarak ilgili düğümü ve çocuk düğümleri inceleyebilir.

## Dosyalar
MarketFisi.csv: Market fişi verilerini içeren örnek veri seti.

FP-Tree Kod Dosyası: FP-Growth algoritmasının Python ile implementasyonu.

## Kullanım
Veri Yükleme: MarketFisi.csv dosyasını proje dizinine ekleyin.

Çalıştırma: main.py dosyasını çalıştırın ve minimum destek değerini girin.

Sonuçları İnceleme: FP-Tree yapısını ekranda görüntüleyin ve belirli öğe kümelerinin detaylarını inceleyin.

## Gereksinimler
numpy
pandas
Python kütüphaneleri, aşağıdaki komutla kurulabilir:
pip install numpy pandas

## ÖRNEK
Minimum destek değerini giriniz: 2
2 minimum destek değerine göre oluşturulan FP Tree
 Null    1
   Ekmek    3
     Süt    2
Aranan nesne kümesi: Süt
Süt:
   Süt     2
Bu örnekte, minimum destek değeri 2 olan ve içinde "Süt" geçen bir FP-Tree yapısı oluşturulmuştur.

## Lisans
Bu proje MIT lisansı ile lisanslanmıştır. Ayrıntılar için LICENSE dosyasına bakın.
