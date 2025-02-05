import json
from datetime import datetime

class FinanceTracker:
    def __init__(self, filename="transactions.json"):
        self.filename = filename
        self.transactions = self.load_transactions()

    def load_transactions(self):
        """Load transactions from a file"""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_transactions(self):
        """Save transactions to a file"""
        with open(self.filename, "w") as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, amount, category, description):
        """Add a new income or expense transaction"""
        transaction = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transactions.append(transaction)
        self.save_transactions()
        print("\n✅ Transaction added successfully!\n")

    def view_transactions(self):
        """Display all transactions"""
        if not self.transactions:
            print("\n📂 No transactions found!\n")
            return

        print("\n📋 Your Transactions:")
        for t in self.transactions:
            print(f"{t['date']} | {t['category']} | ${t['amount']} | {t['description']}")
        print()

    def get_balance(self):
        """Calculate total balance"""
        balance = sum(t['amount'] for t in self.transactions)
        print(f"\n💰 Current Balance: ${balance:.2f}\n")

    def view_category_spending(self):
        """Show spending by category"""
        category_spending = {}
        for t in self.transactions:
            if t['amount'] < 0:  # Expenses only
                category_spending[t['category']] = category_spending.get(t['category'], 0) + abs(t['amount'])

        print("\n📊 Category Spending:")
        for category, total in category_spending.items():
            print(f"{category}: ${total:.2f}")
        print()

# --------- MENU SYSTEM ---------
def main():
    tracker = FinanceTracker()

    while True:
        print("\n📌 Personal Finance Tracker")
        print("1️⃣ Add Transaction")
        print("2️⃣ View Transactions")
        print("3️⃣ Check Balance")
        print("4️⃣ View Spending by Category")
        print("5️⃣ Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            amount = float(input("\nEnter amount (use - for expenses): "))
            category = input("Enter category (Food, Bills, Shopping, etc.): ")
            description = input("Enter description: ")
            tracker.add_transaction(amount, category, description)

        elif choice == "2":
            tracker.view_transactions()

        elif choice == "3":
            tracker.get_balance()

        elif choice == "4":
            tracker.view_category_spending()

        elif choice == "5":
            print("\n👋 Exiting... Have a great day!")
            break

        else:
            print("\n❌ Invalid option, try again.")

if __name__ == "__main__":
    main()
