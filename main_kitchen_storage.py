from storage import Kitchen_Storage
from ui_menu import *

def kitchen_storage_ui():

    while True:

        user_input = ui_get_user_input(A= 'Add/Subtract ingredient', B= 'Create/Remove ingredient', C= 'Display')
        
        if user_input == 'A':
            add_sub_ingredient()

        elif user_input == 'B':
            create_remove_ingredient()

        elif user_input == 'C':
            main_storage = Kitchen_Storage()

            print(main_storage.get_storage())

        elif user_input == 'Z':
            break

        # just in case
        else:
            print('Invalid input!\nPlease try again')

def add_sub_ingredient():

    main_storage = Kitchen_Storage()

    positive_or_negative = ui_get_user_input(A= 'Add', B= 'Subtract')

    if positive_or_negative == 'A':
        number_sign = 1
    elif positive_or_negative == 'B':
        number_sign = -1
    else:
        print('There was an error! Please try again')
        return

    the_ingredient = ui_find_in_dict(main_storage.get_storage())

    how_much = ui_get_int_positive()

    main_storage.add_ingredient_amount(the_ingredient, number_sign * how_much)

    # update memory smth like that
    main_storage.save()

def create_remove_ingredient():

    create_or_remove = ui_get_user_input(A= 'Create', B= 'Remove')

    if create_or_remove == 'A':

        create_ingredient_main_storage()

    # remove is only used here, no need to make modular
    elif create_or_remove == 'B':

        main_storage = Kitchen_Storage()
        
        remove_ingredient = ui_find_in_dict(main_storage.get_storage())

        main_storage.del_ingredient(remove_ingredient)

        # update memory
        main_storage.save()

    else:
        print('There was an error! Please try again')
        return
    
def create_ingredient_main_storage():

    main_storage = Kitchen_Storage()

    while True:

        create_ingredient = input('Enter the ingredient name(in lower case): ')
        create_ingredient = create_ingredient.lower()

        if create_ingredient not in main_storage.get_storage().keys():
            main_storage.add_ingredient_amount(create_ingredient, 0)
            break

        print('Invalid input!\nPlease try again')

    main_storage.save()

    return create_ingredient