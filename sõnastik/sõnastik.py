from omamoodul import *
laused=[]

while True:
    v=int(input("1-loeme failist"))
    if v==1:
        laused=Loe_failist("vene.txt")
        for line in laused:
            print(line)
    elif v==2:
        laused=Loe_failist("english.txt")
        for line in laused:
            print(line)