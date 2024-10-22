class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        self.items.remove(product)

    def get_total(self):
        return sum([item.price for item in self.items])


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()


# Function to create a product
def create_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    return Product(name, price)


# Function to manage the shopping cart
def manage_cart(customer):
    while True:
        action = input("Would you like to (a)dd, (r)emove a product, or (v)iew total? Enter 'q' to quit: ").lower()

        if action == 'a':
            product = create_product()
            customer.cart.add_product(product)
            print(f"{product.name} has been added to your cart.")

        elif action == 'r':
            product_name = input("Enter the name of the product to remove: ")
            product_to_remove = next((item for item in customer.cart.items if item.name == product_name), None)
            if product_to_remove:
                customer.cart.remove_product(product_to_remove)
                print(f"{product_name} has been removed from your cart.")
            else:
                print(f"Product '{product_name}' not found in your cart.")

        elif action == 'v':
            total = customer.cart.get_total()
            print(f"Total: ${total:.2f}")

        elif action == 'q':
            print("Exiting the cart management.")
            break

        else:
            print("Invalid option. Please try again.")


# Main function to run the program
def main():
    customer_name = input("Enter customer name: ")
    customer = Customer(customer_name)

    manage_cart(customer)


if __name__ == "__main__":
    main()
