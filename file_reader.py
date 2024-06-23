import os
import csv

# read a txt file
def read_txt(file_name):

    have_file = os.path.isfile(file_name)

    # handle no file
    if (not have_file):
        write_txt(file_name= file_name, array_data= "")

    # read data and put in list
    reading = open(file_name, "r")
    file_data = reading.readlines()
    reading.close()

    for i in range(len(file_data)):
        data_string = file_data[i]
        file_data[i] = data_string[:-1]

    return file_data

# write to a txt file
def write_txt(file_name, array_data):

    # write to the txt file
    writing = open(file_name, "w")
    for data in array_data:
        writing.write(data)
    writing.close()

def append_txt(file_name, array_data):

    have_file = os.path.isfile(file_name)

    if(not have_file):
        write_txt(file_name= file_name, array_data= "")

    appending = open(file_name, "a")
    for data in array_data:
        appending.write(data)
    appending.close()

# read a csv file that has only one row
def read_csv_one_row(file_name):
    
    have_data = read_txt(file_name= file_name)
    have_file = os.path.isfile(file_name)

    # handle empty and no file
    if (not have_file or not have_data):
        return dict()
    
    # read with csv dictreader to get data as dict
    reading = open(file_name, "r")
    csv_reader = csv.DictReader(reading)

    # since there is only one data(row), only one variable
    for data in csv_reader:
        csv_data_one_row = data
    
    reading.close()
    return csv_data_one_row

# write to a csv file for only one row
def write_csv_one_row(file_name, dict_data: dict):

    # get a list of keys
    list_key = list(dict_data.keys())

    # write to csv with dictwriter
    writing = open(file_name, "w")
    csv_write = csv.DictWriter(writing, fieldnames= list_key)
    csv_write.writeheader()
    csv_write.writerow(dict_data) # use writerow because only one row
    writing.close()

# generate file name
def generate_file_name(file_type_without_dot, *args_names):

    # take all name and combine them
    base_file_name = "_".join(args_names)
    
    count = 0
    # this imitates c++ do while
    while True:

        # create the FULL file name
        file_name = f"{base_file_name}_{count}.{file_type_without_dot}"
        
        # check if there is already a file with that name
        have_file = os.path.isfile(file_name)
        if not have_file:
            break

        # increment counter to make a unique file name
        count += 1

    return base_file_name

# this one reads csv file into dict and converts values into int
def read_csv_one_row_value_int(file_name):

    data_dict = read_csv_one_row(file_name)

    for key, value in data_dict.items():
        data_dict[key] = int(value)

    return data_dict