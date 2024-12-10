#!/usr/bin/env python
import json, random, re, os, string

DATA_FILE ="data/users.json"

# user_data:
# {
#		"0": {
# 	"name": "",
#		"pesel": 0,
#		"nip": 0,
# 	"regon": 0,
#		}
# }

def load_users()-> dict:
    users = {}
    try:
        with open(DATA_FILE,"r") as file:
            return json.load(file)
            
        # file = open(DATA_FILE, "r")
        # users = json.load(file)
        # file.close()
    except IOError:
        False
    except json.decoder.JSONDecodeError:
        False
    return users

def dump_users(users):
    with open(DATA_FILE,"w") as file:
        return json.dump(users, file, indent=4)

def add(user_data):
    """
    Dodanie nowego uzytkownika do pliku users.json
    """
    
    # validate_nip(user_data["nip"]) and validate_pesel(user_data["pesel"]) and validate_regon(user_data["regon"])
    if not validate_nip(user_data["nip"]):
        raise ValueError("Nieprawidlowy nip")
    # if not validate_pesel(user_data["pesel"]):
    # 	raise ValueError("Nieprawidlowy nip")
    # if not validate_regon(user_data["regon"]):
    # 	raise ValueError("Nieprawidlowy nip")
    id = 0
    users = load_users()
    
    while True:
        try:
            users[str(id)]
            id += 1
        except KeyError:
            break
    users.update({str(id): user_data})
    dump_users(users)
    return True

def edit_user(user_id, updated_data):
    users = load_users()
    id = str(user_id)
    try:
        user = users[id]
    except KeyError:
        return False
    user.update(updated_data)
    users.update({id: user})
    dump_users(users)
    return True

def remove_user(user_id):
    users = load_users()
    try:
        users.pop(str(user_id))
    except KeyError:
        return False
    dump_users(users)
    return True

# def validate_numbers(user_data):
# 	try:
# 		return validate_nip(user_data["nip"]) and validate_pesel(user_data["pesel"]) and validate_regon(user_data["regon"])
# 	except KeyError:
# 		return False

def validate_nip(nip:str)->bool:
    """
    Walidacja nip
    """
    
    if len(nip) != 10 or not nip.isdigit():
        return False
    
    # weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    # added = 0
    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]

    # for i in range(0,9):
    #     added += int(nip[i]) * weights[i]
    # last = int(nip[9])
    # return last == (added % 11)
    checksum = sum(int(nip[i] * weights[i] for i in range(9)))
    return checksum % 11 ==int(nip[9])

def validate_pesel(pesel:str)->bool:
    """
    Walidacja pesel
    """
    if len(pesel) != 11 or not pesel.isdigit():
        return False
    

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    checksum = sum(int(pesel[i] * weights[i] for i in range(10)))
    checksum = (10-(checksum%10))%10
    return checksum == int(pesel[10])


    # str_pesel = str(pesel)
    # # test length
    # if len(str_pesel) != 11:
    #     return False
    # # test checksum
    # added = 0
    # for i in range(0,10):
    #     added += int(str_pesel[i]) * weights[i]
    # added %= 10
    # if added != 0:
    #     added = 10 - added
    # last = int(str_pesel[10])
    # if last != added:
    #     return False
    # # test month
    # month = int(str_pesel[2:4])
    # if (month > 12 and month < 21) or (month > 32 and month < 41) or (month > 52 and month < 61) or (month > 72 and month < 81) or (month > 92):
    #     return False
    # # test day
    # day = int(str_pesel[4:6])
    # if day > 31:
    #     return False
    # return True
 
def validate_regon(regon):
    str_regon = str(regon)
    if len(str_regon) == 7:
        str_regon = "00" + str_regon
    if len(str_regon) == 9:
        weights = [8, 9, 2, 3, 4, 5, 6, 7]
    elif len(str_regon) == 14:
        weights = [2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8]
    else:
        return False
    added = 0
    for i in range(0,len(str_regon)-1):
        added += int(str_regon[i]) * weights[i]
    added %= 11
    if added == 10:
        added = 0
    last = int(str_regon[len(str_regon)-1])
    return last == added

def generate_password():
    password = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(12))
    print(password)
    return password

def validate_password(password):
    return (len(password) >= 12) and bool(re.search('[A-Z]', password)) and bool(re.search('[a-z]', password)) and bool(re.search('[0-9]', password))

def test_users():
    add_user({"name": "Ela", "pesel": 55030101230, "nip": 1234563218, "regon": 123456785})
    add_user({"name": "Stanisław", "pesel": 55030101193, "nip": 1234563218, "regon": 12345678512347})
    remove_user(0)
    add_user({"name": "Ewa", "pesel": 55030101230, "nip": 1234563218, "regon": 123456785})
    edit_user(1, {"name": "Stanisława"})
    remove_user(256)

# NIP, PESEL, REGON są testowane w test_users()

test_users()
print(load_users())
