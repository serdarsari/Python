while True:

    girdi=input("Sayı girin (Çıkmak için 'q' ya basın.) : ")
    
    if(girdi=="q"):
        break
    else:
        girdi2=int(girdi)
        toplam=0
        for i in range(1,girdi2):
            if (girdi2%i==0):
                toplam=toplam+i
            
        
        if (toplam==girdi2):
            print("{} Sayısı, Mükemmel Sayıdır!".format(girdi2))
        else:
            print("{} Sayısı, Mükemmel Sayı Değildir!".format(girdi2))
