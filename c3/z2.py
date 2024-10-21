# text = input("Podaj słowo: ")

# if text == text[::-1]:
#     print("To jest palindrom")


# popros usera o podanie 5 liczb, i oblicz i wyswietl średnia artymetyczna:

# liczba1 = input("Podaj liczbe1:")
# liczba2 = input("Podaj liczbe2:")
# liczba3 = input("Podaj liczbe3:")
# liczba4 = input("Podaj liczbe4:")
# liczba5 = input("Podaj liczbe5:")

# liczby = input("Podaj 5 liczb oddzielonych spacja:")


# ile = int(input("Podaj ilosc liczb:"))
# liczby = []
# for _ in range(ile):
#     liczba = float(input("Podaj liczbe:"))
#     liczby.append(liczba)

# srednia = sum(liczby)/ile
# print(f"Srednia to {srednia}")

#Podaj 4 imiona, zapisz do zmiennej listy i posortuj alfabetycznie i wyświetl


# Utwórz słownik przedmiot_oceny z nazwami przedmiotów i ich ocenami. Poproś użytkownika o podanie nazw przedmiotów i ocen, a następnie wyświetl wszystkie klucze i wartości.

# przedmiot_oceny = {}
# for _ in range(3):
#     przedmiot = input("Podaj nazwę przedmiotu: ")
#     ocena = int(input(f"Podaj ocenę z {przedmiot}: "))
#     przedmiot_oceny[przedmiot] = ocena
# print("Oceny:", przedmiot_oceny)

przedmiot_oceny = {}
while True:
    przedmiot = input("Podaj nazwę przedmiotu: ")
    if przedmiot =="":
        break
    ocena = int(input(f"Podaj ocenę z {przedmiot}: "))
    przedmiot_oceny[przedmiot] = ocena

    
print("Oceny:", przedmiot_oceny)

