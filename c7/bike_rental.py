# Milestone 1: Przygotowanie projektu (bike_rental.py)

# bike_rental.py
import json
import datetime
import smtplib
import os

def main():
    # Example entry point
    customer_name = "John Doe"
    rental_duration = 3
    rent_bike(customer_name, rental_duration)

if __name__ == "__main__":
    main()


# Milestone 2: Implementacja podstawowych funkcji (basic_functions.py)

# basic_functions.py
def rent_bike(customer_name, rental_duration):
    cost = calculate_cost(rental_duration)
    rental = {
        "customer_name": customer_name,
        "rental_duration": rental_duration,
        "cost": cost,
        "rental_time": str(datetime.datetime.now())
    }
    save_rental(rental)

def calculate_cost(rental_duration):
    if rental_duration <= 1:
        return 10
    else:
        return 10 + (rental_duration - 1) * 5

def save_rental(rental):
    rentals_file = "data/rentals.json"
    rentals = []
    if os.path.exists(rentals_file):
        with open(rentals_file, "r") as f:
            rentals = json.load(f)
    rentals.append(rental)
    with open(rentals_file, "w") as f:
        json.dump(rentals, f, indent=4)


# Milestone 3: Praca z plikiem rentals.json (rental_management.py)

# rental_management.py
def load_rentals():
    rentals_file = "data/rentals.json"
    if os.path.exists(rentals_file):
        with open(rentals_file, "r") as f:
            rentals = json.load(f)
        for rental in rentals:
            print(rental)
    else:
        print("No rentals found.")

def cancel_rental(customer_name):
    rentals_file = "data/rentals.json"
    if os.path.exists(rentals_file):
        with open(rentals_file, "r") as f:
            rentals = json.load(f)
        updated_rentals = [rental for rental in rentals if rental["customer_name"] != customer_name]
        with open(rentals_file, "w") as f:
            json.dump(updated_rentals, f, indent=4)
    else:
        print("No rentals found.")


# Milestone 4: Generowanie raportów dziennych (report_generation.py)

# report_generation.py
def generate_daily_report():
    rentals_file = "data/rentals.json"
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    report_file = f"data/daily_report_{date_str}.json"
    if os.path.exists(rentals_file):
        with open(rentals_file, "r") as f:
            rentals = json.load(f)
        with open(report_file, "w") as f:
            json.dump(rentals, f, indent=4)
    else:
        print("No rentals found to generate report.")


# Milestone 5: Wysyłanie e-maila z fakturą (email_invoice.py)

# email_invoice.py
def send_rental_invoice_email(customer_email, rental_details):
    try:
        smtp_server = smtplib.SMTP("smtp.example.com", 587)
        smtp_server.starttls()
        smtp_server.login("your_email@example.com", "your_password")
        subject = "Invoice for Bike Rental"
        body = f"Thank you for renting a bike. Here are your rental details: {rental_details}"
        message = f"Subject: {subject}\n\n{body}"
        smtp_server.sendmail("your_email@example.com", customer_email, message)
        smtp_server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


# Milestone 6: Integracja z Google Calendar (google_calendar_integration.py)

# google_calendar_integration.py
from google.oauth2 import service_account
from googleapiclient.discovery import build

def add_calendar_event(summary, start_time, end_time):
    credentials = service_account.Credentials.from_service_account_file(
        "path/to/your/service_account.json",
        scopes=["https://www.googleapis.com/auth/calendar"]
    )
    service = build("calendar", "v3", credentials=credentials)
    event = {
        "summary": summary,
        "start": {"dateTime": start_time, "timeZone": "Europe/Warsaw"},
        "end": {"dateTime": end_time, "timeZone": "Europe/Warsaw"}
    }
    event = service.events().insert(calendarId="primary", body=event).execute()
    print(f"Event created: {event.get('htmlLink')}")
