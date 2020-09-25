from .validations import validate_model_type, validate_vectorizer_type


def validate_clusters_generator(test, clusters_generator, model_name, expected):
    test.assertEqual(clusters_generator.models_manager.name, model_name)
    validate_model_type(test, clusters_generator.model)
    validate_vectorizer_type(test, clusters_generator.vectorizer)
    test.assertEqual(clusters_generator.reference_documents, expected["reference_documents"])
    test.assertEqual(clusters_generator.terms, expected["terms"])
    num_clusters = len(expected["clusters"])
    test.assertEqual(clusters_generator.number_of_clusters, num_clusters)

def validate_clusters_information_in_clusters_generator(test, clusters_generator, expected):
    test.assertEqual(clusters_generator.number_of_clusters, len(expected["clusters"]))
    test.assertEqual(clusters_generator.terms, expected["terms"])
    test.assertEqual(clusters_generator.reference_documents, expected["reference_documents"])
