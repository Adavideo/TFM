from joblib import load
from config import sklearn_models_path


def get_filename(type, level, name):
    name = name.replace(" ","-")
    filename = sklearn_models_path + name + "_" + type + "_level" + str(level) + ".joblib"
    return filename

def load_object(type, level, name):
    filename = get_filename(type, level, name)
    try:
        object = load(filename)
        return object
    except:
        print("ERROR: Could not load "+name+" "+type+" from "+filename)
        return None

def model_created(name):
    model = load_object("model", level=0, name=name)
    if model: return True
    else: return False
