from topics_identifier.ClustersGenerator import ClustersGenerator
from topics_identifier.TreeGenerator import TreeGenerator
from topics_identifier.ModelsManager import ModelsManager
from .examples import doc_options_with_batches, test_model_name
from .example_trees import tree_name


def mock_models_manager(name=test_model_name):
    models_manager = ModelsManager(name=name)
    return models_manager

def mock_clusters_generator(level=0):
    models_manager = mock_models_manager()
    generator = ClustersGenerator(models_manager, level)
    return generator

def mock_tree_generator(max_level=0, document_options=doc_options_with_batches):
    tree_generator = TreeGenerator(tree_name, test_model_name, document_options, max_level)
    return tree_generator
