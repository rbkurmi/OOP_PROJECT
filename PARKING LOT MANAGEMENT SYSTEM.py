class ParkingSlot:
    def __init__(self, slot_id, vehicle_type):
        self.slot_id = slot_id
        self.vehicle_type = vehicle_type
        self.is_available = True


class Vehicle:
    def __init__(self, license_plate):
        self.license_plate = license_plate


class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate)


class Bike(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate)


class ParkingLot:
    def __init__(self):
        self.slots = []

    def add_slot(self, slot):
        self.slots.append(slot)

    def find_available_slot(self, vehicle):
        for slot in self.slots:
            if slot.is_available and ((isinstance(vehicle, Car) and slot.vehicle_type == 'Car') or
                                      (isinstance(vehicle, Bike) and slot.vehicle_type == 'Bike')):
                slot.is_available = False
                return slot
        return None

    def calculate_fee(self, vehicle, hours_parked):
        if isinstance(vehicle, Car):
            return hours_parked * 10
        elif isinstance(vehicle, Bike):
            return hours_parked * 5


def main():
    parking_lot = ParkingLot()

    # Adding slots to the parking lot
    while True:
        slot_id = input("Enter parking slot ID (or 'exit' to finish): ")
        if slot_id.lower() == 'exit':
            break
        vehicle_type = input("Enter vehicle type (Car/Bike): ")
        parking_lot.add_slot(ParkingSlot(slot_id, vehicle_type))
        print(f"Parking slot {slot_id} for {vehicle_type} added.")

    # Parking vehicles
    while True:
        print("\nOptions:")
        print("1. Park a Car")
        print("2. Park a Bike")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            license_plate = input("Enter the license plate for the Car: ")
            car = Car(license_plate)
            slot = parking_lot.find_available_slot(car)
            if slot:
                print(f"Parking slot {slot.slot_id} assigned for Car {license_plate}.")
                hours_parked = float(input("Enter hours parked: "))
                fee = parking_lot.calculate_fee(car, hours_parked)
                print(f"Total fee for {license_plate}: ${fee}")
            else:
                print("No available slots for Cars.")

        elif choice == '2':
            license_plate = input("Enter the license plate for the Bike: ")
            bike = Bike(license_plate)
            slot = parking_lot.find_available_slot(bike)
            if slot:
                print(f"Parking slot {slot.slot_id} assigned for Bike {license_plate}.")
                hours_parked = float(input("Enter hours parked: "))
                fee = parking_lot.calculate_fee(bike, hours_parked)
                print(f"Total fee for {license_plate}: ${fee}")
            else:
                print("No available slots for Bikes.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the parking lot management program
if __name__ == "__main__":
    main()
