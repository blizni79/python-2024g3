# open()


# plik = open('nazwapliku.txt', tryb)


#tryb
# r - read - odczyt
# w - write - zapis
# a - append - dodawanie/dopisywanie
# r+ - odczyt i zapis
# x - utworz nowy plik, 


import os

if os.path.exists('nazwapliku.txt'):
    with open('nazwapliku.txt', 'r') as plik:
        dane = plik.read()
        print(dane)
else:
    print("Plik nie istnije")


try:
    with open('nazwapliku.txt','x') as plik:
        plik.write("Ten plik zostal utworzony")
except FileExistsError:
    print("Plik juz istanije")


# otwarcie pliku w trybie zapisu
plik = open('nazwapliku.txt','w')

# zapis danychdo pliki
plik.write("Witaj na PW!")
plik.close()


plik = open('nazwapliku.txt','r')

#odczyt danychdo pliki
dane = plik.read()
print(dane)
plik.close()

plik = open('nazwapliku.txt','r')
for linia in plik:
    print(linia.strip())
plik.close()


with open('plik.txt','w') as plik:
    plik.write("wwwww")

with open('plik.txt','r') as plik:
    dane = plik.read()
    print(dane)

with open('plik.txt','a') as plik:
    plik.write("Dodaj na koncu nowa linie")

    
