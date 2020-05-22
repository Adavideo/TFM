from sklearn.datasets import load_files

def load_dataset():
    data_path = "data"
    dataset = load_files(data_path, shuffle=True, encoding="utf-8")
    num_examples = len(dataset.data)
    print("Loaded dataset with " + str(num_examples) + " examples")
    return dataset
