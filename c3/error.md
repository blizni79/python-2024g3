### 1. **Niepoprawne wcięcia (IndentationError)**
   Python używa wcięć do oznaczenia bloków kodu. Nieprawidłowe wcięcia skutkują błędem.

   **Błędny kod:**
   ```python
   def func():
   print("Hello")  # Brak odpowiedniego wcięcia
   ```

   **Poprawny kod:**
   ```python
   def func():
       print("Hello")  # Właściwe wcięcie
   ```

### 2. **Próba użycia zmiennej przed jej zdefiniowaniem (NameError)**
   Jeśli próbujemy użyć zmiennej przed jej utworzeniem, Python zwróci błąd `NameError`.

   **Błędny kod:**
   ```python
   print(value)  # value nie jest zdefiniowana
   value = 10
   ```

   **Poprawny kod:**
   ```python
   value = 10
   print(value)
   ```

### 3. **Dzielenie przez zero (ZeroDivisionError)**
   Dzielenie przez zero spowoduje `ZeroDivisionError`.

   **Błędny kod:**
   ```python
   result = 10 / 0  # Dzielenie przez zero
   ```

   **Poprawny kod:**
   ```python
   denominator = 0
   if denominator != 0:
       result = 10 / denominator
   else:
       result = None  # Obsługa błędu, na przykład ustawienie wartości domyślnej
   ```

### 4. **Błędne indeksowanie listy (IndexError)**
   Próba dostępu do elementu poza zakresem listy skutkuje błędem `IndexError`.

   **Błędny kod:**
   ```python
   my_list = [1, 2, 3]
   print(my_list[3])  # Indeks spoza zakresu
   ```

   **Poprawny kod:**
   ```python
   my_list = [1, 2, 3]
   if len(my_list) > 3:
       print(my_list[3])
   else:
       print("Indeks spoza zakresu")
   ```

### 5. **Błędne użycie operatora przypisania (`=`) zamiast porównania (`==`)**
   Operator `=` służy do przypisania wartości, natomiast `==` do porównania.

   **Błędny kod:**
   ```python
   if value = 5:  # Błąd przypisania zamiast porównania
       print("Wartość to 5")
   ```

   **Poprawny kod:**
   ```python
   value = 5
   if value == 5:
       print("Wartość to 5")
   ```

### 6. **Niezgodność typów danych (TypeError)**
   Próba połączenia niekompatybilnych typów, np. liczby i łańcucha znaków, może powodować `TypeError`.

   **Błędny kod:**
   ```python
   number = 10
   message = "Wynik to: " + number  # Próba połączenia int z str
   ```

   **Poprawny kod:**
   ```python
   number = 10
   message = "Wynik to: " + str(number)  # Konwersja int do str
   print(message)
   ```

### 7. **Niezainicjalizowana zmienna w pętli (UnboundLocalError)**
   Próba użycia zmiennej w pętli bez jej wcześniejszej inicjalizacji.

   **Błędny kod:**
   ```python
   total += 10  # Brak wcześniejszej inicjalizacji zmiennej total
   ```

   **Poprawny kod:**
   ```python
   total = 0  # Inicjalizacja zmiennej
   total += 10
   print(total)
   ```

### 8. **Błędne przekazanie argumentów do funkcji (TypeError)**
   Próba wywołania funkcji z niewłaściwą liczbą argumentów.

   **Błędny kod:**
   ```python
   def greet(name):
       print(f"Hello, {name}")

   greet()  # Brak argumentu 'name'
   ```

   **Poprawny kod:**
   ```python
   def greet(name):
       print(f"Hello, {name}")

   greet("Alice")  # Poprawne przekazanie argumentu
   ```

### 9. **Nieprawidłowy dostęp do atrybutów (AttributeError)**
   Próba uzyskania dostępu do nieistniejącego atrybutu obiektu powoduje `AttributeError`.

   **Błędny kod:**
   ```python
   class Car:
       def __init__(self, model):
           self.model = model

   my_car = Car("Toyota")
   print(my_car.color)  # 'Car' nie ma atrybutu 'color'
   ```

   **Poprawny kod:**
   ```python
   class Car:
       def __init__(self, model, color):
           self.model = model
           self.color = color

   my_car = Car("Toyota", "Red")
   print(my_car.color)
   ```

### 10. **Modyfikacja listy podczas iteracji (RuntimeError)**
   Modyfikowanie listy podczas iteracji może prowadzić do `RuntimeError`.

   **Błędny kod:**
   ```python
   my_list = [1, 2, 3, 4]
   for item in my_list:
       if item % 2 == 0:
           my_list.remove(item)  # Modyfikacja listy podczas iteracji
   ```

   **Poprawny kod:**
   ```python
   my_list = [1, 2, 3, 4]
   my_list_copy = my_list[:]
   for item in my_list_copy:
       if item % 2 == 0:
           my_list.remove(item)  # Bezpieczna modyfikacja
   print(my_list)
   ```

### 11. **Błędne użycie `is` zamiast `==` (błąd porównania)**
   Operator `is` porównuje tożsamość obiektów, a nie ich wartość.

   **Błędny kod:**
   ```python
   a = [1, 2, 3]
   b = [1, 2, 3]
   if a is b:  # Porównuje referencje, a nie wartości
       print("Listy są równe")
   ```

   **Poprawny kod:**
   ```python
   a = [1, 2, 3]
   b = [1, 2, 3]
   if a == b:  # Porównuje wartości list
       print("Listy są równe")
   ```

### 12. **Niepoprawne użycie pętli `for` z `range` i `len` (IndexError)**
   Użycie pętli `for` z `range` i `len` może powodować błąd `IndexError`, jeśli źle określono zakres.

   **Błędny kod:**
   ```python
   my_list = [1, 2, 3]
   for i in range(len(my_list) + 1):  # Indeks przekracza długość listy
       print(my_list[i])
   ```

   **Poprawny kod:**
   ```python
   my_list = [1, 2, 3]
   for i in range(len(my_list)):
       print(my_list[i])
   ```
