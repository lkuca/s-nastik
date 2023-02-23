from random import *
def Loe_failist(fail:str)->list:
    """
    """
    f=open(fail,"r",encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend
def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,"a",encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+"\n")
    f.close()
def svabra_gaming(jarjend:list):
        x=input("vana sõna")
        y=input("uus sõna")
        if x in jarjend:
            ind=jarjend.index(x)
            jarjend.remove(x)
            jarjend.insert(ind,y)
def game(jarjend:list):
    x=random
    y=input()
    while x in jarjend:
            ind=jarjend.index(x)
            if x==y:
                print("õige")
                continue
            #else

