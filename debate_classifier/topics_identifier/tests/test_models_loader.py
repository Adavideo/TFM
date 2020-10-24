from django.test import TestCase
from common.models_loader import get_filename, load_object
from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
from .examples import example_reference_documents

model_name ="test"
level = 0

class ModelsLoaderTests(TestCase):

    def test_get_filename_model(self):
        filename = get_filename("model", level, model_name)
        self.assertEqual(filename, "models/sklearn/test_model_level0.joblib")

    def test_get_filename_vectorizer(self):
        filename = get_filename("vectorizer", level, model_name)
        self.assertEqual(filename, "models/sklearn/test_vectorizer_level0.joblib")

    def test_load_model(self):
        model = load_object("model", level, model_name)
        self.assertEqual(type(model), type(AffinityPropagation()))

    def test_load_vectorizer(self):
        vectorizer = load_object("vectorizer", level, model_name)
        self.assertEqual(type(vectorizer), type(TfidfVectorizer()))

    def test_load_reference_documents_level0(self):
        reference_documents = load_object("reference_documents", level, model_name)
        expected = example_reference_documents[level]
        self.assertEqual(reference_documents, expected)

    def test_load_reference_documents_level1(self):
        level = 1
        reference_documents = load_object("reference_documents", level, model_name)
        expected = example_reference_documents[level]
        self.assertEqual(reference_documents, expected)
