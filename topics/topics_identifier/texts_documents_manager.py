import os
from .file_paths import texts_path

def count_existing_files(directory="", type=""):
    if not directory:
        if type == "text_dataset":
            directory = text_datasets_path
        elif type == "news" or type == "comments":
            directory = texts_path + type + "/"
        else:
            print("File type not recognised")
            return None
    number_of_files = len(os.listdir(directory))
    return number_of_files

def store_file(filename, content):
    out_file = open(filename, 'w')
    out_file.write(content)
    out_file.close()

def store_text_in_file(text, file_type, data_name, file_number):
    filename = texts_path + file_type + "/" + data_name + "_" + str(file_number) + ".txt"
    store_file(filename, text)

def short_texts_filenames(full_filenames_list):
    short_filenames_list = []
    for filename in full_filenames_list:
        _, short_filename = filename.split(texts_path)
        short_filenames_list.append(short_filename)
    return short_filenames_list
