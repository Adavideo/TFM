from topics_identifier.ClustersGenerator import ClustersGenerator
from topics_identifier.TreeGenerator import TreeGenerator
from topics_identifier.ModelsManager import ModelsManager
from .mock_datasets import mock_dataset
from .example_trees import tree_name
from .examples import test_model_name, example_terms, example_documents, example_documents_limit


def mock_models_manager(name=test_model_name):
    models_manager = ModelsManager(name=name, documents_limit=example_documents_limit)
    return models_manager

def mock_affinity_propagation_model():
    manager = mock_models_manager()
    model = manager.load_model(level=0)
    return model

def mock_model():
    return mock_affinity_propagation_model()

def mock_vectorizer():
    manager = mock_models_manager()
    vectorizer = manager.load_vectorizer(level=0)
    return vectorizer

def mock_cluster_generator():
    model = mock_affinity_propagation_model()
    vectorizer = mock_vectorizer()
    generator = ClustersGenerator(model, vectorizer, example_documents)
    return generator

def mock_tree_generator(max_level, document_types="both"):
    return TreeGenerator(tree_name, document_types, max_level)
