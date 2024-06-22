#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Acer
#
# Created:     22/06/2024
# Copyright:   (c) Acer 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
class ShoppingList:
    def __init__(self):
        # Dictionary to store item prices
        self.item_prices = {
            'ayam': 8.50,
            'cili': 3.00,
            'bawang': 4.00,
            'sayur': 2.50,
            'beras': 6.00
        }
        # Dictionary to store quantities
        self.quantities = {}

    def add_item(self, item, quantity):
        """
        Add an item to the shopping list with specified quantity.
        """
        if item in self.item_prices:
            if quantity > 0:
                self.quantities[item] = quantity
            else:
                print("Quantity must be greater than zero.")
        else:
            print(f"{item} is not in the shopping list.")

    def calculate_total_cost(self):
        """
        Calculate the total cost of all items in the shopping list.
        """
        total_cost = 0.0
        for item, quantity in self.quantities.items():
            total_cost += quantity * self.item_prices[item]
        return total_cost

    def display_shopping_list(self):
        """
        Display the current shopping list with quantities.
        """
        print("\nYour Shopping List:")
        print("===================")
        for item, quantity in self.quantities.items():
            print(f"{item}: {quantity}")
        print("===================")


def main():
    # Create an instance of the ShoppingList class
    my_shopping_list = ShoppingList()

    print("Welcome to the Coding Class Shopping List!")
    print("========================================")

    # Input quantities for each item
    items = ['ayam', 'cili', 'bawang', 'sayur', 'beras']
    for item in items:
        while True:
            try:
                quantity = int(input(f"Enter quantity of {item}: "))
                my_shopping_list.add_item(item, quantity)
                break
            except ValueError:
                print("Invalid input. Please enter a valid quantity (e.g., 1, 2, 3).")

    # Display the shopping list
    my_shopping_list.display_shopping_list()

    # Calculate and display the total cost
    total_cost = my_shopping_list.calculate_total_cost()
    print(f"\nTotal Cost: RM {total_cost:.2f}")
    print("===================")


if __name__ == "__main__":
    main()
