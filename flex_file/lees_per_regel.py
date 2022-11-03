bestand = open("klasgenoten.txt", "r")
tekst_regel = bestand.readline()
while tekst_regel:
    print(tekst_regel.strip())
    tekst_regel = bestand.readline()