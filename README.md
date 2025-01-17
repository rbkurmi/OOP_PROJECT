# OOP Project Collection

This repository contains a collection of object-oriented programming (OOP) projects that demonstrate various concepts and implementations in Python. Each project serves as an example of how OOP principles can be applied to real-world problems.

## Table of Contents

1. [ATM Simulation System]
2. [School Management System]
3. [Employee Management System]
4. [Weather Monitoring System]
5. [Parking Lot Management System]
6. [Expense Tracker]
7. [Tic-Tac-Toe Game]
8. [Hotel Room Reservation System]
9. [University Course Enrollment System]
10. [Flight Reservation System]
11. [Bank Loan Management System]
12. [Online Shopping Cart System]

## ATM Simulation System
**Description:** Create a simple ATM system that allows users to check balance, withdraw, deposit, and transfer money between accounts.

**Classes:**
- `Account`: Handles balance and basic transactions.
- `ATM`: Simulates the ATM interface for a user.

**OOP Concepts:**
- Encapsulation for account details.
- Abstraction for the interface methods.

---

## School Management System
**Description:** A system that manages teachers, students, and courses. Teachers can be assigned to courses, and students can enroll in courses.

**Classes:**
- `Person`: Base class for common attributes like name and age.
- `Teacher` and `Student`: Derived classes from `Person`.
- `Course`: Represents a course that students can enroll in.

**OOP Concepts:**
- Inheritance to share common properties between Teacher and Student.

---

## Employee Management System
**Description:** Manage employees' details, calculate their salaries, and generate monthly reports.

**Classes:**
- `Employee`: Base class for common attributes like name, salary, and position.
- `FullTimeEmployee` and `PartTimeEmployee`: Specialized classes that extend the Employee class.

**OOP Concepts:**
- Polymorphism to calculate different salary structures for full-time and part-time employees.

---

## Weather Monitoring System
**Description:** A system that tracks the weather in different cities, monitors temperature, humidity, and displays forecasts.

**Classes:**
- `City`: Stores weather data for a city.
- `WeatherReport`: Generates and displays the weather report for multiple cities.

**OOP Concepts:**
- Abstraction for managing complex weather reporting logic.

---

## Parking Lot Management System
**Description:** A system to manage parking slots for different types of vehicles (cars, bikes), track available slots, and bill customers based on the parking time.

**Classes:**
- `ParkingSlot`: Represents a parking slot.
- `Vehicle`: Base class for different types of vehicles (Car, Bike).
- `ParkingLot`: Manages parking slots, checks availability, and bills customers.

**OOP Concepts:**
- Inheritance for different types of vehicles.
- Polymorphism to calculate the parking fee based on vehicle type.

---

## Expense Tracker
**Description:** Track daily expenses, categorize them, and generate reports for weekly or monthly spending.

**Classes:**
- `Expense`: Represents an individual expense.
- `ExpenseTracker`: Manages a collection of expenses and generates reports.

**OOP Concepts:**
- Encapsulation for handling sensitive data.
- Abstraction to manage reporting.

---

## Tic-Tac-Toe Game
**Description:** A simple Tic-Tac-Toe game that two players can play in the console.

**Classes:**
- `Player`: Represents a player.
- `TicTacToe`: Manages the game board, turns, and winner determination.

**OOP Concepts:**
- Encapsulation to manage the game state.
- Abstraction to manage gameplay logic.

---

## Hotel Room Reservation System
**Description:** Manage hotel room reservations with details such as check-in and check-out dates, room types, and guest details.

**Classes:**
- `Guest`: Represents a guest.
- `Room`: Represents a room.
- `Reservation`: Manages room reservations.

**OOP Concepts:**
- Inheritance to manage different room types.
- Polymorphism for different pricing models.

---

## University Course Enrollment System
**Description:** A system that allows students to enroll in courses, and professors to manage their courses.

**Classes:**
- `Student`: Represents a student.
- `Professor`: Represents a professor.
- `Course`: Represents a course.

**OOP Concepts:**
- Encapsulation to handle student and professor details.
- Abstraction for course enrollment logic.

---

## Flight Reservation System
**Description:** A flight reservation system that manages flights, passengers, and reservations.

**Classes:**
- `Flight`: Represents a flight.
- `Passenger`: Represents a passenger.
- `Reservation`: Handles flight reservations.

**OOP Concepts:**
- Inheritance to handle different flight classes.
- Polymorphism for pricing models based on flight class.

---

## Bank Loan Management System
**Description:** A system to manage customer loan applications, approve or reject loans, and calculate interest.

**Classes:**
- `Customer`: Represents a customer.
- `Loan`: Represents a loan.
- `LoanManager`: Manages loan approvals and calculations.

**OOP Concepts:**
- Encapsulation for sensitive data.
- Abstraction to calculate interest.

---

## Online Shopping Cart System
**Description:** A shopping cart system where users can add/remove products, view the cart, and check out.

**Classes:**
- `Product`: Represents a product.
- `Cart`: Manages items added to the shopping cart.
- `Customer`: Represents the customer.

**OOP Concepts:**
- Encapsulation for product details.
- Abstraction to manage cart functionality.

---

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or suggestions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
