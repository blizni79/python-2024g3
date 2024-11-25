
#funkcja suma , dodawnie dwoch liczb
def suma(x:float, y:float) -> float:
    return(x+y)

print(suma(5,6))
print(suma(y=7, x=3))

# pi * r * r
PI = 3.14
def pole_kola(r:float)->float :
    global x
    x = 5
    return PI * r**2


print(f"Pole koła wynosu: {pole_kola(5)}")
print(x)



def witaj(imie:str, powitanie:str = 'Czesc') ->str :
    wynik = suma(3,4)
    return f"{powitanie}, {imie} , wynik {wynik}"

print(witaj("Kuba", "Panie profesorze"))

def silnia(n:int)->int:
    if n == 0:
        return 1
    return n * silnia(n-1)

print(silnia(5))

def pi()->float:
    return 3.14

def suma_wielu(*args: int)->int:
    #opis funkcji
    """
    dsds
    ds
    ds
    ds
    d
    """
    return sum(args)

print(suma_wielu(5,6,36,12,365,368,54))

# funckja przekszatcająca celsjusz na fahrenheit


# funkcja filtrujaca liczby parzyste (we:listam wy:lista)

def parzyste(nums:list)->list:
    even_nums = []
    for i in nums:
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
    return even_nums

def parzyste2(t: [int]) -> [int]:
	wy = []
	for i in t:
		if (i%2) == 0:
			wy.append(i)
	return wy

def liczby_parzyste(numbers: list[int]) ->list[int]:
     return [num for num in numbers if num%2 ==0 ]



# Napisz funkcje do obsługi listy zadań do wykonania, która pozwala dodawać, usuwać, wyświetlać i modyfikować zadania. Przechowuj listę zadań w pamięci jako listę słowników.


def dodaj_zadanie(nazwa, opis)
    
def usun_zadanie

def wyswietl_zadanie

def modyfikuj_zadanie