animal = "dog"
match animal:
    case "dog":
        print("hał hał")
    case "cat":
        print("miał miał")
    case _:
        print ("Zwierzę nie znane!")

def tuple_info(data):
    match data:
        case(x,y):
            print(f"Tuple 2 elementowy: {x}, {y}")
        case(x,y,z):
            print(f"Tuple 3 elementowy: {x} {y} {z}")
        case _:
            print("Nie znany rozmiar tuple")


tuple_info((1,2))
tuple_info((6,7,8))

def number_category(n):
    match n:
        case x if x < 0:
            return "Wartosc ujemna"
        case x if x ==0:
            return "Zero"
        case x if x >0:
            return "Wartosc wieksza od zero"


print(number_category(-5))
wartosc = number_category(0)
print(wartosc)
number_category(5)
