class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def generate_report(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        total = sum(expense.amount for expense in self.expenses)
        print(f"\nTotal expenses: ${total:.2f}")

        category_wise = {}
        for expense in self.expenses:
            if expense.category in category_wise:
                category_wise[expense.category] += expense.amount
            else:
                category_wise[expense.category] = expense.amount

        print("Expenses by category:")
        for category, amount in category_wise.items():
            print(f"{category}: ${amount:.2f}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. Generate Expense Report")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            description = input("Enter the description of the expense: ")
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            expense = Expense(description, amount, category)
            tracker.add_expense(expense)
            print(f"Expense '{description}' added.")

        elif choice == '2':
            tracker.generate_report()

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the expense tracker program
if __name__ == "__main__":
    main()
