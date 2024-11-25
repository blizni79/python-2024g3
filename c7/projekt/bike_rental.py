import json
import os
from datetime import datetime
import smtplib

file_path = "data/rentals.json"



def rent_bike(customer_name, rental_duration):
    """ Process bike rental."""

    if not validate_rental_input(customer_name, rental_duration):
        return


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

def load_rentals()->list:
    """ Load all rentals from rentals.json"""

    if not os.path.exists(file_path):
        print("No retnals found")
        return []
    
    with open(file_path, "r") as file:
        return json.load(file)


def cancel_rental(customer_name:str):
    """ Cancel a rental by customer name."""
    rentals = load_rentals()
    update = [ r for r in rentals if r["customer_name"]!=customer_name]

    if len(rentals) == len(update):
        print(f"No rental found for {customer_name}")
        return

    with open(file_path,"w") as file:
        json.dump(update, file, indent=4)
        print(f"Rental fo {customer_name} has been canceled.")


def generate_daily_report():
    """Generate a daily report of rentas."""
    rentals = load_rentals()
    date = datetime.now().strftime("%Y-%m-%d")

    report_file = f"data/daily_report_{date}.json"

    with open(report_file , "w") as file:
        json.dump(rentals, file, indent=4)

    print(f"Daily report generated: {report_file}")


def send_rental_invoice_email(customer_email:str, rental_details:dict):
    """ Send an email invoice."""
    from email.mime.text import MIMEText
    try:
        message = MIMEText(f"Thanks you for rental a bike.\n\nDetails: {rental_details}")
        message['Subject'] = "Bike Rental Invoce"
        message['To'] = customer_email
        message['From']  = "invoice@bikerental.com"

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("mail.@gmail.com", "password")
            server.send_message(message)

    except Exception as e:
        print(f"Failed to send email: {e}")



def validate_rental_input(customer_name:str, rental_duration:int):
    """Validate rental inputs"""
    if not customer_name.strip():
        print("Cuostomer name cannot by empty")
        return False

    if rental_duration < 0:
        print("Renat duration must by a positive integer")
        return False
    return True
    