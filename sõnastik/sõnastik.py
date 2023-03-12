from calendar import prcal
from omamoodul import *

english_list =[] 
vene_list=[] 
vene_list=Loe_failist("vene.txt")
english_list=Loe_failist("english.txt")

print(vene_list)        
print(english_list)        

while True:
    v=int(input(f"1-translate\n2-lisa sona\n3-muuda sona\n4-mang"))
    if v==1:

        vene_letters =["а", "б", "в", "г","д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
        sona=input("sissesta sona:")
        if sona.lower()[0] in vene_letters:
            print(f"{sona} on vene keeles")
            try:
                ind = vene_list.index(sona)
                vaste = english_list[ind]
                print(f"{sona} - {vaste}")
            except ValueError:
                print("sona ei ole leitud")


        else:
            print(f"{sona} on inglise keeles")
            try:
                ind =english_list.index(sona)
                vaste = vene_list[ind] 
                print(f"{sona} - {vaste}")
            except ValueError:
                print("sona ei ole leitud")


    elif v==2:

        uussona=input("lisa vene sona:")
        vene_list.append(uussona)
        Kirjuta_failisse("vene.txt",uussona)
        translate=input("translate seda sona:")
        english_list.append(translate)
        Kirjuta_failisse("english.txt",translate)
    elif v==3:
        muuda_sona("vene.txt","english.txt",vene_list,english_list)
    elif v==4:
        game(vene_list,english_list)
