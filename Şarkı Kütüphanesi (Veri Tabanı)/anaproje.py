import sqlite3
from sarki import *

print("""**********************
Şarkı Listesi Programına Hoşgeldin!

1. Veritabanındaki Toplam Şarkı Süresi
2. Şarkı Ekle
3. Şarkı Sil
4. Listeyi Görüntüle
5. Tüm Şarkıları Sil
**********************""")
#Sleep komutları görsel açıdan daha gerçekçi gözükmesi için eklenmiştir. :)
sarkikutuphanesi=SarkiKutuphanesi()

while True:
    girdi = input("Seçiniz : ")
    if (girdi=="q"):
	sarkikutuphanesi.BaglantiyiKes()
        break
    elif (girdi == "1"):
        sarkikutuphanesi.ToplamSarkiSuresi()
    elif (girdi == "2"):
        isim=input("Şarkı İsmi : ")
        sanatci= input("Sanatçı : ")
        album =input("Albüm : ")
        sirket = input("Prodüksiyon Şirketi : ")
        sure = int(input("Şarkı Süresi (Saniye Olarak): "))
        yeniSarki=Sarki(isim,sanatci,album,sirket,sure)
        print("Şarkı Ekleniyor...")
        time.sleep(2)
        sarkikutuphanesi.SarkiEkle(yeniSarki)
        print("Yeni Şarkı Eklendi!")
    elif (girdi == "3"):
        girdi = input("Hangi Şarkıyı Silmek İstiyorsunuz : ")
        print("Siliniyor...")
        time.sleep(2)
        sarkikutuphanesi.SarkiSil(girdi)
        print("Şarkı Silindi!")
    elif (girdi=="4"):
        sarkikutuphanesi.SarkilariGoster()
    elif (girdi=="5"):
        print("Tüm Şarkılar Siliniyor...")
        sarkikutuphanesi.SarkilariSil()
        time.sleep(2)
        print("Tüm Şarkılar Silindi!")
    else:
        print("Geçersiz İşlem!")
