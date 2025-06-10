
print("Welcome to the Personal Finance Tracker!")

expenses = {}

def add_expense():
    while True:
        try:
            description = input("Enter expense description: ").strip()
            if not description:
                raise ValueError("Description cannot be empty.")

            category = input("Enter category: ").strip()
            if not category:
                raise ValueError("Category cannot be empty.")

            amount_input = input("Enter amount: ").strip()
            if not amount_input:
                raise ValueError("Amount cannot be empty.")
            
            amount = float(amount_input)

            if category not in expenses:
                expenses[category] = []

            expenses[category].append((description, amount))
            print("Expense added successfully.")
            break

        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except Exception as e:
            print("An unexpected error occurred.")
            print(f"Error: {e}")

def view_expenses(data):
    if not data:
        print("No expenses recorded yet.")
        return

    for category, items in data.items():
        print(f"\nCategory: {category}")
        for desc, amt in items:
            print(f"  - {desc}: ${amt:.2f}")

def view_summary(data):
    if not data:
        print("No expenses recorded yet.")
        return

    print("\nSummary:")
    for category, items in data.items():
        total = sum(amt for _, amt in items)
        print(f"{category}: ${total:.2f}")

# Menu Loop
while True:
    print("\nWhat would you like to do?")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses(expenses)
    elif choice == '3':
        view_summary(expenses)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")