from omamoodel import *
laused=[]

while True:
    v=int(input("1-loeme failist"))
    k=int(input("3-vene,4-english-lisa sõna"))
    s=int(input("paranda vigu 5-vene,6-english"))
    g=int(input("7-mäng"))
    if v==1:
        laused=Loe_failist("vene2.txt")
        for line in laused:
            print(line)
    elif v==2:
        laused=Loe_failist("english2.txt")
        for line in laused:
            print(line)
    elif k==3:

        line=input("lisa lause:")
        laused.append(line)
        Kirjuta_failisse("vene2.txt",laused)
    elif k==4:
        line=input("lisa lause:")
        laused.append(line)
        Kirjuta_failisse("english2.txt",laused)
    elif s==5:
        svabra_gaming("vene2.txt")
    elif s==6:
        svabra_gaming("english2.txt")
