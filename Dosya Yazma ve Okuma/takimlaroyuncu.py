gs=[]
fb=[]
bjk=[]
def TakimlaraBol(satir):
    satir=satir[:-1]
    bolunmussatir=satir.split(",")
    isim=bolunmussatir[0]
    takim=bolunmussatir[1]

    
    if(takim=="Galatasaray"):
        gs.append(isim+"\n")
    elif(takim=="Fenerbahçe"):
        fb.append(isim+"\n")
    elif(takim=="Beşiktaş"):
        bjk.append(isim+"\n")

    

with open("futbolcular.txt","r",encoding="utf-8") as file:
    
    liste=file.readlines()
    
    for satir in liste:
        TakimlaraBol(satir)
    
    with open("gs.txt","w",encoding="utf-8") as file:
        for i in gs:
            file.write(i)
    with open("fb.txt","w",encoding="utf-8") as file:
        for i in fb:
            file.write(i)
    with open("bjk.txt","w",encoding="utf-8") as file:
        for i in bjk:
            file.write(i)


    










