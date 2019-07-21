class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            metin = file.read()

            kelimeler = metin.split()

            self.sadelesmiskelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(",")

                self.sadelesmiskelimeler.append(i)
            
    def TumKelimeler(self):
        kelimeKumesi = set()

        for i in self.sadelesmiskelimeler:
            kelimeKumesi.add(i)
        
        for i in kelimeKumesi:
            print(i)


    def KelimeFrekansi(self):
        self.kelimeSozlugu=dict()

        for i in self.sadelesmiskelimeler:
            if (i in self.kelimeSozlugu):
                self.kelimeSozlugu[i] +=1
            else:
                self.kelimeSozlugu[i] = 1
        
        #for kelime,sayi in kelimeSozlugu.items():
        #    print("{} Kelimesinden {} tane var.".format(kelime,sayi))
    def ArananKelime(self,arananKelime):
        
        dosya.KelimeFrekansi()
        elemanVar=False
        for i in self.kelimeSozlugu.keys():
            if (arananKelime==i):
                print("{} kelimesinden {} tane var.".format(arananKelime,self.kelimeSozlugu[i]))
                elemanVar=True
                break
        if (elemanVar==False):
            print("Aradığınız kelime metinde mevcut değil!")
        
dosya=Dosya()
#dosya.TumKelimeler()  #Hangi kelimelerin kullanıldığını görmek için bu metodu çağırabiliriz.

while True:
    girdi = input("Aramak istediğiniz kelimeyi girin (Çıkış : q ) : ")
    if girdi=="q":
        break
    else:
        dosya.ArananKelime(girdi)
        
    
    
    