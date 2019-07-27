#istenilen sayıda sayı girilen ve maximumunu bulan program
import sys
def Maximum(*girdi):
    enbuyuk=-sys.maxsize -1           #minimum int değeri... bunu kullanmak için sys'yi import etmemiz gerekiyor
    for i in girdi:
        if enbuyuk<i:
            enbuyuk=i
    
    return enbuyuk
	
print(Maximum(1,2,4,7,3,912,4,3,999))
