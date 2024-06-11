class Menu:

    def __init__(self, name, total_price, ingredient) -> None:
        self.name = name
        self.total_price = total_price
        self.ingredient = ingredient

class Food(Menu):

    pass

class Beverage(Menu):

    def __init__(self, name, total_price, ingredient, temperature) -> None:
        Menu.__init__(name, total_price, ingredient)
        self.temperature = temperature