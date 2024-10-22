class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class PartTimeEmployee(Employee):
    def __init__(self, name, base_salary, hours_worked):
        super().__init__(name, base_salary)
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.base_salary * self.hours_worked


def main():
    employees = []

    while True:
        print("\nEmployee Type:")
        print("1. Full-Time Employee")
        print("2. Part-Time Employee")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            name = input("Enter the name of the Full-Time Employee: ")
            base_salary = float(input("Enter the base salary: "))
            bonus = float(input("Enter the bonus amount: "))
            employee = FullTimeEmployee(name, base_salary, bonus)
            employees.append(employee)
            print(f"Full-Time Employee {name} added with salary: {employee.calculate_salary()}")

        elif choice == '2':
            name = input("Enter the name of the Part-Time Employee: ")
            base_salary = float(input("Enter the hourly rate: "))
            hours_worked = float(input("Enter the number of hours worked: "))
            employee = PartTimeEmployee(name, base_salary, hours_worked)
            employees.append(employee)
            print(f"Part-Time Employee {name} added with salary: {employee.calculate_salary()}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

    print("\nSummary of Employees and Salaries:")
    for emp in employees:
        print(f"{emp.name} - Salary: {emp.calculate_salary()}")


# Run the employee salary calculation program
if __name__ == "__main__":
    main()
