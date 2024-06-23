import storage
from ui_menu import ui_get_user_input
from main_kitchen_storage import kitchen_storage_ui
from create_recipe import create_recipe_part
from shopping_list2 import *
from find_recipe import get_list_recipe_storage

kitchen_storage = storage.Kitchen_Storage()

while True:

    # just to make a line space
    print('')

    # display menu and get user input
    user_input = ui_get_user_input(A= 'Create Recipe', B= 'Get All Recipe', C= 'Kitchen Storage', D= 'Shopping List')

    if user_input == 'A':
        create_recipe_part()

    elif user_input == 'B':
        get_list_recipe_storage()

    elif user_input == 'C':
        kitchen_storage_ui()

    elif user_input == 'D':
        shopping_list_part()

    elif user_input == 'Z':
        print('Closing program...')
        break

    # just in case
    else:
        print('Invalid input!\nPlease try again')