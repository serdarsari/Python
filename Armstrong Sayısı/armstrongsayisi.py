while True:
    girdi=input("Sayı girin : ")

    if girdi=="q":
        break
    
    uzunluk=len(girdi)

    toplam=0
    for i in range(uzunluk):
        toplam = toplam + int(girdi[i])**uzunluk
    
    if(toplam==int(girdi)):
        print("Girdiğiniz Sayı Bir Armstrong Sayıdır!")
    else:
        print("Girdiğiniz Sayı Armstrong Bir Sayı Değildir! ")