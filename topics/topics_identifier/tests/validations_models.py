from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
from topics_identifier.ModelsManager import ModelsManager
from .examples import example_documents_limit
from .example_trees import example_documents_clusters


def validate_model_stored(test, model_name, level):
    manager = ModelsManager(name=model_name)
    model = manager.load_model(level)
    test.assertEqual(type(model), type(AffinityPropagation()))

def validate_vectorizer_stored(test, model_name, level):
    manager = ModelsManager(name=model_name)
    vectorizer = manager.load_vectorizer(level)
    test.assertEqual(type(vectorizer), type(TfidfVectorizer()))
