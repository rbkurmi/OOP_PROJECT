class Flight:
    def __init__(self, flight_number, destination, price):
        self.flight_number = flight_number
        self.destination = destination
        self.price = price
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)


class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number


class Reservation:
    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight

    def confirm_reservation(self):
        self.flight.add_passenger(self.passenger)


# Function to create a flight
def create_flight():
    flight_number = input("Enter flight number: ")
    destination = input("Enter destination: ")
    price = float(input("Enter flight price: "))
    return Flight(flight_number, destination, price)


# Function to create a passenger
def create_passenger():
    name = input("Enter passenger name: ")
    passport_number = input("Enter passport number: ")
    return Passenger(name, passport_number)


# Function to create a reservation
def create_reservation(passenger, flight):
    return Reservation(passenger, flight)


# Main function to run the program
def main():
    print("Creating a new flight...")
    flight = create_flight()

    print("Creating a new passenger...")
    passenger = create_passenger()

    print("Creating a reservation...")
    reservation = create_reservation(passenger, flight)

    reservation.confirm_reservation()

    print(
        f"\nReservation confirmed for passenger {passenger.name} on flight {flight.flight_number} to {flight.destination}.")
    print(f"Total price: ${flight.price}")


if __name__ == "__main__":
    main()
