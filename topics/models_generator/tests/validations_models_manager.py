from .load import load_object
from common.testing.validations_models import validate_model_type, validate_vectorizer_type


def validate_model_stored(test, model_name, level):
    model = load_object("model", level, model_name)
    validate_model_type(test, model)

def validate_vectorizer_stored(test, model_name, level):
    vectorizer = load_object("vectorizer", level, model_name)
    validate_vectorizer_type(test, vectorizer)

def validate_reference_documents_stored(test, model_name, level, expected):
    reference_documents = load_object("reference_documents", level, model_name)
    validate_reference_documents(test, reference_documents, level, expected)

def validate_reference_documents(test, reference_documents, level, expected):
    test.assertEqual(len(reference_documents), len(expected))
    test.assertEqual(reference_documents, expected)

def validate_filenames(test, filenames, name, num_levels):
    test.assertEqual(len(filenames["models"]), num_levels)
    path_and_name = "models/sklearn/"+name+"_"
    for level in range(num_levels):
        end = "_level"+str(level)+".joblib"
        test.assertEqual(filenames["models"][level], path_and_name+"model"+end)
        test.assertEqual(filenames["vectorizers"][level], path_and_name+"vectorizer"+end)
        test.assertEqual(filenames["reference_documents"][level], path_and_name+"reference_documents"+end)
