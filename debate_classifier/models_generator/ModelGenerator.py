from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
from .stop_words.stop_words import get_stop_words


class ModelGenerator:

    def __init__(self, documents):
        self.documents = documents
        self.vectorizer = TfidfVectorizer(stop_words=get_stop_words())

    # Process the documents with the vectorizer.
    def process_documents(self):
        print("Procesing "+str(len(self.documents))+" documents")
        self.vectorized_documents = self.vectorizer.fit_transform(self.documents)
        return self.vectorized_documents

    def train_model(self):
        print("Training model")
        model = AffinityPropagation()
        model.fit(self.vectorized_documents)
        return model

    def generate_model(self):
        self.process_documents()
        model = self.train_model()
        return model
