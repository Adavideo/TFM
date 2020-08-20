from joblib import dump, load

path = "models/sklearn/"

def get_filename(name, level):
    filename = path + name + "_level" + str(level) + ".joblib"
    return filename

def store_model(model, name, level):
    filename = get_filename(name, level)
    dump(model, filename)

def load_model(name, level):
    filename = get_filename(name, level)
    model = load(filename)
    return model
