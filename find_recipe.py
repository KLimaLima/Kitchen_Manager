import file_reader
from ui_menu import *
from storage import *

def get_list_recipe_storage():

    list_to_convert = file_reader.read_txt(RECIPE_STORAGE)

    list_recipe = []

    if not list_to_convert:
        print('You have no recipe created\nCreate a recipe to populate your recipe')
        return list_recipe
    
    i = 0
    while i < len(list_to_convert):

        if list_to_convert[i].startswith('recipe:'):

            print('\nRecipe:', list_to_convert[i][7:])

            i += 1

            print('Ingredient:')

            continue

        print(list_to_convert[i], list_to_convert[i+1])

        i += 2