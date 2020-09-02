from .models import Tree
from .datasets_manager import generate_dataset_from_threads
from .ClustersGenerator import ClustersGenerator
from .ModelsManager import ModelsManager
from .ModelGenerator import ModelGenerator
from .TreeGenerator import TreeGenerator


# Create and store model and vectorizer

def get_dataset_for_topic(topic):
    print("Getting threads for topic: " + topic.name)
    topic_threads = topic.get_threads()
    print("Generating dataset")
    dataset = generate_dataset_from_threads(topic_threads)
    return dataset

def store_model_for_topic(topic_name, model, vectorizer):
    level = 0
    models_manager = ModelsManager(name=topic_name)
    models_manager.store_object(model, "model", level)
    models_manager.store_object(vectorizer, "vectorizer", level)

def create_and_store_model_for_topic(topic):
    dataset = get_dataset_for_topic(topic)
    model_generator = ModelGenerator(dataset.data)
    model = model_generator.generate_model()
    vectorizer = model_generator.vectorizer
    store_model_for_topic(topic.name, model, vectorizer)

# Generate clusters and tree

def get_clusters_generator(topic, model_name):
    dataset = get_dataset_for_topic(topic)
    models_manager = ModelsManager(name=model_name)
    model = models_manager.load_object("model", level=0)
    vectorizer = models_manager.load_object("vectorizer", level=0)
    clusters_generator = ClustersGenerator(model, vectorizer, dataset.data)
    return clusters_generator

def add_documents_to_clusters(tree_generator, clusters_generator):
    documents = clusters_generator.original_documents
    tree_generator.add_documents_to_clusters(clusters_generator, documents, level=0)

def generate_tree_for_topic(topic_name, model_name, clusters_generator):
    level = 0
    documents_options = { "types": "both" }
    tree_name = topic_name
    tree_generator = TreeGenerator(tree_name, model_name, documents_options, max_level=level)
    tree_generator.generate_level_clusters(clusters_generator, level)
    print("Clusters completed")
    return tree_generator

def cluster_for_topic(topic, model_name):
    clusters_generator = get_clusters_generator(topic, model_name)
    print("Generating tree for topic " + topic.name)
    tree_generator = generate_tree_for_topic(topic.name, model_name, clusters_generator)
    add_documents_to_clusters(tree_generator, clusters_generator)
    clusters_list = tree_generator.tree.get_clusters_of_level(level=0)
    return clusters_list
