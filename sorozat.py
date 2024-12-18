import random

def veletlen():
    lista = []
    for i in range(0,12,1):
        szam = random.randint(-10,1000)
        lista.append(szam)
    return lista

def paratlanok_szama(lista):
    paratlan = 0
    for i in range(0,12,1):
        if ((lista[i] % 2) != 0):
            paratlan += 1
    return paratlan

def konzol_kiir(lista,paratlan):
    print("II/A, B, C:")
    print(*lista,sep="$")
    print("II/D, E:")
    print(f"A páratlanok száma: {paratlan}.")

def fajlba_kiir(paratlan):
    f = open("eredmeny.txt", "a")
    f.write(f"A páratlanok száma: {paratlan}.")