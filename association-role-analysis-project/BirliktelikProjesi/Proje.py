import numpy as np
import pandas as pd

# veri tabanımızı import ediyoruz kullandığımız veritabanı bir market alışveriş fişinin verileridir
ds = pd.read_csv('MarketFisi.csv')



# FP ağacı için oluşturduğumuz düğüm sınıfı

class TreeNode:
    def __init__(self, isim, sayi, ebeveyn):
        self.isim = isim  # öğenin adını içerir
        self.sayac = sayi
        self.Link = None  # aynı ada sahip düğümlere bağlanmak için
        self.ebeveyn = ebeveyn  # üst düğümü içerir
        self.cocuklar = {}

    def getSayac(self, integer):
        self.sayac += integer

    def displayNode(self, index=1):
        print('  '*index, self.isim, '  ', self.sayac)
        for cocuk in self.cocuklar.values():
            cocuk.displayNode(index + 1)


# FPTree ağacı fonskiyonu


def fpTree(veri, minSupport=1):
    # Başlık tablomuz için sözlük yapısı
    BaslikTablosu = {}
    # verilerin sıklıklarını buluyoruz ve başlık tablosuna ekliyoruz
    for items in veri:
        for item in items:
         BaslikTablosu[item] = BaslikTablosu.get(item, 0) + veri[items]
    # işlemleri support değerine göre eliyoruz
    for item in list(BaslikTablosu):
        if BaslikTablosu[item] < minSupport:
            del (BaslikTablosu[item])
    # sık olan nesneler başlık tablosu sözlüğümüzün key değerleridir burada onu eşitliyoruz
    frequentItemSet = set(BaslikTablosu.keys())

    if len(frequentItemSet) == 0:
        return None, None
    # başlık tablomuzda işaretçi oluşturmak için tabloyu düzenledik
    for item in BaslikTablosu:
        BaslikTablosu[item] = [BaslikTablosu[item], None]
    # mevcut ağacımızı oluşturuyoruz
    currPree = TreeNode('Null', minSupport, None)
    # işlemlerimizi tekrar geziyoruz
    for islem_kumesi, sayac in veri.items():
        # geçici bir sözlük oluşturduk
        tempD = {}
        # işlemlerimizi gezerken sık itemsetde bulunan nesnelerimizi geçici sözlüğe ekliyoruz
        for item in islem_kumesi:
            if item in frequentItemSet:
                tempD[item] = BaslikTablosu[item][0]

        if len(tempD) > 0:
            # geçici sözlükte eleman bulunuyorsa burada sıralama işlemi yapılıyor
            oItems = [v[0] for v in sorted(
                tempD.items(), key=lambda p: p[1], reverse=True)]
            # ve ağac tekrar güncelleniyor
            GuncelleAgac(oItems, currPree, BaslikTablosu, sayac)

    return currPree, BaslikTablosu
    # ağaç güncelleme fonksiyonu


"""Bu işlev, her işlem için özyinelemeli olarak FP Ağacını oluşturur."""


def GuncelleAgac(items, simdiki_Tree, BaslikTablosu, sayac):
   
    # Çocuk zaten mevcutsa, sayısını artırın 
    # sıraladıgımız veri agacın cocuk düğümlerindeyse
    if items[0] in simdiki_Tree.cocuklar:
        simdiki_Tree.cocuklar[items[0]].getSayac(sayac)
        # Else, alt öğe için yeni bir düğüm oluşturun ve onu üst öğesine bağlayın
    else:
        # cocuk dügümde sıralamış veriyi ekliyoruz
        # Yeni oluşturulan her düğüm için Benzer Öğe tablosu güncellenir
        simdiki_Tree.cocuklar[items[0]] = TreeNode(
            items[0], sayac, simdiki_Tree)
        # burada başlık tablomuzu guncelliyoruz çünkü ağaç yapımız değişti
        if BaslikTablosu[items[0]][1] == None:
            # 1. Düğüm için 'Yok/None' değerini düğümle değiştirin
            BaslikTablosu[items[0]][1] = simdiki_Tree.cocuklar[items[0]]
        else:
            # Son benzer düğüme kadar ilerleyin ve yeni düğümü güncelleyin
            GuncelleTablo(BaslikTablosu[items[0]][1],
                          simdiki_Tree.cocuklar[items[0]])
    # en son sıralanmış öğeler için metodumuzu tekrar çağırıyoruz
    # İşlev, bir işlemdeki her öğe için yinelemeli olarak çağrılır
    if len(items) > 1:
        GuncelleAgac(
            items[1::], simdiki_Tree.cocuklar[items[0]], BaslikTablosu, sayac)




# GuncelleTablo(), düğüm bağlantılarının bu öğenin ağaçtaki her örneğini işaret etmesini sağlar
# Başlık tablomuzu güncellemek için yazmış olduğumuz fonksiyon
def GuncelleTablo(simdiki_Node, hedefNode):
    while (simdiki_Node.Link != None):
        simdiki_Node = simdiki_Node.Link
    simdiki_Node.Link = hedefNode


islemler = []
# ilk 20 satırı alıyorz veri çok olduğu için ve işlemler dizimize ekliyoruz
for i in range(0, 20):
    islemler.append([str(ds.values[i, j]) for j in range(0, 20)])


# sözlüğümüzü frozenset ile değiştiriyoruz
def tData(veriSeti):
    tmpDict = {}
    for islemler in veriSeti:
        tmpDict[frozenset(islemler)] = 1
    return tmpDict


yeniVeri = islemler

yeniVeriSeti = tData(yeniVeri)

while True:
    try:
        minSupport = int(input('Minimum support değerini giriniz: '))
        break
    except Exception:
        print('lütfen bir tam sayı girin!!')


fpTree, BaslikTablosu = fpTree(yeniVeriSeti, minSupport)

print(str(minSupport) + ' minimum destek değerine göre oluşturulan FP TRee')

fpTree.displayNode()

while 1 < 2:
    arananItem = input("Aranan nesne kümesi ")
    print("Nesne kümesi: ")
    BaslikTablosu[arananItem][1].displayNode()
# Öğe ve sıklık sayısı, ağacın derinliğini temsil eden girinti ile görüntülenir.
