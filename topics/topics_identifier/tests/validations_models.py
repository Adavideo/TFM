from topics_identifier.ModelsManager import ModelsManager
from .examples import example_documents_limit
from .example_trees import example_reference_documents

model_type = "<class 'sklearn.cluster.affinity_propagation_.AffinityPropagation'>"
vectoricer_type = "<class 'sklearn.feature_extraction.text.TfidfVectorizer'>"

def validate_model_stored(test, model_name, level):
    manager = ModelsManager(name=model_name)
    model = manager.load_object("model", level)
    test.assertEqual(str(type(model)), model_type)

def validate_vectorizer_stored(test, model_name, level):
    manager = ModelsManager(name=model_name)
    vectorizer = manager.load_object("vectorizer", level)
    test.assertEqual(str(type(vectorizer)), vectoricer_type)

def validate_reference_documents_stored(test, model_name, level):
    manager = ModelsManager(name=model_name)
    reference_documents = manager.load_object("reference_documents", level)
    validate_reference_documents(test, reference_documents, level)

def validate_reference_documents(test, reference_documents, level):
    expected = example_reference_documents[level]
    test.assertEqual(len(reference_documents), len(expected))
    test.assertEqual(reference_documents, expected)
