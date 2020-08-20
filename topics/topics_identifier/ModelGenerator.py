from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
from .stop_words.stop_words import get_stop_words


class ModelGenerator:

    def __init__(self, documents):
        self.documents = documents
        self.vectorizer = TfidfVectorizer(stop_words=get_stop_words())

    # Process the documents with the vectorizer.
    def process_documents(self, documents=[]):
        if not documents: documents = self.documents
        self.vectorized_documents = self.vectorizer.fit_transform(documents)

    def get_all_terms(self):
        all_terms = self.vectorizer.get_feature_names()
        return all_terms

    def train_model(self):
        model = AffinityPropagation()
        model.fit(self.vectorized_documents)
        return model

    def generate_model(self):
        self.process_documents()
        self.all_terms = self.get_all_terms()
        model = self.train_model()
        return model
