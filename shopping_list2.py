class ShoppingList:
    def __init__(self):
        self.groceries = []  # List to store grocery items

    def add_item(self, item_name, quantity, price_per_unit):
        """Add an item to the shopping list."""
        item = {
            'name': item_name,
            'quantity': quantity,
            'price_per_unit': price_per_unit
        }
        self.groceries.append(item)

    def remove_item(self, item_name):
        """Remove an item from the shopping list by name."""
        self.groceries = [item for item in self.groceries if item['name'] != item_name]

    def calculate_total_cost(self):
        """Calculate the total cost of the groceries."""
        total_cost = sum(item['quantity'] * item['price_per_unit'] for item in self.groceries)
        return total_cost

    def display_list(self):
        """Display the shopping list with item details."""
        print("Shopping List:")
        for item in self.groceries:
            print(f"Item: {item['name']}, Quantity: {item['quantity']}, Price per unit: ${item['price_per_unit']:.2f}")
        print(f"Total cost: ${self.calculate_total_cost():.2f}")

def shopping_list_part():
    shopping_list = ShoppingList()

    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Display list")
        print("4. Calculate total cost")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = float(input("Enter quantity: "))
            price_per_unit = float(input("Enter price per unit: "))
            shopping_list.add_item(item_name, quantity, price_per_unit)

        elif choice == '2':
            item_name = input("Enter item name to remove: ")
            shopping_list.remove_item(item_name)

        elif choice == '3':
            shopping_list.display_list()

        elif choice == '4':
            total_cost = shopping_list.calculate_total_cost()
            print(f"Total cost: ${total_cost:.2f}")

        elif choice == '5':
            break

        else:
            print("Invalid choice, please try again.")