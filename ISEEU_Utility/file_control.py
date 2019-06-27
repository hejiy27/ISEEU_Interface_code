import os

def Check_directory_exist(path):
    if os.path.exists(path):
        return True
    else:
        return False

def file_open(directory, file_name, file_option):
    if not Check_directory_exist(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory,file_name)
    return open(file_path,file_option)

def text_file_read(path,file_name):
    data_path = path
    data = open(data_path + file_name, 'r')
    return [line for line in data.read().split("\n") if line.strip() != '']