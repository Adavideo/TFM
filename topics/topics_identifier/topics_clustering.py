from .models import Tree
from .documents_selector import get_documents_from_threads
from .ClustersGenerator import ClustersGenerator
from .ModelsManager import ModelsManager
from .ModelGenerator import ModelGenerator
from .TreeGenerator import TreeGenerator


# Create and store model, vectorizer and reference documents

def get_documents_for_topic(topic):
    print("Getting threads for topic: " + topic.name)
    topic_threads = topic.get_threads()
    print("Geneting documents")
    dataset = get_documents_from_threads(topic_threads)
    return dataset

def create_and_store_model_for_topic(topic):
    level = 0
    documents = get_documents_for_topic(topic)
    # Generate model and vectorizer
    model_generator = ModelGenerator(documents)
    model = model_generator.generate_model()
    vectorizer = model_generator.vectorizer
    # Store model and vectorizer
    models_manager = ModelsManager(name=topic.name)
    models_manager.store_object(model, "model", level)
    models_manager.store_object(vectorizer, "vectorizer", level)
    # Get and store reference documents
    clusters_generator = ClustersGenerator(models_manager, level, model=model, vectorizer=vectorizer)
    reference_documents = clusters_generator.get_reference_documents(documents)
    models_manager.store_object(reference_documents, "reference_documents", level)


# Generate clusters and tree

def get_clusters_generator(topic, model_name):
    level = 0
    models_manager = ModelsManager(name=model_name)
    clusters_generator = ClustersGenerator(models_manager, level)
    return clusters_generator

def add_documents_to_clusters(topic, tree_generator, clusters_generator):
    documents = get_documents_for_topic(topic)
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
    add_documents_to_clusters(topic, tree_generator, clusters_generator)
    clusters_list = tree_generator.tree.get_clusters_of_level(level=0)
    return clusters_list
