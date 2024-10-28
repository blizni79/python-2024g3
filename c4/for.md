# Tutorial: Pętla `for` w Pythonie

Pętla `for` jest jednym z podstawowych narzędzi w Pythonie, które pozwalają na iterowanie po sekwencjach danych, takich jak listy, krotki, łańcuchy znaków, słowniki i wiele innych. W tym tutorialu omówimy różne zastosowania pętli `for`, pokażemy jej możliwości oraz przedstawimy zadania praktyczne wraz z ich rozwiązaniami.

---

## Spis treści

1. [Podstawy pętli `for`](#1)
2. [Iterowanie po różnych typach danych](#2)
   - [Listy](#2-1)
   - [Krotki](#2-2)
   - [Łańcuchy znaków](#2-3)
   - [Słowniki](#2-4)
   - [Zbiory](#2-5)
3. [Funkcja `range()`](#3)
4. [Pętla `for` z instrukcjami `break` i `continue`](#4)
5. [Funkcja `enumerate()`](#5)
6. [Zagnieżdżone pętle `for`](#6)
7. [Pętla `for` z klauzulą `else`](#7)
8. [Wyrażenia listowe (list comprehensions)](#8)
9. [Zadania praktyczne](#9)
   - [Zadanie 1](#zad1)
   - [Zadanie 2](#zad2)
   - [Zadanie 3](#zad3)
   - [Zadanie 4](#zad4)
   - [Zadanie 5](#zad5)
10. [Podsumowanie](#10)

---

<a id="1"></a>
## 1. Podstawy pętli `for`

W Pythonie pętla `for` służy do iterowania po elementach sekwencji (np. listy, łańcucha znaków) lub innego obiektu iterowalnego. Ogólna składnia pętli `for` wygląda następująco:

```python
for element in sekwencja:
    # blok kodu do wykonania dla każdego elementu
```

**Przykład:**

```python
fruits = ['jabłko', 'banan', 'czereśnia']
for fruit in fruits:
    print(fruit)
```

**Wynik:**

```
jabłko
banan
czereśnia
```

---

<a id="2"></a>
## 2. Iterowanie po różnych typach danych

<a id="2-1"></a>
### a) Listy

Listy są jednymi z najczęściej używanych struktur danych w Pythonie.

**Przykład:**

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)
```

**Wynik:**

```
2
4
6
8
10
```

<a id="2-2"></a>
### b) Krotki

Krotki są podobne do list, ale są niezmienne (immutable).

**Przykład:**

```python
coordinates = (10, 20, 30)
for coord in coordinates:
    print(coord)
```

**Wynik:**

```
10
20
30
```

<a id="2-3"></a>
### c) Łańcuchy znaków

Łańcuchy znaków są iterowalne znak po znaku.

**Przykład:**

```python
text = "Python"
for char in text:
    print(char)
```

**Wynik:**

```
P
y
t
h
o
n
```

<a id="2-4"></a>
### d) Słowniki

Iterując po słowniku, domyślnie otrzymujemy klucze. Możemy również iterować po wartościach lub parach klucz-wartość.

**Przykład iteracji po kluczach:**

```python
person = {'imie': 'Jan', 'wiek': 30, 'miasto': 'Warszawa'}
for key in person:
    print(key)
```

**Wynik:**

```
imie
wiek
miasto
```

**Iteracja po wartościach:**

```python
for value in person.values():
    print(value)
```

**Wynik:**

```
Jan
30
Warszawa
```

**Iteracja po parach klucz-wartość:**

```python
for key, value in person.items():
    print(f"{key}: {value}")
```

**Wynik:**

```
imie: Jan
wiek: 30
miasto: Warszawa
```

<a id="2-5"></a>
### e) Zbiory

Zbiory są nieuporządkowane i nie zawierają duplikatów.

**Przykład:**

```python
unique_numbers = {1, 2, 3, 2, 1}
for num in unique_numbers:
    print(num)
```

**Wynik (kolejność może być różna):**

```
1
2
3
```

---

<a id="3"></a>
## 3. Funkcja `range()`

Funkcja `range()` generuje sekwencję liczb. Może przyjmować do trzech argumentów: `start`, `stop` i `step`.

**Składnia:**

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

**Przykłady:**

- Od 0 do 4:

  ```python
  for i in range(5):
      print(i)
  ```

  **Wynik:**

  ```
  0
  1
  2
  3
  4
  ```

- Od 1 do 5:

  ```python
  for i in range(1, 6):
      print(i)
  ```

  **Wynik:**

  ```
  1
  2
  3
  4
  5
  ```

- Od 0 do 10 co 2:

  ```python
  for i in range(0, 11, 2):
      print(i)
  ```

  **Wynik:**

  ```
  0
  2
  4
  6
  8
  10
  ```

---

<a id="4"></a>
## 4. Pętla `for` z instrukcjami `break` i `continue`

- **`break`**: przerywa działanie pętli.
- **`continue`**: pomija bieżącą iterację i przechodzi do następnej.

**Przykład użycia `break`:**

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

**Wynik:**

```
0
1
2
3
4
```

**Przykład użycia `continue`:**

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

**Wynik:**

```
0
1
3
4
```

---

<a id="5"></a>
## 5. Funkcja `enumerate()`

Funkcja `enumerate()` pozwala na iterowanie po sekwencji, jednocześnie mając dostęp do indeksu elementu.

**Przykład:**

```python
fruits = ['jabłko', 'banan', 'czereśnia']
for index, fruit in enumerate(fruits):
    print(f"Indeks: {index}, Owoc: {fruit}")
```

**Wynik:**

```
Indeks: 0, Owoc: jabłko
Indeks: 1, Owoc: banan
Indeks: 2, Owoc: czereśnia
```

---

<a id="6"></a>
## 6. Zagnieżdżone pętle `for`

Pętle `for` mogą być zagnieżdżane, czyli jedna pętla może być wewnątrz drugiej.

**Przykład:**

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
```

**Wynik:**

```
i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
i=2, j=2
i=2, j=3
i=3, j=1
i=3, j=2
i=3, j=3
```

---

<a id="7"></a>
## 7. Pętla `for` z klauzulą `else`

Pętla `for` może mieć klauzulę `else`, która jest wykonywana, gdy pętla zakończy się normalnie (nie przez `break`).

**Przykład:**

```python
for i in range(5):
    print(i)
else:
    print("Pętla zakończona")
```

**Wynik:**

```
0
1
2
3
4
Pętla zakończona
```

Jeśli jednak użyjemy `break`, klauzula `else` nie zostanie wykonana.

---

<a id="8"></a>
## 8. Wyrażenia listowe (list comprehensions)

Wyrażenia listowe to zwięzły sposób tworzenia list.

**Składnia:**

```python
[wyrażenie for element in sekwencja if warunek]
```

**Przykład:**

```python
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)
```

**Wynik:**

```
[1, 4, 9, 16, 25]
```

---

<a id="9"></a>
## 9. Zadania praktyczne

<a id="zad1"></a>
### **Zadanie 1:**

Napisz program, który wyświetli liczby od 1 do 50. Dla liczb podzielnych przez 3 zamiast liczby wyświetl "Fizz", dla liczb podzielnych przez 5 wyświetl "Buzz", a dla liczb podzielnych jednocześnie przez 3 i 5 wyświetl "FizzBuzz".

**Rozwiązanie:**

```python
for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

---

<a id="zad2"></a>
### **Zadanie 2:**

Poproś użytkownika o wprowadzenie liczby naturalnej większej od zera. Napisz program, który wyświetli ciąg Collatza dla tej liczby, aż do osiągnięcia liczby 1.

**Rozwiązanie:**

```python
number = int(input("Wprowadź liczbę naturalną większą od zera: "))

if number <= 0:
    print("Liczba musi być większa od zera.")
else:
    while number != 1:
        print(number, end=' ')
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
    print(1)
```

---

<a id="zad3"></a>
### **Zadanie 3:**

Napisz program, który dla liczby n podanej przez użytkownika (n ≥ 1) wygeneruje tabliczkę mnożenia o rozmiarze n x n.

**Rozwiązanie:**

```python
n = int(input("Podaj liczbę naturalną n (n ≥ 1): "))

if n < 1:
    print("Liczba musi być co najmniej 1.")
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end='')
        print()
```

---

<a id="zad4"></a>
### **Zadanie 4:**

Poproś użytkownika o wprowadzenie listy liczb całkowitych dodatnich oddzielonych spacjami. Następnie wyświetl wykres słupkowy z gwiazdek reprezentujący te liczby.

**Rozwiązanie:**

```python
input_numbers = input("Wprowadź liczby całkowite dodatnie oddzielone spacjami: ")
numbers = [int(num) for num in input_numbers.split() if int(num) > 0]

for num in numbers:
    print('*' * num)
```

---

<a id="zad5"></a>
### **Zadanie 5:**

Napisz program, który znajdzie i wyświetli wszystkie liczby Armstronga w zakresie od 100 do 999.

**Rozwiązanie:**

```python
for num in range(100, 1000):
    suma = sum(int(digit) ** 3 for digit in str(num))
    if num == suma:
        print(num)
```

---

<a id="10"></a>
## 10. Podsumowanie

Pętla `for` w Pythonie to potężne narzędzie pozwalające na efektywne iterowanie po różnych strukturach danych. Dzięki niej możemy w prosty sposób przetwarzać listy, krotki, łańcuchy znaków, słowniki i inne iterowalne obiekty. Poznaliśmy również dodatkowe funkcje i konstrukcje, takie jak `range()`, `enumerate()`, instrukcje `break` i `continue`, zagnieżdżone pętle oraz wyrażenia listowe.

Praktyczne zadania pomogły w utrwaleniu wiedzy i pokazaniu, jak zastosować pętlę `for` w różnych kontekstach programistycznych.

**Zachęcam do dalszego eksperymentowania i tworzenia własnych programów wykorzystujących pętle!**