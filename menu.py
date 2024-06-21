import storage

class Food:

    def __init__(self, name, total_price, storage, recipe):
        self.name = name
        self.total_price = total_price
        self.ingredient = storage
        self.recipe = recipe

class Meal(Food):

    def __init__(self, name, total_price, ingredient, recipe, food_type):
        Food.__init__(name, total_price, ingredient, recipe)
        self.food_type = food_type

class Beverage(Food):

    def __init__(self, name, total_price, ingredient, temperature):
        Food.__init__(name, total_price, ingredient)
        self.temperature = temperature

class Raw_Food(Food):

    def __init__(self, name, total_price, storage, recipe):
        Food.__init__(name, total_price, storage, recipe)