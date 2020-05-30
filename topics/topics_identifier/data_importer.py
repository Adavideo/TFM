from .input_output_files import texts_path, store_text_dataset
from sklearn.datasets import load_files

def load_dataset_from_texts(description):
    dataset = load_files(container_path=texts_path, description=description, shuffle=True, encoding="utf-8")
    return dataset

def load_and_store_dataset(dataset_name, description):
    print("Loading dataset "+dataset_name+" from texts files.")
    dataset = load_dataset_from_texts(description)
    print("Dataset "+dataset_name+" loaded. Storing dataset.")
    store_text_dataset(dataset, dataset_name)
    print("Dataset "+dataset_name+" stored.")
    return dataset
