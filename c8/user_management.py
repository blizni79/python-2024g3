import json
import os


USER_FILE = "data/users.json"



def load_user_from_file():
    """
    Wczytuje dane o uzytkownikach z pliku users.json
    """

    if not os.path.exists(USER_FILE):
        return []
    with open(USER_FILE , "r") as f:
        return json.load(f)

def add_user(user_data)