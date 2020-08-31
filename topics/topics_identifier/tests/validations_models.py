from topics_identifier.ModelsManager import ModelsManager
from .examples import example_documents_limit

model_type = "<class 'sklearn.cluster.affinity_propagation_.AffinityPropagation'>"
vectoricer_type = "<class 'sklearn.feature_extraction.text.TfidfVectorizer'>"

def validate_model_stored(test, model_name, level):
    manager = ModelsManager(name=model_name)
    model = manager.load_model(level)
    test.assertEqual(str(type(model)), model_type)

def validate_vectorizer_stored(test, model_name, level):
    manager = ModelsManager(name=model_name)
    vectorizer = manager.load_vectorizer(level)
    test.assertEqual(str(type(vectorizer)), vectoricer_type)
