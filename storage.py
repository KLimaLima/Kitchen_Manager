import file_reader

KITCHEN_STORAGE = "kitchen_storage.csv"
RECIPE_STORAGE = "recipe_storage.txt"

# storage boleh dikira sebagai jumlah bahan2(utk recipe) yg diperlukan juga
class Storage:

    # best practice to declare parameter type for easier use at other parts
    def __init__(self, ingredient:dict = dict()):
        self.__ingredient = ingredient

    # increment/decrement ONE ingredient in storage; Also adds it if it does not exist
    def add_ingredient_amount(self, ingredient, add_amount):
        self.__ingredient[ingredient] = self.__ingredient.get(ingredient, 0) + add_amount

    # sets ONE ingredient(will overwrite if already exist)
    def set_ingredient_amount(self, ingredient, set_amount):
        self.__ingredient[ingredient] = set_amount

    def set_ingredient_dict(self, ingredient:dict):
        self.__ingredient = ingredient

    def del_ingredient(self, ingredient):
        del self.__ingredient[ingredient]

    # get the ingredients currently available
    def get_storage(self):
        return self.__ingredient
    
    # all storage(bahan2 utk recipe) can access kitchen storage
    def get_kitchen_storage(self):
        storage_data = file_reader.read_csv_one_row_value_int(KITCHEN_STORAGE)
        return storage_data
    
    def save(self, file_name):
        file_reader.write_csv_one_row(file_name, self.__ingredient)

# the main kitchen storage that holds all raw ingredients
class Kitchen_Storage(Storage):

    # the ingredient must be taken from csv storage
    def __init__(self):
        self.__ingredient = self.get_kitchen_storage()

        Storage.__init__(self, self.__ingredient)

    # gets the latest update of the main storage
    def update_latest(self):
        self.__ingredient = self.get_kitchen_storage()

    def save(self):
        file_reader.write_csv_one_row(KITCHEN_STORAGE, self.__ingredient)

class Recipe_Storage(Storage):

    def __init__(self, ingredient: dict = dict(), name = 'no name'):
        self.__ingredient = ingredient
        self.__name = name
        
        Storage.__init__(self, ingredient)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def save(self):
        array_data = []

        data_name = f'recipe:{self.get_name()}'
        array_data.append(str(data_name))

        for ingredient, amount in self.get_storage().items():
            array_data.append('\n')
            array_data.append(str(ingredient))
            array_data.append('\n')
            array_data.append(str(amount))

        array_data.append('\n')

        file_reader.append_txt(RECIPE_STORAGE, array_data)

    def reset_storage(self):

        for ingredient in list(self.__ingredient):
            del self.__ingredient[ingredient]