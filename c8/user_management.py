import json
import os
import random
import re
from datetime import datetime
from typing import List, Dict, Any

USERS_FILE = "data/users1.json"

# Utility function for file operations
def load_users_from_file() -> List[Dict[str, Any]]:
    """
    Wczytuje istniejących użytkowników z pliku users.json
    """
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users_to_file(users: List[Dict[str, Any]]) -> None:
    """
    Zapisuje użytkowników do pliku users.json
    """
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Milestone 2: Implementacja funkcji dodawania i edycji użytkowników

def add_user(user_data: Dict[str, Any]) -> None:
    """
    Dodaje nowego użytkownika do pliku users.json
    """
    if not validate_pesel(user_data.get("pesel")):
        raise ValueError("Niepoprawny PESEL")
    if not validate_nip(user_data.get("nip")):
        raise ValueError("Niepoprawny NIP")
    if not validate_regon(user_data.get("regon")):
        raise ValueError("Niepoprawny REGON")

    users = load_users_from_file()
    users.append(user_data)
    save_users_to_file(users)

def edit_user(user_id: str, updated_data: Dict[str, Any]) -> None:
    """
    Edytuje dane istniejącego użytkownika
    """
    users = load_users_from_file()

    for user in users:
        if user.get("user_id") == user_id:
            user.update(updated_data)
            save_users_to_file(users)
            return

    raise ValueError("Nie znaleziono użytkownika o podanym ID")

# Milestone 3: Praca z plikiem users.json

def remove_user(user_id: str) -> None:
    """
    Usuwa użytkownika na podstawie jego identyfikatora
    """
    users = load_users_from_file()
    updated_users = [user for user in users if user.get("user_id") != user_id]

    if len(updated_users) == len(users):
        raise ValueError("Nie znaleziono użytkownika o podanym ID")

    save_users_to_file(updated_users)

def load_users() -> None:
    """
    Wczytuje istniejących użytkowników z pliku users.json i wypisuje ich na ekran
    """
    users = load_users_from_file()
    if users:
        for user in users:
            print(user)
    else:
        print("Brak użytkowników.")

# Milestone 4: Walidacja danych użytkownika

def validate_nip(nip: str) -> bool:
    """
    Waliduje numer NIP
    """
    if len(nip) != 10 or not nip.isdigit():
        return False
    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    checksum = sum(int(nip[i]) * weights[i] for i in range(9))
    return checksum % 11 == int(nip[9])

def validate_pesel(pesel: str) -> bool:
    """
    Waliduje numer PESEL
    """
    if len(pesel) != 11 or not pesel.isdigit():
        return False
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = sum(int(pesel[i]) * weights[i] for i in range(10))
    checksum = (10 - (checksum % 10)) % 10
    return checksum == int(pesel[10])

def validate_regon(regon: str) -> bool:
    """
    Waliduje numer REGON
    """
    if len(regon) not in [9, 14] or not regon.isdigit():
        return False
    weights = [8, 9, 2, 3, 4, 5, 6, 7] if len(regon) == 9 else [2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 8, 9, 2]
    checksum = sum(int(regon[i]) * weights[i] for i in range(len(weights)))
    return checksum % 11 == int(regon[-1])

# Milestone 5: Generowanie i walidacja hasł

def generate_password(length: int = 12) -> str:
    """
    Generuje silne hasło o minimalnej długości 12 znaków
    """
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-="
    return "".join(random.choice(chars) for _ in range(length))

def validate_password(password: str) -> bool:
    """
    Waliduje siłę hasła
    """
    if len(password) < 12:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+-=]", password):
        return False
    return True

# Przykładowe użycie z input
if __name__ == "__main__":
    while True:
        print("\nWybierz operację:")
        print("1. Dodaj użytkownika")
        print("2. Edytuj użytkownika")
        print("3. Usuń użytkownika")
        print("4. Wyświetl użytkowników")
        print("5. Wyjście")
        choice = input("Wybór: ")

        if choice == "1":
            user_id = input("Podaj ID użytkownika: ")
            name = input("Podaj imię i nazwisko: ")
            pesel = input("Podaj PESEL: ")
            nip = input("Podaj NIP: ")
            regon = input("Podaj REGON: ")
            user_data = {
                "user_id": user_id,
                "name": name,
                "pesel": pesel,
                "nip": nip,
                "regon": regon
            }
            try:
                add_user(user_data)
                print("Użytkownik dodany pomyślnie.")
            except ValueError as e:
                print(f"Błąd walidacji: {e}")
            except FileNotFoundError as e:
                print(f"Błąd pliku: {e}")

        elif choice == "2":
            user_id = input("Podaj ID użytkownika do edycji: ")
            print("Podaj nowe dane (pozostaw puste, aby nie zmieniać):")
            name = input("Nowe imię i nazwisko: ")
            pesel = input("Nowy PESEL: ")
            nip = input("Nowy NIP: ")
            regon = input("Nowy REGON: ")
            updated_data = {}
            if name:
                updated_data["name"] = name
            if pesel:
                updated_data["pesel"] = pesel
            if nip:
                updated_data["nip"] = nip
            if regon:
                updated_data["regon"] = regon
            try:
                edit_user(user_id, updated_data)
                print("Dane użytkownika zaktualizowane pomyślnie.")
            except ValueError as e:
                print(f"Błąd: {e}")

        elif choice == "3":
            user_id = input("Podaj ID użytkownika do usunięcia: ")
            try:
                remove_user(user_id)
                print("Użytkownik usunięty pomyślnie.")
            except ValueError as e:
                print(f"Błąd: {e}")

        elif choice == "4":
            load_users()

        elif choice == "5":
            break

        else:
            print("Niepoprawny wybór, spróbuj ponownie.")

    # Generowanie i walidacja hasła
    password = generate_password()
    print(f"Wygenerowane hasło: {password}")
    print(f"Czy hasło jest poprawne? {'Tak' if validate_password(password) else 'Nie'}")
