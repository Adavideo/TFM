from joblib import dump, load
from .ModelGenerator import ModelGenerator
from .ClustersGenerator import ClustersGenerator
from .paths import sklearn_models_path


class ModelsManager:

    def __init__(self, name):
        self.name = name
        self.initialize_levels_information()

    def initialize_levels_information(self):
        self.models_filenames = []
        self.vectorizers_filenames = []

    def get_filename(self, type, level):
        filename = sklearn_models_path + self.name + "_" + type + "_level" + str(level) + ".joblib"
        return filename

    def store_object(self, object, type, level):
        filename = self.get_filename(type, level)
        dump(object, filename)
        return filename

    def load_object(self, type, level):
        filename = self.get_filename(type=type, level=level)
        try:
            object = load(filename)
            return object
        except:
            return None

    def get_next_level_documents(self, model, vectorizer, documents):
        clusters_generator = ClustersGenerator(model, vectorizer, documents)
        reference_documents = clusters_generator.get_clusters_reference_documents()
        return reference_documents

    def store_level_information(self, model, vectorizer, level):
        model_filename = self.store_object(model, type="model", level=level)
        self.models_filenames.append(model_filename)
        vectorizer_filename = self.store_object(vectorizer, type="vectorizer", level=level)
        self.vectorizers_filenames.append(vectorizer_filename)

    def generate_and_store_models(self, documents, max_level):
        self.initialize_levels_information()
        for level in range(max_level+1):
            model_generator = ModelGenerator(documents)
            model = model_generator.generate_model()
            vectorizer = model_generator.vectorizer
            self.store_level_information(model, vectorizer, level)
            if level < max_level+1:
                documents = self.get_next_level_documents(model, vectorizer, documents)
        return self.models_filenames[max_level]
