**Prezentacja: Typy Danych w Pythonie**

**1. Liczby całkowite (int)**

Liczby całkowite to liczby bez części ułamkowej, np. 5, -10, 0. Python automatycznie rozpoznaje ten typ, gdy używamy liczb bez kropek dziesiętnych.

- **Przykłady użycia:** liczniki, liczba osób, identyfikatory.
- **Funkcje wbudowane:**
  - `abs(x)` - zwraca wartość absolutną liczby.
    - **Parametry:** `x` - liczba całkowita lub zmiennoprzecinkowa.
    - **Przykład:** `abs(-5)` zwróci `5`.
  - `pow(x, y, z=None)` - zwraca x do potęgi y, opcjonalnie modulo z.
    - **Parametry:** `x` - podstawa, `y` - wykładnik, `z` (opcjonalny) - liczba do obliczenia reszty z potęgowania.
    - **Przykład:** `pow(2, 3)` zwróci `8`, `pow(2, 3, 3)` zwróci `2`.
  - `int(x, base=10)` - konwertuje x na liczbę całkowitą.
    - **Parametry:** `x` - wartość do konwersji, `base` (opcjonalny) - podstawa systemu liczbowego (domyślnie 10).
    - **Przykład:** `int('10', 2)` zwróci `2`.
  - `bin(x)` - zwraca reprezentację binarną liczby x.
    - **Parametry:** `x` - liczba całkowita.
    - **Przykład:** `bin(10)` zwróci `'0b1010'`.
  - `hex(x)` - zwraca reprezentację szesnastkową liczby x.
    - **Parametry:** `x` - liczba całkowita.
    - **Przykład:** `hex(255)` zwróci `'0xff'`.
  - `oct(x)` - zwraca reprezentację ósemkową liczby x.
    - **Parametry:** `x` - liczba całkowita.
    - **Przykład:** `oct(8)` zwróci `'0o10'`.
  - `divmod(x, y)` - zwraca parę liczb (iloraz, reszta) z dzielenia x przez y.
    - **Parametry:** `x` - dzielna, `y` - dzielnik.
    - **Przykład:** `divmod(10, 3)` zwróci `(3, 1)`.
  - `max(*args, key=None)` - zwraca największą z podanych liczb.
    - **Parametry:** `*args` - wartości do porównania, `key` (opcjonalny) - funkcja klucza do określenia porządku.
    - **Przykład:** `max(1, 5, 3)` zwróci `5`.
  - `min(*args, key=None)` - zwraca najmniejszą z podanych liczb.
    - **Parametry:** `*args` - wartości do porównania, `key` (opcjonalny) - funkcja klucza do określenia porządku.
    - **Przykład:** `min(1, 5, 3)` zwróci `1`.
  - `sum(iterable, start=0)` - zwraca sumę wszystkich elementów w iterowalnym obiekcie.
    - **Parametry:** `iterable` - obiekt iterowalny, `start` (opcjonalny) - wartość początkowa do dodania.
    - **Przykład:** `sum([1, 2, 3])` zwróci `6`.

**2. Liczby zmiennoprzecinkowe (float)**

Liczby zmiennoprzecinkowe to liczby z częścią ułamkową, np. 3.14, -2.5, 0.0. Python rozpoznaje je, gdy używamy liczb z kropką dziesiętną.

- **Przykłady użycia:** obliczenia z użyciem miar, współrzędne.
- **Funkcje wbudowane:**
  - `round(x, n=0)` - zaokrągla x do n miejsc po przecinku.
    - **Parametry:** `x` - liczba do zaokrąglenia, `n` (opcjonalny) - liczba miejsc po przecinku (domyślnie `0`).
    - **Przykład:** `round(3.14159, 2)` zwróci `3.14`.
  - `float(x)` - konwertuje x na liczbę zmiennoprzecinkową.
    - **Parametry:** `x` - wartość do konwersji.
    - **Przykład:** `float(5)` zwróci `5.0`.
  - `abs(x)` - zwraca wartość absolutną.
    - **Parametry:** `x` - liczba.
    - **Przykład:** `abs(-3.7)` zwróci `3.7`.
  - `is_integer()` - zwraca `True`, jeśli liczba jest liczbą całkowitą.
    - **Przykład:** `(5.0).is_integer()` zwróci `True`.
  - `pow(x, y, z=None)` - zwraca x do potęgi y, opcjonalnie modulo z.
    - **Parametry:** `x` - podstawa, `y` - wykładnik, `z` (opcjonalny) - liczba do obliczenia reszty z potęgowania.
    - **Przykład:** `pow(2.5, 2)` zwróci `6.25`.

**3. Łańcuchy znaków (str)**

Łańcuchy znaków to ciągi tekstowe, np. "Hello World", "Python jest super!". Python pozwala na łatwe operowanie na tekście.

- **Przykłady użycia:** przechowywanie i manipulacja tekstu, komunikaty dla użytkownika.
- **Funkcje wbudowane:**
  - `len(s)` - zwraca długość łańcucha.
    - **Parametry:** `s` - łańcuch znaków.
    - **Przykład:** `len("Hello")` zwróci `5`.
  - `str(x)` - konwertuje x na łańcuch znaków.
    - **Parametry:** `x` - wartość do konwersji.
    - **Przykład:** `str(123)` zwróci `'123'`.
  - `s.upper()` - konwertuje wszystkie znaki w łańcuchu do wielkich liter.
    - **Przykład:** `"python".upper()` zwróci `'PYTHON'`.
  - `s.replace(a, b, count=-1)` - zamienia podłańcuch `a` na `b`.
    - **Parametry:** `a` - podłańcuch do zastąpienia, `b` - nowy podłańcuch, `count` (opcjonalny) - maksymalna liczba zamian (domyślnie `-1` - wszystkie).
    - **Przykład:** `"Hello World".replace('World', 'Python')` zwróci `'Hello Python'`.
  - `s.find(sub, start=0, end=None)` - zwraca indeks pierwszego wystąpienia `sub` w łańcuchu.
    - **Parametry:** `sub` - podłańcuch do wyszukania, `start` (opcjonalny) - początkowy indeks (domyślnie `0`), `end` (opcjonalny) - końcowy indeks (domyślnie koniec łańcucha).
    - **Przykład:** `"Hello".find('e')` zwróci `1`.
  - `s.join(iterable)` - łączy elementy iterowalne, używając łańcucha `s` jako separatora.
    - **Parametry:** `iterable` - obiekt iterowalny zawierający elementy do połączenia.
    - **Przykład:** `','.join(['a', 'b', 'c'])` zwróci `'a,b,c'`.
  - `s.startswith(prefix, start=0, end=None)` - sprawdza, czy łańcuch zaczyna się od `prefix`.
    - **Parametry:** `prefix` - prefiks do sprawdzenia, `start` (opcjonalny) - początkowy indeks (domyślnie `0`), `end` (opcjonalny) - końcowy indeks (domyślnie koniec łańcucha).
    - **Przykład:** `"Hello".startswith('He')` zwróci `True`.
  - `s.endswith(suffix, start=0, end=None)` - sprawdza, czy łańcuch kończy się na `suffix`.
    - **Parametry:** `suffix` - sufiks do sprawdzenia, `start` (opcjonalny) - początkowy indeks (domyślnie `0`), `end` (opcjonalny) - końcowy indeks (domyślnie koniec łańcucha).
    - **Przykład:** `"Hello".endswith('lo')` zwróci `True`.
  - `s.strip(chars=None)` - usuwa białe znaki (lub określone znaki) z początku i końca łańcucha.
    - **Parametry:** `chars` (opcjonalny) - znaki do usunięcia (domyślnie białe znaki).
    - **Przykład:** `"  Hello  ".strip()` zwróci `'Hello'`.

**4. Listy (list)**

Listy to uporządkowane kolekcje elementów, które mogą mieć różne typy, np. [1, 2, 3], ["jabłko", "banan", "pomarańcza"].

- **Przykłady użycia:** przechowywanie kolekcji danych, takich jak listy uczniów, ceny.
- **Funkcje wbudowane:**
  - `len(lst)` - zwraca długość listy.
    - **Parametry:** `lst` - lista.
    - **Przykład:** `len([1, 2, 3])` zwróci `3`.
  - `list(x)` - konwertuje x na listę.
    - **Parametry:** `x` - wartość do konwersji.
    - **Przykład:** `list("abc")` zwróci `['a', 'b', 'c']`.
  - `lst.append(x)` - dodaje element `x` na końcu listy.
    - **Parametry:** `x` - element do dodania.
    - **Przykład:** `lst = [1, 2]; lst.append(3)` zmieni `lst` na `[1, 2, 3]`.
  - `lst.remove(x)` - usuwa pierwsze wystąpienie `x` z listy.
    - **Parametry:** `x` - element do usunięcia.
    - **Przykład:** `lst = [1, 2, 3]; lst.remove(2)` zmieni `lst` na `[1, 3]`.
  - `lst.sort(key=None, reverse=False)` - sortuje listę rosnąco.
    - **Parametry:** `key` (opcjonalny) - funkcja klucza do określenia porządku, `reverse` (opcjonalny) - czy sortować w porządku malejącym (domyślnie `False`).
    - **Przykład:** `lst = [3, 1, 2]; lst.sort()` zmieni `lst` na `[1, 2, 3]`.
  - `lst.insert(index, x)` - wstawia element `x` na indeks `index`.
    - **Parametry:** `index` - pozycja, `x` - element do wstawienia.
    - **Przykład:** `lst = [1, 3]; lst.insert(1, 2)` zmieni `lst` na `[1, 2, 3]`.
  - `lst.pop(index=-1)` - usuwa i zwraca element na pozycji `index`.
    - **Parametry:** `index` (opcjonalny) - pozycja elementu do usunięcia (domyślnie `-1` - ostatni element).
    - **Przykład:** `lst = [1, 2, 3]; lst.pop(1)` zwróci `2` i zmieni `lst` na `[1, 3]`.
  - `lst.count(x)` - zwraca liczbę wystąpień `x` w liście.
    - **Parametry:** `x` - element do zliczenia.
    - **Przykład:** `[1, 2, 2, 3].count(2)` zwróci `2`.
  - `lst.reverse()` - odwraca kolejność elementów w liście.
    - **Przykład:** `lst = [1, 2, 3]; lst.reverse()` zmieni `lst` na `[3, 2, 1]`.
  - `lst.copy()` - zwraca płytką kopię listy.
    - **Przykład:** `lst = [1, 2, 3]; lst_copy = lst.copy()` zwróci `[1, 2, 3]`.

**5. Krotki (tuple)**

Krotki to podobne do listy, ale niezmienne (niemodyfikowalne) kolekcje, np. (1, 2, 3), ("Ala", "ma", "kota").

- **Przykłady użycia:** przechowywanie stałych zestawów danych, współrzędnych.
- **Funkcje wbudowane:**
  - `len(tpl)` - zwraca długość krotki.
    - **Parametry:** `tpl` - krotka.
    - **Przykład:** `len((1, 2, 3))` zwróci `3`.
  - `tuple(x)` - konwertuje x na krotkę.
    - **Parametry:** `x` - wartość do konwersji.
    - **Przykład:** `tuple([1, 2, 3])` zwróci `(1, 2, 3)`.
  - `tpl.count(x)` - zwraca liczbę wystąpień `x` w krotce.
    - **Parametry:** `x` - element do zliczenia.
    - **Przykład:** `(1, 2, 2, 3).count(2)` zwróci `2`.
  - `tpl.index(x)` - zwraca indeks pierwszego wystąpienia `x`.
    - **Parametry:** `x` - element do znalezienia.
    - **Przykład:** `(1, 2, 3).index(2)` zwróci `1`.

**6. Słowniki (dict)**

Słowniki to kolekcje par klucz-wartość, np. `{"imie": "Ala", "wiek": 5}`. Pozwalają na szybki dostęp do danych po kluczu.

- **Przykłady użycia:** przechowywanie danych użytkownika, konfiguracja aplikacji.
- **Funkcje wbudowane:**
  - `len(d)` - zwraca liczbę elementów w słowniku.
    - **Parametry:** `d` - słownik.
    - **Przykład:** `len({'a': 1, 'b': 2})` zwróci `2`.
  - `dict(**kwargs)` - tworzy nowy słownik.
    - **Parametry:** `**kwargs` - klucze i wartości jako argumenty nazwane.
    - **Przykład:** `dict(a=1, b=2)` zwróci `{'a': 1, 'b': 2}`.
  - `d.keys()` - zwraca wszystkie klucze w słowniku.
    - **Przykład:** `{'a': 1, 'b': 2}.keys()` zwróci `dict_keys(['a', 'b'])`.
  - `d.values()` - zwraca wszystkie wartości w słowniku.
    - **Przykład:** `{'a': 1, 'b': 2}.values()` zwróci `dict_values([1, 2])`.
  - `d.get(k, default=None)` - zwraca wartość dla klucza `k`, zwraca `default`, jeśli klucz nie istnieje.
    - **Parametry:** `k` - klucz do wyszukania, `default` (opcjonalny) - wartość domyślna, gdy klucz nie istnieje.
    - **Przykład:** `{'a': 1}.get('a')` zwróci `1`.
  - `d.items()` - zwraca pary klucz-wartość jako widok.
    - **Przykład:** `{'a': 1, 'b': 2}.items()` zwróci `dict_items([('a', 1), ('b', 2)])`.
  - `d.update(other)` - aktualizuje słownik `d` o klucze i wartości ze słownika `other`.
    - **Parametry:** `other` - słownik lub iterowalny obiekt klucz-wartość.
    - **Przykład:** `d = {'a': 1}; d.update({'b': 2})` zmieni `d` na `{'a': 1, 'b': 2}`.
  - `d.pop(k, default=None)` - usuwa klucz `k` i zwraca jego wartość.
    - **Parametry:** `k` - klucz do usunięcia, `default` (opcjonalny) - wartość do zwrócenia, gdy klucz nie istnieje.
    - **Przykład:** `d = {'a': 1, 'b': 2}; d.pop('a')` zwróci `1` i zmieni `d` na `{'b': 2}`.
  - `d.clear()` - usuwa wszystkie elementy ze słownika.
    - **Przykład:** `d = {'a': 1, 'b': 2}; d.clear()` zmieni `d` na `{}`.
  - `d.copy()` - zwraca płytką kopię słownika.
    - **Przykład:** `d = {'a': 1}; d_copy = d.copy()` zwróci `{'a': 1}`.

**7. Zbiory (set)**

Zbiory to nieuporządkowane kolekcje unikalnych elementów, np. `{1, 2, 3}`, `{"jabłko", "banan"}`. Zbiory eliminują duplikaty.

- **Przykłady użycia:** operacje matematyczne na zbiorach, usuwanie duplikatów.
- **Funkcje wbudowane:**
  - `len(s)` - zwraca liczbę elementów w zbiorze.
    - **Parametry:** `s` - zbiór.
    - **Przykład:** `len({1, 2, 3})` zwróci `3`.
  - `set(x)` - konwertuje x na zbiór.
    - **Parametry:** `x` - wartość do konwersji.
    - **Przykład:** `set([1, 2, 2, 3])` zwróci `{1, 2, 3}`.
  - `s.add(x)` - dodaje element `x` do zbioru.
    - **Parametry:** `x` - element do dodania.
    - **Przykład:** `s = {1, 2}; s.add(3)` zmieni `s` na `{1, 2, 3}`.
  - `s.remove(x)` - usuwa element `x` ze zbioru.
    - **Parametry:** `x` - element do usunięcia.
    - **Przykład:** `s = {1, 2, 3}; s.remove(2)` zmieni `s` na `{1, 3}`.
  - `s.union(t)` - zwraca sumę zbiorów `s` i `t`.
    - **Parametry:** `t` - inny zbiór.
    - **Przykład:** `{1, 2}.union({3, 4})` zwróci `{1, 2, 3, 4}`.
  - `s.intersection(t)` - zwraca część wspólną zbiorów `s` i `t`.
    - **Parametry:** `t` - inny zbiór.
    - **Przykład:** `{1, 2, 3}.intersection({2, 3, 4})` zwróci `{2, 3}`.
  - `s.difference(t)` - zwraca różnicę zbiorów `s` i `t`.
    - **Parametry:** `t` - inny zbiór.
    - **Przykład:** `{1, 2, 3}.difference({2})` zwróci `{1, 3}`.
  - `s.clear()` - usuwa wszystkie elementy ze zbioru.
    - **Przykład:** `s = {1, 2, 3}; s.clear()` zmieni `s` na `{}`.
  - `s.pop()` - usuwa i zwraca losowy element ze zbioru.
    - **Przykład:** `s = {1, 2, 3}; s.pop()` może zwrócić `1` i zmienić `s` na `{2, 3}`.

**8. Boolowskie (bool)**

Typ `bool` przyjmuje wartość `True` lub `False`. Jest używany do logiki i warunków.

- **Przykłady użycia:** sterowanie przepływem programu, warunki.
- **Funkcje wbudowane:**
  - `bool(x)` - konwertuje x na wartość boolowską.
    - **Parametry:** `x` - wartość do konwersji.
    - **Przykład:** `bool(0)` zwróci `False`, a `bool(1)` zwróci `True`.
  - `not x` - zwraca przeciwną wartość do `x`.
    - **Przykład:** `not True` zwróci `False`.
  - `any(iterable)` - zwraca `True`, jeśli którykolwiek element w iterowalnym jest `True`.
    - **Parametry:** `iterable` - obiekt iterowalny.
    - **Przykład:** `any([0, False, 5])` zwróci `True`.
  - `all(iterable)` - zwraca `True`, jeśli wszystkie elementy w iterowalnym są `True`.
    - **Parametry:** `iterable` - obiekt iterowalny.
    - **Przykład:** `all([1, True, 3])` zwróci `True`.
  - `isinstance(x, type)` - sprawdza, czy obiekt `x` jest określonego typu.
    - **Parametry:** `x` - obiekt do sprawdzenia, `type` - typ do sprawdzenia.
    - **Przykład:** `isinstance(5, int)` zwróci `True`.