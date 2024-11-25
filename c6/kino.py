seats = [None]*140

def print_seats(seats : list):
	j = 1
	for i in seats:
		if i==None:
			print(f"{j} wolne")
		else:
			print(f"{j} zajęte przez {i}")
		j += 1

def add_reservation(seats : list):
	imie = input("Imię: ")
	numer = int(input("Numer: "))
	if numer < 1 or numer > 10:
		return 
	numer -= 1
	if seats[numer] == None:
		seats[numer] = imie

def remove_reservation(setas: list):
	numer = int(input("Numer do zwolnienia: "))
	if numer < 1 or numer > 10:
		return 
	numer -= 1
	seats[numer] = None

def modify_reservation(seats):
	numer1 = int(input("Numer do przeniesienia: "))
	if numer1 < 1 or numer1 > 10:
		return
	numer1 -= 1
	if seats[numer1] == None:
		return
	numer2 = int(input("Nowy numer: "))
	if numer2 < 1 or numer2 > 10:
		return
	numer2 -= 1
	if seats[numer2] == None:
		seats[numer2] = seats[numer1]
		seats[numer1] = None
	

def main():
	while True:
		print("1. Wyświetl stan\n2. Dodaj rezerwację\n3. Usuń rezerwację\n4. Zmodyfikuj rezerwację\n5. Wyjdź")
		opcja = int(input(">"))
		match opcja:
			case 1: print_seats(seats)
			case 2: add_reservation(seats)
			case 3: remove_reservation(seats)
			case 4: modify_reservation(seats)
			case 5: break


main()
