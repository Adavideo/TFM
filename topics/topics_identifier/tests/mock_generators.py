from topics_identifier.ClustersGenerator import ClustersGenerator
from topics_identifier.TreeGenerator import TreeGenerator
from topics_identifier.ModelsManager import ModelsManager
from .mock_datasets import mock_dataset
from .example_trees import tree_name
from .examples import test_model_name, example_terms, example_documents, example_doc_options


def mock_models_manager(name=test_model_name):
    models_manager = ModelsManager(name=name)
    return models_manager

def mock_affinity_propagation_model(level=0):
    manager = mock_models_manager()
    model = manager.load_model(level)
    return model

def mock_model(level=0):
    return mock_affinity_propagation_model(level)

def mock_vectorizer(level=0):
    manager = mock_models_manager()
    vectorizer = manager.load_vectorizer(level)
    return vectorizer

def mock_cluster_generator(level=0):
    model = mock_affinity_propagation_model(level)
    vectorizer = mock_vectorizer(level)
    generator = ClustersGenerator(model, vectorizer, example_documents)
    return generator

def mock_tree_generator(max_level=0, document_options=example_doc_options):
    return TreeGenerator(tree_name, test_model_name, document_options, max_level)
