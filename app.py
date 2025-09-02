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


    


    


    


   

       
        

        
       


