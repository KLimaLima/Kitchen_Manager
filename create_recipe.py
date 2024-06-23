from storage import Recipe_Storage
from ui_menu import *
from main_kitchen_storage import create_ingredient_main_storage

def create_recipe_part():

    recipe_name = str(input('\nEnter recipe name: '))

    recipe = Recipe_Storage(name= recipe_name)    

    ingredient_storage = adding_ingredient(recipe)

    recipe.save()

def adding_ingredient(recipe_storage:Recipe_Storage):

    recipe_storage.reset_storage()

    while True:
        
        print(f'\nIngredients available in main storage:\n{recipe_storage.get_kitchen_storage()}\nCurrent ingredients in recipe:\n{recipe_storage.get_storage()}')
        ingredient_to_add = input('Enter an ingredient based on main storage or enter [Z] to finish: ')
        ingredient_to_add = ingredient_to_add.lower()

        if ingredient_to_add == 'z':
            break

        # true if there is already in main storage, no need to add to main storage
        if ingredient_to_add in recipe_storage.get_kitchen_storage().keys():

            print('How much?')
            how_much = ui_get_int_positive()

            recipe_storage.set_ingredient_amount(ingredient_to_add, how_much)
            continue

        print('\nThe ingredient you entered does not exist in the main storage\nWould you like to add it into the main storage?')
        if ui_boolean_yes_or_no():
            
            print('\nPlease re-enter the ingredient to create in main storage')
            ingredient_to_add = create_ingredient_main_storage()

            print('How much?')
            how_much = ui_get_int_positive()

            recipe_storage.set_ingredient_amount(ingredient_to_add, how_much)

            continue

        print('\nInvalid input!\nPlease try again')

    return recipe_storage