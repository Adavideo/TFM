from .input_output_files import texts_path, store_text_dataset
from sklearn.datasets import load_files

def load_dataset_from_texts():
    description = "Texts examples extracted form news and comments from Meneame"
    dataset = load_files(container_path=texts_path, description=description, shuffle=True, encoding="utf-8")
    return dataset

def load_and_store_dataset():
    dataset = load_dataset_from_texts()
    store_text_dataset(dataset)
    return dataset
