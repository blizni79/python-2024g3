#Utwórz zmienną napis i przypisz jej tekst "Witaj w Pythonie!". Wyświetl tekst w całości dużymi literami.

napis = "Witaj w Python!"
print(napis.upper())

# Znajdź indeks pierwszego wystąpienia litery y w napisie "Python jest wspaniały!".

print(napis.index('y'))


owoce = ["jabłko", "gruszka", "banan" ]

print(owoce[1])
owoce.append("pomoarancza")
print(owoce[3])
owoce.remove("gruszka")
print(owoce)
owoce.reverse()
print(owoce)

wspolrzedne =(10,20,30)
print(wspolrzedne[0])
# wspolrzedne[3] = "Kuba"
stale = ("Kuba")
print(stale)



samochod  = { "klucz" : "wartosc", "marka": "Topyota", "model":"Corolla", "rok": 2007}
samochod['kolor'] = "czerwony"
print(samochod["kolor"])

print(samochod.items())

toyota = samochod.pop("marka")
print(toyota)
print(samochod)
# samochod.values()

japonia = samochod.copy()
samochod.clear()

czypada = True
czypada = not czypada

if czypada:
    print("Pada")
else:
    print("Nie pada")