
import sqlite3
import time

class Sarki():
    def __init__(self,isim,sanatci,album,sirket,sure):
        self.isim=isim
        self.sanatci=sanatci
        self.album=album
        self.sirket=sirket
        self.sure=sure
    
    def __str__(self):
        return "Şarkı İsmi : {}\nSanatçı : {}\nAlbüm : {}\nProdüksiyon Şirketi : {}\nŞarkı Süresi : {}\n".format(self.isim,self.sanatci,self.album,self.sirket,self.sure)
    
class SarkiKutuphanesi():
    def __init__(self):
        self.VeritabaninaBaglan()
    
    def VeritabaninaBaglan(self):
        self.baglanti=sqlite3.connect("kutuphane.db")
        self.cursor=self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS sarkilar (isim TEXT,sanatci TEXT,album TEXT,sirket TEXT,sure INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    
    def BaglantiyiKes(self):
        self.baglanti.close()
    
    def ToplamSarkiSuresi(self):
        sorgu = "SELECT * FROM sarkilar"

        self.cursor.execute(sorgu)

        sarkilar = self.cursor.fetchall()

        if (len(sarkilar)==0):
            print("Listede şarkı bulunmuyor.")
        else:
            toplamsaniye=0
            for i in sarkilar:
                sarki = Sarki(i[0],i[1],i[2],i[3],i[4])
                toplamsaniye +=sarki.sure
            
            toplamdk=toplamsaniye//60
            toplamsn=toplamsaniye%60
            print("Toplam Şarkı Süresi Hesaplanıyor...")
            time.sleep(2)
            print("{}.{}".format(toplamdk,toplamsn))

    
    def SarkiEkle(self,sarki):
        sorgu = "INSERT INTO sarkilar VALUES(?,?,?,?,?)"
        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatci,sarki.album,sarki.sirket,sarki.sure))
        self.baglanti.commit()
    
    def SarkiSil(self,isim):
        sorgu="DELETE FROM sarkilar WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()
    
    def SarkilariGoster(self):
        sorgu = "SELECT * FROM sarkilar"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()

        if (len(sarkilar)==0):
            print("Listede Şarkı Bulunmuyor...")
        else:
            for i in sarkilar:
                sarki=Sarki(i[0],i[1],i[2],i[3],i[4])

                print(sarki)
    
    def SarkilariSil(self):
        sorgu = "DELETE FROM sarkilar"
        self.cursor.execute(sorgu)
        self.baglanti.commit()


