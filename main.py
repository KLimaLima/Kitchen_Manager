import file_reader
import storage

kitchen_storage = storage.Kitchen_Storage()

print("kitchen storage")
print(kitchen_storage.get_storage())

##############################################################

# data = {'bawang': 12,'ayam': 1,'sayur': 5,'cili': 20,'beras': 50}

# file_reader.write_csv_one_row(file_reader.KITCHEN_STORAGE, data)

# b = file_reader.read_csv_one_row(file_reader.KITCHEN_STORAGE)

menu_ingredients = storage.Storage()

print(menu_ingredients.get_storage())
# print(menu_ingredients.get_kitchen_storage())

# menu_ingredients.add_one("bawang", 20)

# print(menu_ingredients.get_storage())

# menu_ingredients.add_one("bawang", -10)
# menu_ingredients.add_one("beras", 10)

# print(menu_ingredients.get_storage())

print(menu_ingredients.write_data_csv("a_storage.csv"))

menu_ingredients.set_one("ikan", 2)

print(menu_ingredients.get_storage())