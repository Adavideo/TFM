import os
import numpy as np
from sklearn.datasets.base import Bunch

texts_path = "data/texts/"
text_datasets_path = "data/text_datasets/"
clusters_path = "data/clusters/"
stop_words_filename = "data/stop_words_spanish.txt"

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

def store_text_dataset(dataset, dataset_name):
    file_number = int(count_existing_files(text_datasets_path) / 5) + 1
    dataname = text_datasets_path + dataset_name.replace(" ", "")
    np.save(dataname + '__data.npy', dataset.data)
    np.save(dataname + '__filenames.npy', dataset.filenames)
    np.save(dataname + '__target.npy', dataset.target)
    np.save(dataname + '__target_names.npy', dataset.target_names)
    np.save(dataname + '__descr.npy', dataset.DESCR)

def get_datasets_names():
    files = os.listdir(text_datasets_path)
    if len(files) == 0:
        return None
    else:
        filenames = []
        for filename in files:
            name, rest = filename.split("__")
            if (name not in filenames):
                filenames.append(name)
        return filenames

def load_dataset(data_name):
    data_file = text_datasets_path + data_name
    dataset = Bunch()
    dataset['data'] = np.load(data_file+'__data.npy')
    dataset['target'] = np.load(data_file+'__target.npy')
    dataset['target_names'] = np.load(data_file+'__target_names.npy')
    dataset['DESCR'] = np.load(data_file+'__descr.npy')
    return dataset

def get_stop_words():
    stop_words = []
    file = open(stop_words_filename, 'r')
    words_from_file = file.read().split("\n")
    file.close()
    for word in words_from_file:
        stop_words.append(word)
    return stop_words

def store_clusters(clusters_info):
    file_number = count_existing_files(clusters_path) + 1
    filename = clusters_path + "clusters_" + str(len(clusters_info)) + "_" + str(file_number) + ".txt"
    out_file = open(filename, 'w')
    count = 0
    for cluster in clusters_info:
        out_file.write("Cluster "+str(count)+"\n")
        out_file.write("Terms: "+str(cluster["terms"])+"\n")
        out_file.write("Reference document:\n"+ cluster["reference_document"]+"\n")
        out_file.write("__________\n")
        out_file.write("Documents:\n")
        out_file.write("__________\n")
        for document in cluster["documents"]:
            out_file.write(document+"\n")
            out_file.write("__________\n")
        out_file.write("\n")
        count += 1
    out_file.close()

def short_texts_filenames(full_filenames_list):
    short_filenames_list = []
    for filename in full_filenames_list:
        _, short_filename = filename.split(texts_path)
        short_filenames_list.append(short_filename)
    return short_filenames_list
