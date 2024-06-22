# flexible ui that gets user input and validates it
def ui_get_user_input(**kwargs_letter_message):

    while True:

        # this is the ui
        for letter, message in kwargs_letter_message.items():
            print(f'[{letter}] {message}')

        # since all have this
        print('[Z] Exit')

        # standardise input
        user_input = str(input("Enter a key: "))
        user_input = user_input.upper()

        # validise input
        if user_input in kwargs_letter_message.keys() or user_input == 'Z':
            break
        
        # invalid so no break
        print('Invalid input!\nPlease try again')

    
    # return upper version of valid user input
    return user_input

# get user data that exist in dict key
def ui_find_in_dict(my_dict: dict):

    while True:

        for key, value in my_dict.items():
            print(f'{key}: {value}')

        user_input = str(input("Type your choice: "))
        user_input = user_input.lower()

        if user_input in my_dict.keys():
            break

        print('Invalid input!\nPlease try again')

    return user_input

# get user input for positive int
def ui_get_int_positive():

    while True:

        user_input = input("Enter a positive integer: ")

        # to check if it is integer, only integer is allowed
        if user_input.isdigit():
            user_input = int(user_input)
            break

        print('Invalid input!\nPlease try again')

    return user_input