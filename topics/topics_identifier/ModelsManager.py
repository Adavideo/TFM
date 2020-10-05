from joblib import load
from config import sklearn_models_path


class ModelsManager:

    def __init__(self, name):
        self.name = name.replace(" ","-")

    def get_filename(self, type, level):
        filename = sklearn_models_path + self.name + "_" + type + "_level" + str(level) + ".joblib"
        return filename

    def load_object(self, type, level):
        filename = self.get_filename(type=type, level=level)
        try:
            object = load(filename)
            return object
        except:
            return None
