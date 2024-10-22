class Guest:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_reserved = False

    def reserve(self):
        self.is_reserved = True

    def release(self):
        self.is_reserved = False


class Reservation:
    def __init__(self, guest, room, check_in, check_out):
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out

    def total_price(self):
        days = (self.check_out - self.check_in).days
        return days * self.room.price


# Function to create a guest
def create_guest():
    name = input("Enter guest name: ")
    email = input("Enter guest email: ")
    return Guest(name, email)


# Function to create a room
def create_room():
    room_number = int(input("Enter room number: "))
    room_type = input("Enter room type: ")
    price = float(input("Enter room price per night: "))
    return Room(room_number, room_type, price)


# Function to create a reservation
def create_reservation(guest, room):
    from datetime import datetime

    check_in_str = input("Enter check-in date (YYYY-MM-DD): ")
    check_out_str = input("Enter check-out date (YYYY-MM-DD): ")

    check_in = datetime.strptime(check_in_str, "%Y-%m-%d").date()
    check_out = datetime.strptime(check_out_str, "%Y-%m-%d").date()

    return Reservation(guest, room, check_in, check_out)


# Main function to run the program
def main():
    print("Creating a new guest...")
    guest = create_guest()

    print("Creating a new room...")
    room = create_room()

    print("Creating a new reservation...")
    reservation = create_reservation(guest, room)

    print(f"Total price for the reservation: ${reservation.total_price()}")


if __name__ == "__main__":
    main()
