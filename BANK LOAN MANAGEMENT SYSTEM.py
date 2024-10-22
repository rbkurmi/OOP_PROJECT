class Customer:
    def __init__(self, name, credit_score):
        self.name = name
        self.credit_score = credit_score


class Loan:
    def __init__(self, loan_amount, interest_rate, term):
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.term = term

    def calculate_total_payment(self):
        return self.loan_amount * (1 + self.interest_rate * self.term)


class LoanManager:
    def approve_loan(self, customer, loan):
        if customer.credit_score >= 700:
            return f"Loan approved for {customer.name}."
        else:
            return f"Loan rejected for {customer.name}."


# Function to create a customer
def create_customer():
    name = input("Enter customer name: ")
    credit_score = int(input("Enter credit score: "))
    return Customer(name, credit_score)


# Function to create a loan
def create_loan():
    loan_amount = float(input("Enter loan amount: "))
    interest_rate = float(input("Enter interest rate (as a decimal): "))
    term = int(input("Enter loan term (in years): "))
    return Loan(loan_amount, interest_rate, term)


# Main function to run the program
def main():
    print("Creating a new customer...")
    customer = create_customer()

    print("Creating a new loan...")
    loan = create_loan()

    manager = LoanManager()
    approval_message = manager.approve_loan(customer, loan)

    print(approval_message)
    if customer.credit_score >= 700:
        total_payment = loan.calculate_total_payment()
        print(f"Total payment over {loan.term} years: ${total_payment:.2f}")


if __name__ == "__main__":
    main()
