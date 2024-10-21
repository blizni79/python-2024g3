
# Zadanie 1: Przetwarzanie tekstu i analizy statystyczne
# Napisz program, który:
#     Pobiera od użytkownika wieloliniowy tekst.
#     Wypisuje liczbę słów, zdań (przyjmując, że zdania kończą się kropką), oraz średnią długość słowa (w znakach).
#     Sprawdza, czy podane słowo występuje w tekście. Jeśli tak, wypisuje liczbę jego wystąpień oraz pozycje (indeksy) w tekście.

# Podaj tekst: "Python jest fajny. Uczymy się Pythona."
# Podaj szukane słowo: "Python"

text = input("Podaj tekst: ")
search = input("Szukane słowo: ")

words = text.split()
# print(len(words))
sentences = text.count(".")

ilosc_znakpow = 0
for word in words:
    ilosc_znakpow +=len(word)

avg_word = ilosc_znakpow / len(words)

print(f"Liczba słów: {len(words)}")
print(f"Liczba zdań: {sentences}")
print(f"Średnia długość słowa: {avg_word:.2f}")

word_count = text.count(search)

# position = [ i for i in range(len(words)) if text.startswith(search, i) ]

# print(f"Słowo {search} wystepuje {word_count} razy na pozycjach: {position} ")
# for i in range(len(words)):

for i in range(len(words)):
    if text.startswith(search):  
        print(i)