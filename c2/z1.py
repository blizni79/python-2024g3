# Dane liczbowe i dane tekstowe
# Zadanie 1: Napisz program, który przypisze do zmiennych liczbę całkowitą i tekst, a następnie wypisze te dane na ekran.
# Zadanie 2: Zadeklaruj zmienną z liczbą zmiennoprzecinkową i tekstem, a następnie wypisz oba elementy w jednym ciągu zdaniowym.

liczba = 10
tekst = "Hello, Pyhton"

print("Liczba", liczba)
print("Tekst", tekst)


liczba_zmiennoprzecinkowa =3.14
text = "Wartość liczby pi to:"

print(f"{text} {liczba_zmiennoprzecinkowa}")

# Zadanie 3: Wypisz na ekranie sumę dwóch liczb oraz komunikat z wynikiem w formie: „Suma liczb 5 i 10 wynosi 15”.

liczba1 = 10
liczba2 = 30
suma = liczba1 + liczba2

print(f"Suma liczb {liczba1} i {liczba2} wynosi {suma}")

# Zadanie 4: Wczytaj od użytkownika dwie liczby i oblicz ich iloczyn, różnicę oraz iloraz.

liczba1 = int(input("Podaj piersza liczbe: "))
liczba2 = int(input("Podaj druga liczbe: "))

iloczyn = liczba1 * liczba2
roznica = liczba1 - liczba2

# iloraz = liczba1 / liczba2 if liczba2 != 0  else "Dzielenie prezz zero!"

if liczba2 !=0:
    iloraz = liczba1 / liczba2
else:
    iloraz = "Dzielenie prezz zero!"

print(f"Iloczyn: {iloczyn}")
print(f"Roznica: {roznica}")
print(f"Iloraz: {iloraz}")



# Zadanie 5 : Wczytaj od użytkownika wartość tekstową reprezentującą liczbę, przekonwertuj ją na liczbę całkowitą, dodaj 5 i wypisz wynik.




# Zadanie 6: Wczytaj ciąg znaków, który reprezentuje liczbę zmiennoprzecinkową, przekonwertuj go i oblicz pierwiastek kwadratowy z tej liczby.
import math

liczba = float(input("Podaj liczbę zmiennoprzecinkową: "))
pierwiastek  = math.sqrt(liczba)

print(f"Pierwiastek kwadratowy z liczby {liczba} to {pierwiastek}" )


# Zadanie 1: Przetwarzanie tekstu i analizy statystyczne
# Napisz program, który:
#     Pobiera od użytkownika wieloliniowy tekst.
#     Wypisuje liczbę słów, zdań (przyjmując, że zdania kończą się kropką), oraz średnią długość słowa (w znakach).
#     Sprawdza, czy podane słowo występuje w tekście. Jeśli tak, wypisuje liczbę jego wystąpień oraz pozycje (indeksy) w tekście.

