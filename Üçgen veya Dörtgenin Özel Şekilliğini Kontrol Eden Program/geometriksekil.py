print("""
****************************
Üçgen veya Dörtgenin Şeklini Bulan Program
****************************
Üçgenin tipini hesaplamak için 1'e basın
Dikdörtgenin tipini hesaplamak için 2'ye basın
""")

girdi=input("Seçin yapın : ")

if girdi =="1":
    x=int(input("1.Kenarı girin : "))
    y=int(input("2.Kenarı girin : "))
    z=int(input("3.Kenarı girin : "))

    if (abs(y-z)<x and x<y+z) and (abs(x-z)<y and y<x+z) and (abs(x-y)<z and z<x+y):
        if x==y or x==z or y==z:
            print("Bu üçgen İkizkenar'dır.")
        elif x==y==z:
            print("Bu üçgen Eşkenar'dır.")
    else:
        print("Bu ölçüler bir üçgen belirtmiyor.")



elif girdi =="2":
    a=int(input("1.Kenarı girin : "))
    b=int(input("2.Kenarı girin : "))
    c=int(input("3.Kenarı girin : "))
    d=int(input("4.Kenarı girin : "))

    if a==b==c==d:
        print("Bu şekil Kare'dir.")
    elif (a==b and c==d) or (a==c and b==d) or (a==d and b==c):
        print("Bu şekil Dikdörtgen'dir.")
    else:
        print("Bu şekil sıradan bir Dörtgen'dir.")
    



