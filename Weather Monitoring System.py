class City:
    def __init__(self, name, temperature, humidity):
        self.name = name
        self.temperature = temperature
        self.humidity = humidity


class WeatherReport:
    def __init__(self):
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)

    def generate_report(self):
        if not self.cities:
            print("No cities in the report.")
            return

        print("\nWeather Report:")
        for city in self.cities:
            print(f"Weather in {city.name}: Temp: {city.temperature}°C, Humidity: {city.humidity}%")


def main():
    report = WeatherReport()

    while True:
        print("\nOptions:")
        print("1. Add City")
        print("2. Generate Weather Report")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            name = input("Enter the name of the city: ")
            temperature = float(input(f"Enter the temperature in {name} (°C): "))
            humidity = float(input(f"Enter the humidity in {name} (%): "))
            city = City(name, temperature, humidity)
            report.add_city(city)
            print(f"City {name} added to the report.")

        elif choice == '2':
            report.generate_report()

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the weather report program
if __name__ == "__main__":
    main()
