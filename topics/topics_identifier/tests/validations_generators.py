from .example_trees import example_tree
from .validations_models import model_type, vectoricer_type
from .example_trees import example_reference_documents
from .examples import example_terms


# TREE BUILDING VALIDATIONS

def validate_clusters_terms(test, all_clusters_terms, level):
    example_clusters = example_tree[level]["clusters"]
    for i in range(len(all_clusters_terms)):
        test.assertEqual(str(all_clusters_terms[i]), example_clusters[i]["terms"])

def validate_clusters_reference_documents(test, clusters_reference_documents, expected_documents):
    for i in range(len(clusters_reference_documents)):
        test.assertEqual(clusters_reference_documents[i], expected_documents[i])


# CLUSTERS GENERATOR VALIDATION

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
    validate_clusters_reference_documents(test, clusters_generator.reference_documents, expected["reference_documents"])
