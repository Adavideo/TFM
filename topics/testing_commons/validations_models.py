from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer


def validate_model_type(test, model):
    test.assertEqual(type(model), type(AffinityPropagation()))

def validate_vectorizer_type(test, vectorizer):
    test.assertEqual(type(vectorizer), type(TfidfVectorizer()))
