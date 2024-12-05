def show_menu():
    print("\nExpense Tracker Menu:")
    print("1. View Expenses")
    print("2. Add Expense")
    print("3. Calculate Total")
    print("4. Exit")

def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded!")
    else:
        print("\nExpenses:")
        for expense in expenses:
            print(f"- {expense['description']}: ${expense['amount']}")

def add_expense(expenses):
    description = input("\nEnter expense description: ").strip()
    try:
        amount = float(input("Enter expense amount: "))
        expenses.append({"description": description, "amount": amount})
        print("Expense added!")
    except ValueError:
        print("Invalid amount! Please enter a number.")

def calculate_total(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal expenses: ${total:.2f}")

def main():
    expenses = []
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            view_expenses(expenses)
        elif choice == "2":
            add_expense(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
