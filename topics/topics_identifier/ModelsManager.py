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

    def get_model_filename(self, level):
        filename = sklearn_models_path + self.name + "_model_level" + str(level) + ".joblib"
        return filename

    def get_vectorizer_filename(self, level):
        filename = sklearn_models_path + self.name + "_vectorizer_level" + str(level) + ".joblib"
        return filename

    def store_model(self, model, level):
        filename = self.get_model_filename(level)
        dump(model, filename)
        return filename

    def store_vectorizer(self, vectorizer, level):
        filename = self.get_vectorizer_filename(level)
        dump(vectorizer, filename)
        return filename

    def load_model(self, level):
        filename = self.get_model_filename(level)
        try:
            model = load(filename)
            return model
        except:
            return None

    def load_vectorizer(self, level):
        filename = self.get_vectorizer_filename(level)
        try:
            vectorizer = load(filename)
            return vectorizer
        except:
            return None

    def get_next_level_documents(self, model, vectorizer, documents):
        clusters_generator = ClustersGenerator(model, vectorizer, documents)
        clusters_information = clusters_generator.get_clusters_information()
        return clusters_information["reference_documents"]

    def store_level_information(self, model, vectorizer, level):
        model_filename = self.store_model(model, level)
        self.models_filenames.append(model_filename)
        vectorizer_filename = self.store_vectorizer(vectorizer, level)
        self.vectorizers_filenames.append(vectorizer_filename)

    def generate_and_store_models(self, documents, max_level):
        self.initialize_levels_information()
        for level in range(0, max_level+1):
            model_generator = ModelGenerator(documents)
            model = model_generator.generate_model()
            vectorizer = model_generator.vectorizer
            self.store_level_information(model, vectorizer, level)
            if level < max_level+1:
                documents = self.get_next_level_documents(model, vectorizer, documents)
        return self.models_filenames[max_level]
