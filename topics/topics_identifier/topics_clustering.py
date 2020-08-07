from .models import Tree, Topic
from .datasets_manager import generate_dataset_from_threads
from .ClustersGenerator import ClustersGenerator


def generate_tree_for_topic(topic_name, clusters_information, documents_clusters):
    tree = Tree(name=topic_name, news=True, comments=True)
    tree.save()
    tree.add_clusters(level=0, clusters_information=clusters_information)
    tree.add_documents_to_clusters(level=0, documents_clusters_list=documents_clusters)
    return tree

def generate_clusters_for_topic(dataset):
    clusters_generator = ClustersGenerator(dataset)
    print("Clustering documents")
    clusters_information = clusters_generator.cluster_data()
    num_clusters = len(clusters_information["terms"])
    print("Clustering completed. "+str(num_clusters)+" clusters.")
    documents_clusters = clusters_generator.get_documents_clusters()
    return clusters_information, documents_clusters

def get_dataset_for_topic(topic):
    print("Getting threads for topic: " + topic.name)
    topic_threads = topic.get_threads()
    print("Generating dataset")
    dataset = generate_dataset_from_threads(topic_threads)
    return dataset

def find_topic(topic_name):
    topic_search = Topic.objects.filter(name=topic_name)
    if topic_search:
        topic = topic_search[0]
    return topic

def cluster_for_topic(topic_name):
    topic = find_topic(topic_name)
    if not topic: return []
    dataset = get_dataset_for_topic(topic)
    clusters_information, documents_clusters = generate_clusters_for_topic(dataset)
    tree = generate_tree_for_topic(topic.name, clusters_information, documents_clusters)
    clusters_list = tree.get_clusters_of_level(level=0)
    return clusters_list
