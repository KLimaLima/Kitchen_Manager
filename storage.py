class storage:

    def __init__(self):
        self.__ingredient = dict()

    def add_to_storage(self, ingredient, amount):
        self.__ingredient[ingredient] = self.__ingredient.get(ingredient, 0) + amount

    def set_to_storage(self, ingredient, amount):
        self.__ingredient[ingredient] = amount