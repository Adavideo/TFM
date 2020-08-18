from .example_trees import tree_name
from .example_stop_words import example_stop_words
from topics_identifier.ClustersGenerator import ClustersGenerator
from topics_identifier.TreeGenerator import TreeGenerator
from .mock_datasets import mock_dataset


def mock_cluster_generator():
    dataset = mock_dataset()
    generator = ClustersGenerator(dataset, example_stop_words)
    return generator

def mock_tree_generator(max_level, document_types="both"):
    return TreeGenerator(tree_name, document_types, max_level)

def mock_affinity_propagation_model():
    generator = mock_cluster_generator()
    generator.process_data()
    model = generator.train_model()
    return model
