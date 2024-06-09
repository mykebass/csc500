class ItemToPurchase:
    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        # Initialize the item with name, price, quantity, and description
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def print_item_cost(self):
        # Calculate and print the total cost of the item
        total_cost = self.price * self.quantity
        print(f"{self.name} {self.quantity} @ ${self.price} = ${total_cost}")

def get_item_details(item_number):
    print(f"\nItem {item_number}")
    
    # Prompt for the name of the item
    name = input("Enter the item name:\n")
    # Prompt for the description 
    description = input("Enter the item description:\n")
    
    # Prompt for the price of the item, ensuring a valid number is entered
    while True:
        try:
            price_input = input("Enter the item price:\n")
            price = float(price_input)
            break  # Exit loop if successful
        except ValueError:
            print("Try again. Please enter only a number (no characters).")  # Error message for invalid input
    
    # Prompt for the quantity of the item, ensuring a valid number is entered
    while True:
        try:
            quantity_input = input("Enter the item quantity:\n")
            quantity = int(quantity_input)
            break  # Exit loop if successful
        except ValueError:
            print("Try again. Please enter only a number (no decimals) for quantity.")  # Error message for invalid input

    # Create an instance of ItemToPurchase with validated user inputs
    return ItemToPurchase(name, price, quantity, description)

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # Initialize the shopping cart with customer name and current date
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        # Add an item to the shopping cart
        self.cart_items.append(item)

    def remove_item(self, item_name):
        # Remove an item from the shopping cart by name
        item_found = False
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        # Modify an item's quantity. Outputs a message if item not found
        item_found = False
        for cart_item in self.cart_items:
            if cart_item.name == item.name:
                cart_item.quantity = item.quantity
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        # Returns the total quantity of all items in the cart
        total_quantity = sum(item.quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        # Determines and returns the total cost of the items in the cart
        total_cost = sum(item.price * item.quantity for item in self.cart_items)
        return total_cost
    
    def print_total(self):
        # Outputs the total number of items and their total cost in the shopping cart
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        total_cost = 0
        for item in self.cart_items:
            item_cost = item.price * item.quantity
            print(f"{item.name} {item.quantity} @ ${item.price} = ${item_cost}")
            total_cost += item_cost
        print(f"\nTotal: ${total_cost}")

    def print_descriptions(self):
        # Outputs each item's description in the cart
        print(f"{self.customer_name}'s Shopping Cart – {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

def print_menu(cart):
    # Menu options dictionary
    menu_options = {
        'a': 'Add item to cart',
        'r': 'Remove item from cart',
        'c': 'Change item quantity',
        'i': 'Output items\' descriptions',
        'o': 'Output shopping cart',
        'q': 'Quit'
    }

    # Execute the menu options until the user chooses to quit
    while True:
        print("\nMENU")
        for option, description in menu_options.items():
            print(f"{option} - {description}")
        
        option = input("Choose an option:\n")

        if option == 'q':
            break
        elif option == 'a':
            # Add item to cart
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)
        elif option == 'r':
            # Remove item from cart
            name = input("Enter the name of the item to remove:\n")
            cart.remove_item(name)
        elif option == 'c':
            # Change item quantity
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            item = ItemToPurchase(name=name, quantity=quantity)
            cart.modify_item(item)
        elif option == 'i':
            # Output items' descriptions
            cart.print_descriptions()
        elif option == 'o':
            # Output shopping cart
            cart.print_total()
        else:
            print("Invalid option. Please choose again.")
            
def main():
    # Main function to run the program
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)
    
    # Get details for two items from the user
    first_item = get_item_details(1)
    second_item = get_item_details(2)

    # Output the total cost of the two items
    print("\nTOTAL COST")
    first_item.print_item_cost()
    second_item.print_item_cost()
    total_cost = (first_item.price * first_item.quantity) + (second_item.price * second_item.quantity)
    print(f"\nTotal: ${total_cost}")
    
    # Add the items to the shopping cart
    cart.add_item(first_item)
    cart.add_item(second_item)

    # Call print_menu function with the created shopping cart
    print_menu(cart)

if __name__ == "__main__":
    main()