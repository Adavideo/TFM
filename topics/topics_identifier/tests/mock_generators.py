from topics_identifier.ClustersGenerator import ClustersGenerator
from topics_identifier.TreeGenerator import TreeGenerator
from .examples import doc_options_with_batches, test_model_name
from .example_trees import tree_name


def mock_clusters_generator(level=0):
    generator = ClustersGenerator(test_model_name, level)
    return generator

def mock_tree_generator(max_level=0, document_options=doc_options_with_batches):
    tree_generator = TreeGenerator(tree_name, test_model_name, document_options, max_level)
    return tree_generator
