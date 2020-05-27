import os, json
import numpy as np
from sklearn.datasets.base import Bunch

texts_path = "data/texts/"
texts_import_path = texts_path+"to_classify/"
text_datasets_path = "data/text_datasets/"
clusters_path = "data/clusters/"
stop_words_filename = "data/stop_words_spanish.txt"

def count_existing_files(directory="", type=""):
    if not directory:
        if type == "text_dataset":
            directory = text_datasets_path
        else:
            directory = texts_import_path
    number_of_files = len(os.listdir(directory))
    return number_of_files

def store_file(filename, content):
    out_file = open(filename, 'w')
    out_file.write(content)
    out_file.close()

def store_text_in_file(text, file_number):
    filename = texts_import_path + "text" + str(file_number) + ".txt"
    store_file(filename, text)

def store_text_dataset(dataset):
    file_number = int(count_existing_files(text_datasets_path) / 5) + 1
    dataname = text_datasets_path + "text_dataset" + str(file_number)
    np.save(dataname + '_data.npy', dataset.data)
    np.save(dataname + '_filenames.npy', dataset.filenames)
    np.save(dataname + '_target.npy', dataset.target)
    np.save(dataname + '_target_names.npy', dataset.target_names)
    np.save(dataname + '_descr.npy', dataset.DESCR)

def load_dataset():
    files = os.listdir(text_datasets_path)
    if len(files) == 0:
        return None
    #filename = text_datasets_path + files[0]
    dataname = text_datasets_path + "text_dataset1"
    dataset = Bunch()
    dataset['data'] = np.load(dataname+'_data.npy')
    dataset['target'] = np.load(dataname+'_target.npy')
    dataset['target_names'] = np.load(dataname+'_target_names.npy')
    dataset['DESCR'] = np.load(dataname+'_descr.npy')
    return dataset

def get_stop_words():
    stop_words = []
    file = open(stop_words_filename, 'r')
    words_from_file = file.read().split("\n")
    file.close()
    for word in words_from_file:
        stop_words.append(word)
    return stop_words

def store_clustered_documents(clustered_documents):
    file_number = count_existing_files(clusters_path) + 1
    filename = clusters_path + "clusters_" + str(len(clustered_documents)) + "_" + str(file_number) + ".txt"
    out_file = open(filename, 'w')
    count = 0
    for cluster in clustered_documents:
        out_file.write("Cluster "+str(count)+". Terms: ")
        out_file.write(str(cluster["terms"])+"\n")
        for document in cluster["documents"]:
            out_file.write(document+"\n")
        out_file.write("\n")
        count += 1
    out_file.close()
