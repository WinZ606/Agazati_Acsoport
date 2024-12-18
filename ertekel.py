def adat():
    print("I/A, B:")
    lista = []
    neve = input("Étel neve: ")
    rendelo = input("Étel rendelőjének neve: ")
    ertek = int(input("Értékelés (1-5): "))
    lista.append(neve)
    lista.append(rendelo)
    lista.append(ertek)
    return lista

def ertekeles(lista):
    print("I/C:")
    if (lista[2] < 0):
        print("Az értékelés nem lehet negatív!")
    elif (lista[2] > 5):
        print("5 pont feletti értékelés nem elfogadható!")
    else:
        print("Köszönjük az értékelést!")
    