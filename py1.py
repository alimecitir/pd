import random


def Tfonk(sayi):
    sifatliste = ["guzel","genc","tatli","uzun","iyi","guclu","kibar"] #sifatlari icinde bulunduran liste#
    isimliste = ["insan","adam","kedi","ruya","kalem","kadin","masa"]  #isimleri icinde bulunduran liste#
    liste = []
    i = 0
    while (i<sayi):
        kelime1 = random.randint(0,len(sifatliste)-1)    #0 ile  sifatlari icinde bulunduran listenin uzunlugu arasinda sayi uretme ve bunu kelime1 degiskenine atama#
        kelime2 = random.randint(0,len(isimliste)-1)     #0 ile  isimleri icinde bulunduran listenin uzunlugu arasinda sayi uretme ve bunu kelime2 degiskenine atama#
        cumle = sifatliste[kelime1] + " " + isimliste[kelime2] # isim ve sifat stringlerini birlestirme ve bunu vumle degiskenine atama
        if(len(liste) < sayi):   #listenin uzunlugunu sayiyla (istenen uzunlukta listeyle) karsilastirma
            liste.append(cumle)  #uretilen cumleyi listeye ekleme
        i+=1
    print "Liste:" , liste        
        

def Ifonk(sayi):
    adjectivelist = ["good","bad","tall"]
    namelist = ["man","pencil","cat","dog"]
    liste = []
    i = 0
    while (i < sayi):
        word1 = random.randint(0,len(adjectivelist)-1)
        word2 = random.randint(0,len(namelist)-1)
        if(len(liste) < sayi):
            cumle = adjectivelist[word1] + " " + namelist[word2]
            liste.append(cumle)
        i+=1                  
    print "Liste:",liste
   


dil = int(raw_input(" Lutfen Dili Seciniz: Turkce : 1 English : 2"))
sayi = int(raw_input("Uretmek istediginiz cumle sayýsý:"))

if (dil == 1):
    Tfonk(sayi)
elif(dil == 2):
    Ifonk(sayi)
else:
    print "hatali giris"


