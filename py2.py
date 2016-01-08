# -*- coding: cp1254 -*-
import random

Liste = []

def IsimUreteci( Sayi,Dil ):
    
    TrSifatListe = [ "guzel","genc","tatli","uzun","iyi","guclu","kibar" ] 
    TrIsimListe = [ "insan","adam","kedi","ruya","kalem","kadin","masa" ]

    EngSifatListe = [ "good","bad","tall" ]
    EngIsimListe = [ "man","pencil","cat","dog" ]
    
    i = 0
    while ( i < Sayi ):
        
        if ( Dil == 1 ):
            Kelime1 = random.randint ( 0,len ( TrSifatListe ) -1 )    
            Kelime2 = random.randint ( 0,len ( TrIsimListe ) -1 )
            Cumle = TrSifatListe [ Kelime1 ] + " " + TrIsimListe [ Kelime2 ]    
    
        elif ( Dil == 2 ):
            Kelime1 = random.randint ( 0,len ( EngSifatListe ) -1 )
            Kelime2 = random.randint ( 0,len ( EngIsimListe ) -1 )
            Cumle = EngSifatListe [ Kelime1 ] + " " + EngIsimListe [ Kelime2 ] 
            
        else:
            print "Hatali giris!"
        
        Liste.append ( Cumle )  
        i+= 1
        
    return Liste
      
        
Dil = int(raw_input(" Lutfen Dili Seciniz: Turkce : 1 English : 2"))
Sayi = int(raw_input("Uretmek istediginiz cumle sayısı:"))

IsimUreteci(Sayi,Dil)

print "Liste:" , Liste  
