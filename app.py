import json
from datetime import datetime

# File to store expenses
FILE = "expenses.json"

# Load previous expenses
def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save expenses
def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)

# Add a new expense
def add_expense(expenses):
    category = input("Enter category (Food/Transport/Shopping/Other): ")
    amount = float(input("Enter amount: "))
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expenses.append({"category": category, "amount": amount, "date": date})
    save_expenses(expenses)
    print("✅ Expense added successfully!")


    


    


   

       
        

        
       


