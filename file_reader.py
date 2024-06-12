import os

def read_file(file_name):

    if (not os.path.isfile(file_name)):
        write_file(file_name= file_name, array_data= "")

    reading = open(file_name, "r")

    file_data = reading.readlines()

    reading.close

    return file_data

def write_file(file_name, array_data):

    writing = open(file_name, "w")

    for data in array_data:
        writing.write(data)

    writing.close