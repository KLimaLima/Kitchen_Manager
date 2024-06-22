import file_reader
import storage
from ui_menu import ui_get_user_input
from main_kitchen_storage import kitchen_storage_ui

test_kitchen_storage = storage.Kitchen_Storage()

print("kitchen storage")
print(test_kitchen_storage.get_storage())

##############################################################

# data = {'bawang': 12,'ayam': 1,'sayur': 5,'cili': 20,'beras': 50}

# file_reader.write_csv_one_row(file_reader.KITCHEN_STORAGE, data)

# b = file_reader.read_csv_one_row(file_reader.KITCHEN_STORAGE)

menu_ingredients = storage.Storage()

print(menu_ingredients.get_storage())
# print(menu_ingredients.get_kitchen_storage())

# menu_ingredients.add_one("bawang", 20)

# print(menu_ingredients.get_storage())

# menu_ingredients.add_one("bawang", -10)
# menu_ingredients.add_one("beras", 10)

# print(menu_ingredients.get_storage())

print(menu_ingredients.save("a_storage.csv"))

menu_ingredients.set_ingredient_amount("ikan", 2)

print(menu_ingredients.get_storage())

##################################################################

kitchen_storage = storage.Kitchen_Storage()

while True:

    # display menu and get user input
    user_input = ui_get_user_input(A= 'Create Recipe', B= 'Find Recipe', C= 'Kitchen Storage', D= 'Print Shopping List')

    if user_input == 'A':
        print('a masuk')

    elif user_input == 'B':
        print('b masuk')

    elif user_input == 'C':
        kitchen_storage_ui()

    elif user_input == 'D':
        print('d masuk')

    elif user_input == 'Z':
        print('Closing program...')
        break
    
    # just in case
    else:
        print('Invalid input!\nPlease try again')