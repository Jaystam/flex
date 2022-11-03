import os

bestand = open("klasgenoten.txt", "r")
tekst_regel = bestand.readline()
while tekst_regel:
    os.mkdir(tekst_regel.strip())
    tekst_regel = bestand.readline()