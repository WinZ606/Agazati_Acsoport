import ertekel
import sorozat
import poggyasz
from poggyasz import Poggyasz

#ertekel.ertekeles(ertekel.adat())
#sorozat.konzol_kiir(sorozat.veletlen(),sorozat.paratlanok_szama(sorozat.veletlen()))
#sorozat.fajlba_kiir(sorozat.paratlanok_szama(sorozat.veletlen()))

lista = poggyasz.beolvasas("csomag.txt")
poggyasz.poggyaszok(lista)
poggyasz.atlag_tomeg(lista)
poggyasz.legmagasabb_poggyasz(lista)