import os
import numpy as np
from sklearn.datasets import load_files
from sklearn.datasets.base import Bunch
from .file_paths import texts_path, text_datasets_path

def load_dataset_from_texts(description):
    dataset = load_files(container_path=texts_path, description=description, shuffle=True, encoding="utf-8")
    return dataset

def load_dataset(data_name):
    data_file = text_datasets_path + data_name
    dataset = Bunch()
    dataset['data'] = np.load(data_file+'__data.npy')
    dataset['target'] = np.load(data_file+'__target.npy')
    dataset['target_names'] = np.load(data_file+'__target_names.npy')
    dataset['DESCR'] = np.load(data_file+'__descr.npy')
    return dataset

def store_text_dataset(dataset, dataset_name):
    dataname = text_datasets_path + dataset_name.replace(" ", "")
    np.save(dataname + '__data.npy', dataset.data)
    np.save(dataname + '__filenames.npy', dataset.filenames)
    np.save(dataname + '__target.npy', dataset.target)
    np.save(dataname + '__target_names.npy', dataset.target_names)
    np.save(dataname + '__descr.npy', dataset.DESCR)

def load_and_store_dataset(dataset_name, description):
    print("Loading dataset "+dataset_name+" from texts files.")
    dataset = load_dataset_from_texts(description)
    print("Dataset "+dataset_name+" loaded. Storing dataset.")
    store_text_dataset(dataset, dataset_name)
    print("Dataset "+dataset_name+" stored.")
    return dataset

def get_datasets_names_from_files():
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
