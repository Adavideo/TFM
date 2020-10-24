from joblib import load
from .examples import test_model_name
from models_generator.ModelsManager import ModelsManager


def load_object(type, level, model_name=test_model_name):
    models_manager = ModelsManager(name=model_name)
    filename = models_manager.get_filename(type=type, level=level)
    try:
        object = load(filename)
        return object
    except:
        return None
