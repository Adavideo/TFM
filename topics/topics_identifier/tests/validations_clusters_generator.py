from .validations_models import model_type, vectoricer_type


def validate_clusters_generator(test, clusters_generator, model_name, expected):
    test.assertEqual(clusters_generator.models_manager.name, model_name)
    test.assertEqual(str(type(clusters_generator.model)), model_type)
    test.assertEqual(str(type(clusters_generator.vectorizer)), vectoricer_type)
    test.assertEqual(clusters_generator.reference_documents, expected["reference_documents"])
    test.assertEqual(clusters_generator.terms, expected["terms"])
    num_clusters = len(expected["clusters"])
    test.assertEqual(clusters_generator.number_of_clusters, num_clusters)

def validate_clusters_information_in_clusters_generator(test, clusters_generator, expected):
    test.assertEqual(clusters_generator.number_of_clusters, len(expected["clusters"]))
    test.assertEqual(clusters_generator.terms, expected["terms"])
    test.assertEqual(clusters_generator.reference_documents, expected["reference_documents"])

def validate_clusters_documents(test, clusters_documents, example):
    for i in range(len(example["clusters_documents"])):
        test.assertEqual(clusters_documents[i], example["clusters_documents"][i])
