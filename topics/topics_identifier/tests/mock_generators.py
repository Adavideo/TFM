from .example_stop_words import example_stop_words
from topics_identifier.ClustersGenerator import ClustersGenerator
from topics_identifier.TreeGenerator import TreeGenerator
from topics_identifier.models_manager import load_model
from .mock_datasets import mock_dataset
from .example_trees import tree_name
from .examples import test_model_name


def mock_cluster_generator():
    dataset = mock_dataset()
    generator = ClustersGenerator(dataset, example_stop_words)
    return generator

def mock_tree_generator(max_level, document_types="both"):
    return TreeGenerator(tree_name, document_types, max_level)

def mock_affinity_propagation_model():
    model = load_model(test_model_name, level=0)
    return model

def mock_model():
    return mock_affinity_propagation_model()
