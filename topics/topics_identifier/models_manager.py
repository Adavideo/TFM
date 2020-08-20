from joblib import dump, load

path = "models/sklearn/"

def get_filename(name):
    filename = path + name + ".joblib"
    return filename

def store_model(model, name):
    filename = get_filename(name)
    dump(model, filename)

def load_model(name):
    filename = get_filename(name)
    model = load(filename)
    return model
