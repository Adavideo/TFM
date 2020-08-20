from .models import Tree, Topic
from .datasets_manager import generate_dataset_from_threads
from .ClustersGenerator import ClustersGenerator
from .models_manager import load_model_and_terms

def get_dataset_for_topic(topic):
    print("Getting threads for topic: " + topic.name)
    topic_threads = topic.get_threads()
    print("Generating dataset")
    dataset = generate_dataset_from_threads(topic_threads)
    return dataset

def generate_clusters_for_topic(model, dataset, terms):
    clusters_generator = ClustersGenerator(model, dataset, terms)
    print("Clustering documents")
    clusters_information = clusters_generator.cluster_data()
    num_clusters = len(clusters_information["terms"])
    print("Clustering completed. "+str(num_clusters)+" clusters.")
    documents_clusters = clusters_generator.get_documents_clusters()
    return clusters_information, documents_clusters

def generate_tree_for_topic(topic_name, clusters_information, documents_clusters):
    tree, created = Tree.objects.get_or_create(name=topic_name, news=True, comments=True)
    if created: tree.save()
    tree.add_clusters(level=0, clusters_information=clusters_information)
    tree.add_documents_to_clusters(level=0, documents_clusters_list=documents_clusters)
    return tree

def cluster_for_topic(topic, model_name):
    dataset = get_dataset_for_topic(topic)
    model, terms = load_model_and_terms(model_name, level=0)
    clusters_information, documents_clusters = generate_clusters_for_topic(model, dataset, terms)
    tree = generate_tree_for_topic(topic.name, clusters_information, documents_clusters)
    clusters_list = tree.get_clusters_of_level(level=0)
    return clusters_list
