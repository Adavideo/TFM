from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
from topics_identifier.models_manager import load_model, load_vectorizer

def validate_model_stored(test, model_name, level):
    model = load_model(model_name, level)
    test.assertEqual(type(model), type(AffinityPropagation()))

def validate_vectorizer_stored(test, model_name, level):
    vectorizer = load_vectorizer(model_name, level)
    test.assertEqual(type(vectorizer), type(TfidfVectorizer()))
