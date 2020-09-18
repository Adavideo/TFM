from topics_identifier.ClustersGenerator import ClustersGenerator
from topics_identifier.TreeGenerator import TreeGenerator
from topics_identifier.ModelsManager import ModelsManager
from .example_trees import tree_name, example_tree, example_terms
from .examples_models import test_model_name
from .examples_documents_selector import example_doc_options


def mock_models_manager(name=test_model_name):
    models_manager = ModelsManager(name=name)
    return models_manager

def mock_affinity_propagation_model(level=0):
    manager = mock_models_manager()
    model = manager.load_object("model", level)
    return model

def mock_model(level=0):
    return mock_affinity_propagation_model(level)

def mock_vectorizer(level=0):
    manager = mock_models_manager()
    vectorizer = manager.load_object("vectorizer", level)
    return vectorizer

def mock_clusters_generator(level=0):
    models_manager = mock_models_manager()
    generator = ClustersGenerator(models_manager, level)
    return generator

def mock_tree_generator(max_level=0, document_options=example_doc_options):
    return TreeGenerator(tree_name, test_model_name, document_options, max_level)
