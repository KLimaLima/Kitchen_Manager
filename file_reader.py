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

    return file_data

# write to a txt file
def write_txt(file_name, array_data):

    # write to the txt file
    writing = open(file_name, "w")
    for data in array_data:
        writing.write(data)
    writing.close()

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