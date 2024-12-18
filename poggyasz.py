class Poggyasz:
    def __init__(self, a, b, c, m):
        self.a = a
        self.b = b
        self.c = c
        self.m = m
      
    def __str__(self):
        return f"Szélesség: {self.a}, Magasság: {self.b}, Mélység: {self.c}, Tömeg: {self.m}"

def beolvasas(fajlnev):
    pogy = []
    file = open(fajlnev, "r")
    sorok = file.readlines()
    file.close()
    fejléc = sorok[0]
    for i in range(1, len(sorok)):
        a, b, c, m = sorok[i].strip().split("#")
        pogy.append(Poggyasz(a, b, c, m))
    return pogy

def poggyaszok(pogy):
    print("III/A, B:")
    print(f"A poggyászok száma: {len(pogy)}")

def atlag_tomeg(pogy):
    ossztomeg = 0
    darab = 0
    for i in range(len(pogy)):
        if pogy[i].a == 51:
            ossztomeg += pogy[i].m
            darab += 1
    print("III/C:")
    if darab > 0:
        print(f"Az 51 cm-es poggyászok átlag tömeg értéke: {int((ossztomeg / darab) * 1000)} g")
    else:
        print("Nincs 51 cm-es poggyász.")

def legmagasabb_poggyasz(pogy):
    legmagasabb = pogy[0]  
    for i in range(1, len(pogy)):
        if pogy[i].b > legmagasabb.b:
            legmagasabb = pogy[i]

    print("III/D:")
    print(f"A legmagasabb poggyász méretei: {legmagasabb.a}x{legmagasabb.b}x{legmagasabb.c}, tömege: {legmagasabb.m} kg.")