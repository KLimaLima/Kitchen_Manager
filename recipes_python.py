#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     21/06/2024
# Copyright:   (c) User 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Predefined list of ingredients
available_ingredients = ["bawang", "ayam", "sayur", "cili", "beras"]

# Function to add recipes from a file
def add_recipes_from_file(filename, recipes):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        current_recipe = {}
        for line in lines:
            line = line.strip()
            if line.startswith("Recipe:"):
                if current_recipe:
                    recipes.append(current_recipe)
                current_recipe = {"name": line.split(":", 1)[1].strip(), "ingredients": []}
            elif line.startswith("Ingredients:"):
                ingredients = line.split(":", 1)[1].strip().split(", ")
                current_recipe["ingredients"] = [ing for ing in ingredients if ing in available_ingredients]

        if current_recipe:
            recipes.append(current_recipe)

    except FileNotFoundError:
        print(f"{filename} not found.")
        return

# Function to save recipes to a text file
def save_recipes_to_file(recipes, filename="recipes.txt"):
    try:
        with open(filename, 'w') as file:
            for recipe in recipes:
                file.write(f"Recipe: {recipe['name']}\n")
                file.write(f"Ingredients: {', '.join(recipe['ingredients'])}\n\n")
        print(f"Recipes saved to {filename}")
    except IOError as e:
        print(f"An error occurred while saving the recipes: {e}")

# Function to load recipes from a text file
def load_recipes_from_file(filename="recipes.txt"):
    recipes = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        current_recipe = {}
        for line in lines:
            line = line.strip()
            if line.startswith("Recipe:"):
                if current_recipe:
                    recipes.append(current_recipe)
                current_recipe = {"name": line.split(":", 1)[1].strip(), "ingredients": []}
            elif line.startswith("Ingredients:"):
                ingredients = line.split(":", 1)[1].strip().split(", ")
                current_recipe["ingredients"] = ingredients

        if current_recipe:
            recipes.append(current_recipe)

    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        pass

    return recipes

# Main program
def main():
    recipes = load_recipes_from_file()

    input_filename = "input_recipes.txt"
    add_recipes_from_file(input_filename, recipes)

    save_recipes_to_file(recipes)

if __name__ == "__main__":
    main()