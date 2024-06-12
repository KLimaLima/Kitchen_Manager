class Menu:

    def __init__(self, name, total_price, ingredient, recipe):
        self.name = name
        self.total_price = total_price
        self.ingredient = ingredient
        self.recipe = recipe

class Food(Menu):

    def __init__(self, name, total_price, ingredient, recipe, food_type):
        Menu.__init__(name, total_price, ingredient, recipe)
        self.food_type = food_type

class Beverage(Menu):

    def __init__(self, name, total_price, ingredient, temperature):
        Menu.__init__(name, total_price, ingredient)
        self.temperature = temperature