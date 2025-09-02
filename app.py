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

# Show all expenses
def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Your Expenses ---")
    for e in expenses:
        print(f"{e['date']} | {e['category']} | ${e['amount']}")
    print("---------------------")

# Show total expenses
def total_expenses(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"\n💰 Total Expenses: ${total}\n")

# Show expenses by category
def category_summary(expenses):
    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]
    print("\n📊 Category Summary:")
    for cat, amt in summary.items():
        print(f"{cat}: ${amt}")
    print("---------------------")

# Main program
def main():
    expenses = load_expenses()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Show Total Expenses")
        print("4. Show Category Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
       


