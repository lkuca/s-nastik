from pickle import LIST
#from random import *
import random


def Loe_failist(fail:str)->list:
    """
    """
    f=open(fail,"r",encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()

    return jarjend
def Kirjuta_failisse(fail:str,sona:str):
    f=open(fail,"a",encoding="utf-8-sig")
    f.write(sona+"\n")
    f.close()
def muuda_sona(fail:str,fail2:str, jarjend:list,teinekeel:list):
        x=input("vana sõna: ")
        if x in jarjend:
            y=input("uus sõna: ")
            ind=jarjend.index(x)
            jarjend.remove(x)
            jarjend.insert(ind,y)

            k=input(f"translate {y}: ")
            teinekeel.pop(ind)
            teinekeel.insert(ind,k)

            f=open(fail,"w",encoding="utf-8-sig")
            for sona in jarjend:
                f.write(sona+"\n")
            f=open(fail2,"w",encoding="utf-8-sig")
            for sona in teinekeel:
                f.write(sona+"\n")
def game(jarjend:list,teinekeel:list):

    while True:
        sona = random.choice(jarjend)
        kasutaja_vaste=input(f"sisestage vaste sonale {sona}: ")

        ind = jarjend.index(sona)
        if teinekeel[ind] == kasutaja_vaste:
            print("oige")
        else:
            print(f"vale. oige vaste on {teinekeel[ind]}")
            break
