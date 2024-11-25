# Program rezerwacji miejsc w kinie
# Zadania do wykonania:
# 1. Wyświetlanie aktualnego stanu rezerwacji miejsc:
#    - Używamy listy `seats`, która przechowuje informacje o rezerwacjach miejsc.
#    - Jeśli miejsce jest wolne, w liście znajduje się wartość `None`.
#    - Jeśli miejsce jest zarezerwowane, w liście przechowywane jest imię osoby, która je zarezerwowała.
#    - Funkcja `print_seats(seats)` wyświetla aktualny stan wszystkich miejsc.
# 
# 2. Dodawanie nowej rezerwacji:
#    - Użytkownik podaje swoje imię i numer miejsca, które chce zarezerwować.
#    - Sprawdzamy, czy numer miejsca jest poprawny (czy mieści się w zakresie 1-10).
#    - Sprawdzamy, czy miejsce jest wolne (czy wartość w liście `seats` jest `None`).
#    - Jeśli miejsce jest wolne, zapisujemy imię użytkownika w odpowiednim indeksie listy `seats`.
#    - Funkcja `add_reservation(seats)` realizuje te kroki.
# 
# 3. Usuwanie istniejącej rezerwacji:
#    - Użytkownik podaje numer miejsca, które chce zwolnić.
#    - Sprawdzamy, czy numer miejsca jest poprawny (czy mieści się w zakresie 1-10).
#    - Sprawdzamy, czy miejsce jest zarezerwowane (czy wartość w liście `seats` nie jest `None`).
#    - Jeśli miejsce jest zarezerwowane, usuwamy rezerwację (ustawiamy wartość `None` w odpowiednim indeksie listy `seats`).
#    - Funkcja `remove_reservation(seats)` realizuje te kroki.
# 
# 4. Modyfikacja istniejącej rezerwacji:
#    - Użytkownik podaje numer miejsca, które chce zmodyfikować.
#    - Sprawdzamy, czy numer miejsca jest poprawny oraz czy miejsce jest zarezerwowane.
#    - Następnie użytkownik podaje nowy numer miejsca, na które chce przenieść rezerwację.
#    - Sprawdzamy, czy nowy numer miejsca jest poprawny i czy miejsce jest wolne.
#    - Jeśli warunki są spełnione, przenosimy rezerwację na nowe miejsce.
#    - Funkcja `modify_reservation(seats)` realizuje te kroki.
# 
# 5. Wyjście z programu:
#    - Użytkownik może zakończyć działanie programu wybierając opcję "5".
#    - Funkcja `main()` odpowiada za główną pętlę programu, która umożliwia wybór opcji przez użytkownika.
from typing import List, Optional

def print_seats(seats: List[Optional[str]]) -> None:
    """
    Wyświetla aktualny stan rezerwacji miejsc.

    :param seats: Lista miejsc, gdzie None oznacza miejsce wolne, a string oznacza zarezerwowane miejsce przez osobę o danym imieniu.
    """
    print("\nRezerwacje miejsc:")
    for i, seat in enumerate(seats):
        status = "wolne" if seat is None else f"zarezerwowane przez {seat}"
        print(f"Miejsce {i + 1}: {status}")
    print()

def add_reservation(seats: List[Optional[str]]) -> None:
    """
    Dodaje nową rezerwację na wybrane miejsce.

    :param seats: Lista miejsc, gdzie None oznacza miejsce wolne, a string oznacza zarezerwowane miejsce przez osobę o danym imieniu.
    """
    name = input("Podaj swoje imię: ")
    try:
        seat_number = int(input("Podaj numer miejsca, które chcesz zarezerwować (1-10): "))
    except ValueError:
        print("Nieprawidłowy numer miejsca. Spróbuj ponownie.")
        return
    
    if seat_number < 1 or seat_number > len(seats):
        print("Nieprawidłowy numer miejsca. Spróbuj ponownie.")
    elif seats[seat_number - 1] is not None:
        print("To miejsce jest już zarezerwowane. Wybierz inne.")
    else:
        seats[seat_number - 1] = name
        print("Rezerwacja zakończona sukcesem.")

def remove_reservation(seats: List[Optional[str]]) -> None:
    """
    Usuwa istniejącą rezerwację.

    :param seats: Lista miejsc, gdzie None oznacza miejsce wolne, a string oznacza zarezerwowane miejsce przez osobę o danym imieniu.
    """
    try:
        seat_number = int(input("Podaj numer miejsca, które chcesz zwolnić (1-10): "))
    except ValueError:
        print("Nieprawidłowy numer miejsca. Spróbuj ponownie.")
        return
    
    if seat_number < 1 or seat_number > len(seats):
        print("Nieprawidłowy numer miejsca. Spróbuj ponownie.")
    elif seats[seat_number - 1] is None:
        print("To miejsce nie jest zarezerwowane.")
    else:
        seats[seat_number - 1] = None
        print("Rezerwacja została usunięta.")

def modify_reservation(seats: List[Optional[str]]) -> None:
    """
    Modyfikuje istniejącą rezerwację, przenosząc ją na inne miejsce.

    :param seats: Lista miejsc, gdzie None oznacza miejsce wolne, a string oznacza zarezerwowane miejsce przez osobę o danym imieniu.
    """
    try:
        old_seat_number = int(input("Podaj numer miejsca, które chcesz zmodyfikować (1-10): "))
    except ValueError:
        print("Nieprawidłowy numer miejsca. Spróbuj ponownie.")
        return
    
    if old_seat_number < 1 or old_seat_number > len(seats) or seats[old_seat_number - 1] is None:
        print("Nieprawidłowy numer miejsca lub miejsce nie jest zarezerwowane.")
    else:
        name = seats[old_seat_number - 1]
        try:
            new_seat_number = int(input("Podaj nowy numer miejsca (1-10): "))
        except ValueError:
            print("Nieprawidłowy numer miejsca. Spróbuj ponownie.")
            return
        
        if new_seat_number < 1 or new_seat_number > len(seats):
            print("Nieprawidłowy numer miejsca. Spróbuj ponownie.")
        elif seats[new_seat_number - 1] is not None:
            print("Nowe miejsce jest już zarezerwowane. Wybierz inne.")
        else:
            seats[old_seat_number - 1] = None
            seats[new_seat_number - 1] = name
            print("Rezerwacja została zmodyfikowana.")

def main() -> None:
    """
    Główna funkcja programu do zarządzania rezerwacjami miejsc w kinie.
    """
    seats: List[Optional[str]] = [None] * 10  # Lista 10 miejsc w kinie, początkowo wszystkie wolne
    
    while True:
        print("Wybierz opcję:")
        print("1. Wyświetl miejsca")
        print("2. Dodaj rezerwację")
        print("3. Usuń rezerwację")
        print("4. Modyfikuj rezerwację")
        print("5. Wyjdź")
        
        choice = input("Twój wybór: ")
        if choice == "1":
            print_seats(seats)
        elif choice == "2":
            add_reservation(seats)
        elif choice == "3":
            remove_reservation(seats)
        elif choice == "4":
            modify_reservation(seats)
        elif choice == "5":
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()
