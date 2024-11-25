### **Implementacja systemu wynajmu rowerów krok po kroku**

#### **Sprint 1: Podstawowe Funkcjonalności Wynajmu Rowerów**

---

#### **Milestone 1: Przygotowanie projektu**

1. **Stwórz strukturę projektu**

```bash
mkdir bike_rental
cd bike_rental
mkdir data
touch bike_rental.py data/rentals.json README.md
```

2. **Zainicjalizuj repozytorium Git**

```bash
git init
git branch -M main
echo "data/" >> .gitignore
git add .
git commit -m "Initialize project structure"
```

---

#### **Milestone 2: Implementacja podstawowych funkcji**

1. **Import wymaganych bibliotek w `bike_rental.py`**

```python
import json
import os
from datetime import datetime
```

---

2. **Funkcja `calculate_cost`**

```python
def calculate_cost(rental_duration: int) -> float:
    """Calculate the cost of bike rental."""
    if rental_duration <= 1:
        return 10
    return 10 + (rental_duration - 1) * 5
```

---

3. **Funkcja `save_rental`**

```python
def save_rental(rental: dict):
    """Save rental to rentals.json."""
    file_path = "data/rentals.json"
    rentals = []

    # Load existing rentals if the file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            rentals = json.load(file)

    rentals.append(rental)

    # Save the updated rentals list
    with open(file_path, "w") as file:
        json.dump(rentals, file, indent=4)
```

---

4. **Funkcja `rent_bike`**

```python
def rent_bike(customer_name: str, rental_duration: int):
    """Process bike rental."""
    cost = calculate_cost(rental_duration)
    rental = {
        "customer_name": customer_name,
        "rental_duration": rental_duration,
        "cost": cost,
        "rental_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    save_rental(rental)
    print(f"Rental saved: {rental}")
```

---

#### **Milestone 3: Praca z plikiem rentals.json**

1. **Funkcja `load_rentals`**

```python
def load_rentals() -> list:
    """Load all rentals from rentals.json."""
    file_path = "data/rentals.json"

    if not os.path.exists(file_path):
        print("No rentals found.")
        return []

    with open(file_path, "r") as file:
        return json.load(file)
```

---

2. **Funkcja `cancel_rental`**

```python
def cancel_rental(customer_name: str):
    """Cancel a rental by customer name."""
    rentals = load_rentals()
    updated_rentals = [r for r in rentals if r["customer_name"] != customer_name]

    if len(rentals) == len(updated_rentals):
        print(f"No rental found for {customer_name}.")
        return

    with open("data/rentals.json", "w") as file:
        json.dump(updated_rentals, file, indent=4)

    print(f"Rental for {customer_name} has been canceled.")
```

---

#### **Sprint 2: Zaawansowane Funkcjonalności**

---

#### **Milestone 1: Generowanie raportów dziennych**

```python
def generate_daily_report():
    """Generate a daily report of rentals."""
    rentals = load_rentals()
    date = datetime.now().strftime("%Y-%m-%d")
    report_file = f"data/daily_report_{date}.json"

    with open(report_file, "w") as file:
        json.dump(rentals, file, indent=4)

    print(f"Daily report generated: {report_file}")
```

---

#### **Milestone 2: Wysyłanie e-maila z fakturą**

1. **Funkcja `send_rental_invoice_email`**

```python
import smtplib
from email.mime.text import MIMEText

def send_rental_invoice_email(customer_email: str, rental_details: dict):
    """Send an email invoice."""
    try:
        message = MIMEText(f"Thank you for renting a bike!\n\nDetails: {rental_details}")
        message["Subject"] = "Bike Rental Invoice"
        message["From"] = "noreply@bikerental.com"
        message["To"] = customer_email

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("your_email@gmail.com", "your_password")
            server.send_message(message)

        print(f"Invoice sent to {customer_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
```

---

#### **Sprint 3: Testowanie i Walidacja**

1. **Walidacja danych wejściowych**

```python
def validate_rental_input(customer_name: str, rental_duration: int) -> bool:
    """Validate rental input."""
    if not customer_name.strip():
        print("Customer name cannot be empty.")
        return False

    if rental_duration <= 0:
        print("Rental duration must be a positive integer.")
        return False

    return True
```

2. **Integracja walidacji w funkcji `rent_bike`**

```python
def rent_bike(customer_name: str, rental_duration: int):
    """Process bike rental."""
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
    print(f"Rental saved: {rental}")
```

---

#### **Podsumowanie**

1. **Zatwierdzaj zmiany w odpowiednich branchach**

```bash
git checkout -b feature/basic_rental
git add .
git commit -m "Implement basic rental functionality"
git push origin feature/basic_rental
```

2. **Twórz Pull Requesty do `main` dla każdej funkcji i milestone.**

---