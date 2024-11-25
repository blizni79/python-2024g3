import json
import os
from datetime import datetime
import smtplib

file_path = "data/rentals.json"



def rent_bike(customer_name, rental_duration):
    """ Process bike rental."""

    cost = calculate_cost(rental_duration)
    rental = {
        "customer_name": customer_name,
        "rental_duration": rental_duration,
        "cost": cost,
        "rental_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    save_rental(rental)
    return f"Rental save: {rental}"
 

def calculate_cost(rental_duration:int)->int:
    """Calculate the cost of vike rental."""
    if rental_duration <=1:
        return 10
    return 10 + (rental_duration-1)*5


def save_rental(rental:dict):
    """ Save rental to rentals.json"""
    rentals = []

    #Load existing rentals if th file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            rentals = json.load(file)
    rentals.append(rental)

    # Save th uploaded rentals list
    with open(file_path, "w") as file:
        json.dump(rentals, file, indent=4)

