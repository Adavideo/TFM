from joblib import dump
from config import sklearn_models_path
from .ModelGenerator import ModelGenerator
from .reference_documents_generator import generate_reference_documents


class ModelsManager:

    def __init__(self, name):
        self.name = name
        self.initialize_levels_information()

    def initialize_levels_information(self):
        self.models_filenames = []
        self.vectorizers_filenames = []
        self.reference_documents_filenames = []

    def get_filename(self, type, level):
        filename = sklearn_models_path + self.name + "_" + type + "_level" + str(level) + ".joblib"
        return filename

    def store_object(self, object, type, level):
        filename = self.get_filename(type, level)
        dump(object, filename)
        return filename

    def store_level_information(self, model, vectorizer, reference_documents, level):
        print("Storing level "+str(level)+" model")
        model_filename = self.store_object(model, type="model", level=level)
        self.models_filenames.append(model_filename)
        vectorizer_filename = self.store_object(vectorizer, type="vectorizer", level=level)
        self.vectorizers_filenames.append(vectorizer_filename)
        reference_docs_filename = self.store_object(reference_documents, type="reference_documents", level=level)
        self.reference_documents_filenames.append(reference_docs_filename)

    def get_filenames(self):
        filenames = {
            "models": self.models_filenames,
            "vectorizers": self.vectorizers_filenames,
            "reference_documents": self.reference_documents_filenames
        }
        return filenames

    def generate_and_store_models(self, documents, max_level):
        self.initialize_levels_information()
        for level in range(max_level+1):
            print("\nGenerating level "+str(level)+" model with "+str(len(documents))+ " documents")
            model_generator = ModelGenerator(documents)
            model = model_generator.generate_model()
            vectorizer = model_generator.vectorizer
            reference_documents = generate_reference_documents(self, model, vectorizer, documents, level)
            self.store_level_information(model, vectorizer, reference_documents, level)
            documents = reference_documents
        filenames = self.get_filenames()
        return filenames
