Poniżej znajdziesz 10 zadań z zastosowaniem pętli `while` w Pythonie. Każde zadanie ma na celu rozwijanie umiejętności pracy z pętlą `while` oraz użycie jej do rozwiązywania różnorodnych problemów.

### Zadania z zastosowaniem pętli `while` w Pythonie

1. **Zgadnij liczbę**
   - Napisz program, który losowo generuje liczbę z zakresu od 1 do 100. Następnie poproś użytkownika o zgadywanie liczby, dopóki użytkownik nie trafi. Program powinien informować użytkownika, czy jego liczba jest za mała, za duża, czy trafiona.

2. **Suma liczb dodatnich**
   - Poproś użytkownika o podawanie liczb całkowitych. Dodawaj podane liczby, dopóki użytkownik nie wpisze liczby ujemnej. Gdy to zrobi, wyświetl sumę wszystkich liczb dodatnich.

3. **Logowanie do systemu**
   - Stwórz prosty system logowania, który będzie prosił użytkownika o wpisanie poprawnego hasła ("sekret123"). Użytkownik ma trzy próby na podanie prawidłowego hasła. Jeśli po trzech próbach nie wpisze poprawnego hasła, wyświetl komunikat "Odmowa dostępu".

4. **Licznik od 1 do 10**
   - Napisz program, który wyświetla liczby od 1 do 10 przy użyciu pętli `while`.

5. **Suma cyfr liczby**
   - Napisz program, który poprosi użytkownika o wprowadzenie liczby całkowitej. Oblicz i wyświetl sumę cyfr tej liczby, używając pętli `while`.

6. **Liczby Armstronga w zakresie**
   - Poproś użytkownika o podanie liczby końcowej `n`, a następnie znajdź i wyświetl wszystkie liczby Armstronga w zakresie od 1 do `n`, używając pętli `while`.

7. **Odliczanie do zera**
   - Poproś użytkownika o podanie liczby całkowitej dodatniej. Następnie odliczaj od tej liczby do zera, wyświetlając kolejne liczby, używając pętli `while`.

8. **Zgadnij hasło**
   - Stwórz program, w którym użytkownik ma odgadnąć hasło ("PythonRocks"). Pętla `while` powinna działać, dopóki użytkownik nie wprowadzi prawidłowego hasła. Po każdej nieudanej próbie wyświetl komunikat "Błędne hasło, spróbuj ponownie".

9. **Lista zakupów**
   - Napisz program, który poprosi użytkownika o wprowadzenie przedmiotów na listę zakupów. Program powinien działać w pętli `while` i kończyć się po wpisaniu przez użytkownika słowa "koniec". Na końcu wyświetl pełną listę zakupów.

10. **Obliczanie silni liczby**
    - Poproś użytkownika o podanie liczby całkowitej dodatniej i oblicz silnię tej liczby (`n!`). Wykorzystaj pętlę `while` do wykonania tego zadania.

### Przykładowe Rozwiązanie Zadania z `while`

#### Zadanie 5: Suma cyfr liczby

**Opis**: Napisz program, który poprosi użytkownika o wprowadzenie liczby całkowitej. Oblicz i wyświetl sumę cyfr tej liczby, używając pętli `while`.

**Rozwiązanie**:

```python
liczba = int(input("Podaj liczbę całkowitą: "))
suma_cyfr = 0

# Wykorzystanie pętli while do obliczenia sumy cyfr
while liczba > 0:
    cyfra = liczba % 10
    suma_cyfr += cyfra
    liczba = liczba // 10

print(f"Suma cyfr podanej liczby wynosi: {suma_cyfr}")
```

**Wyjaśnienie**:
- Liczba jest dzielona przez 10 w każdej iteracji, co pozwala przejść przez każdą cyfrę od końca.
- Cyfra (`cyfra = liczba % 10`) jest dodawana do `suma_cyfr`, aż cała liczba zostanie rozbita na poszczególne cyfry.

### Przykładowe Rozwiązanie Zadania 2: Suma liczb dodatnich

**Opis**: Poproś użytkownika o podawanie liczb całkowitych. Dodawaj podane liczby, dopóki użytkownik nie wpisze liczby ujemnej. Gdy to zrobi, wyświetl sumę wszystkich liczb dodatnich.

**Rozwiązanie**:

```python
suma = 0
while True:
    liczba = int(input("Podaj liczbę (liczba ujemna kończy): "))
    if liczba < 0:
        break
    suma += liczba

print(f"Suma wszystkich liczb dodatnich wynosi: {suma}")
```

**Wyjaśnienie**:
- Pętla `while True:` działa nieskończenie długo, dopóki nie zostanie napotkane `break`.
- Wprowadzona liczba jest dodawana do sumy, jeśli jest dodatnia.
- Gdy użytkownik wpisze liczbę ujemną, pętla zostaje przerwana za pomocą `break`.

Każde z tych zadań rozwija umiejętności pracy z pętlą `while` oraz uczy, jak wykorzystać pętlę do rozwiązywania problemów poprzez iteracje.