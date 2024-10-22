class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance  # Encapsulated attribute

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            print("Insufficient funds!")
            return self.__balance

    def get_balance(self):
        return self.__balance


class ATM:
    def __init__(self, account):
        self.account = account

    def display_balance(self):
        print(f"Current balance: {self.account.get_balance()}")

    def deposit_money(self, amount):
        self.account.deposit(amount)
        print(f"Deposited {amount}. New balance: {self.account.get_balance()}")

    def withdraw_money(self, amount):
        self.account.withdraw(amount)
        print(f"Withdrew {amount}. New balance: {self.account.get_balance()}")


def main():
    # Getting user input for account creation
    account_number = input("Enter your account number: ")
    initial_balance = float(input("Enter initial balance (default is 0): ") or 0)
    account = Account(account_number, initial_balance)

    atm = ATM(account)

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            atm.display_balance()
        elif choice == '2':
            deposit_amount = float(input("Enter amount to deposit: "))
            atm.deposit_money(deposit_amount)
        elif choice == '3':
            withdraw_amount = float(input("Enter amount to withdraw: "))
            atm.withdraw_money(withdraw_amount)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the ATM simulation
if __name__ == "__main__":
    main()
