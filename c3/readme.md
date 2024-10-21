Stałe w Pythonie to wartości, które nie powinny zmieniać się w trakcie działania programu. 
Python nie ma wbudowanego mechanizmu definiowania stałych (jak np. `const` w innych językach), konwencja języka pozwala na stosowanie pewnych rozwiązań, aby uzyskać efekt działania stałych.

### 1. Definiowanie Stałych

W Pythonie nie istnieje słowo kluczowe `const`, ale można stosować konwencje nazw, aby określić, że dana zmienna powinna być traktowana jako stała. Stosujemy do tego nazwy składające się z wielkich liter, opcjonalnie rozdzielone podkreśleniami.

#### Przykład Definicji Stałej

```python
PI = 3.14159
GRAVITY = 9.81
APP_NAME = "MyApplication"
```

W powyższym przykładzie `PI`, `GRAVITY`, `APP_NAME` to stałe. To, że używamy wielkich liter, informuje innych programistów, że te wartości nie powinny się zmieniać.

### 2. Użycie Stałych

Stałe mogą być używane tak jak zwykłe zmienne. Oto przykłady:

```python
def calculate_area(radius):
    return PI * radius * radius

print(f"Obszar koła o promieniu 5 wynosi: {calculate_area(5)}")
```

W powyższym przykładzie `PI` jest traktowane jako stała, co sprawia, że kod jest bardziej czytelny i wyraźnie zaznacza, że wartość ta nie powinna być modyfikowana.

### 3. Przechowywanie Stałych w Oddzielnym Pliku

Aby ułatwić zarządzanie dużymi aplikacjami, często umieszcza się stałe w oddzielnym pliku, np. `constants.py`. Możesz wtedy importować je tam, gdzie są potrzebne.

Przykład pliku `constants.py`:

```python
PI = 3.14159
GRAVITY = 9.81
APP_NAME = "MyApplication"
```

Użycie stałych z innego pliku:

```python
from constants import PI, APP_NAME

def display_app_info():
    print(f"Application Name: {APP_NAME}")

def calculate_circumference(radius):
    return 2 * PI * radius

display_app_info()
print(f"Obwód koła o promieniu 5 wynosi: {calculate_circumference(5)}")
```

### 4. Zmienne Globalne a Stałe

Stałe często pełnią rolę zmiennych globalnych, które są dostępne w całym programie. Warto jednak pamiętać, aby ograniczać użycie zmiennych globalnych, ponieważ mogą one zwiększyć złożoność kodu.

Dzięki konwencji używania wielkich liter, stałe globalne są łatwe do odróżnienia od lokalnych zmiennych.

### 5. Typy Stałych

W Pythonie stałe mogą być różnego typu – numeryczne, tekstowe, listy, krotki itd.

Przykład:

```python
MAX_CONNECTIONS = 5
WELCOME_MESSAGE = "Witamy w naszej aplikacji!"
ALLOWED_EXTENSIONS = ('jpg', 'jpeg', 'png', 'gif')
```

### 6. Stałe a Mutable (Listy, Słowniki)

Jeśli stała odnosi się do struktury danych takiej jak lista lub słownik, należy pamiętać, że struktura ta jest mutowalna, co oznacza, że zawartość listy lub słownika może być zmieniona, nawet jeśli sama zmienna powinna być stała.

Przykład:

```python
ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif']
ALLOWED_EXTENSIONS.append('bmp')  # To zadziała, chociaż ALLOWED_EXTENSIONS jest teoretycznie stałą
```

Aby uniknąć takiej sytuacji, warto użyć krotek, które są niemutowalne:

```python
ALLOWED_EXTENSIONS = ('jpg', 'jpeg', 'png', 'gif')
```

### 7. Ochrona Stałych

Python, będąc językiem dynamicznym, nie posiada wbudowanego mechanizmu do ochrony stałych przed modyfikacją. Z pomocą przychodzi jednak biblioteka `typing` oraz niektóre konwencje, takie jak stosowanie funkcji, które nie pozwalają na zmianę.

Przykład z użyciem klasy, aby zapobiec modyfikacji:

```python
class Constants:
    PI = 3.14159
    GRAVITY = 9.81

# Użycie stałych
print(Constants.PI)
```

Powyższa klasa działa jak kontener na stałe, co sugeruje, że nie należy ich modyfikować.

### Podsumowanie

1. **Stałe w Pythonie**: Python nie posiada stałych w sensie ścisłym, ale konwencją jest używanie wielkich liter, aby zaznaczyć, że dana zmienna jest stała.
2. **Przechowywanie w pliku**: Stałe warto trzymać w oddzielnym pliku, aby ułatwić zarządzanie kodem.
3. **Ograniczanie modyfikacji**: Krotki mogą być pomocne, gdy potrzebujemy niemutowalnych struktur danych.
