from .models import Tree, Topic
from .datasets_manager import generate_dataset_from_threads
from .ClustersGenerator import ClustersGenerator
from .models_manager import load_model_and_terms
from .ModelGenerator import ModelGenerator


def get_dataset_for_topic(topic):
    print("Getting threads for topic: " + topic.name)
    topic_threads = topic.get_threads()
    print("Generating dataset")
    dataset = generate_dataset_from_threads(topic_threads)
    return dataset

def generate_clusters_for_topic(model, dataset, terms):
    clusters_generator = ClustersGenerator(model, dataset, terms)
    clusters_information = clusters_generator.get_clusters_information()
    num_clusters = len(clusters_information["terms"])
    print("Clusters completed. "+str(num_clusters)+" clusters.")
    return clusters_information

def generate_tree_for_topic(topic_name, clusters_information, documents_clusters):
    tree, created = Tree.objects.get_or_create(name=topic_name, news=True, comments=True)
    if created: tree.save()
    tree.add_clusters(level=0, clusters_information=clusters_information)
    tree.add_documents_to_clusters(level=0, documents_clusters_list=documents_clusters)
    return tree

def get_documents(model_generator):
    try:
        print("Clustering documents")
        vectorized_documents = model_generator.process_documents()
        documents_clusters = clusters_generator.get_documents_clusters(vectorized_documents)
        return documents_clusters
    except:
        print("Clustering failed")
        return []

def get_model_and_terms(model_name, documents, model_generator):
    if model_name.strip():
        print("Loading model "+model_name)
        model, terms = load_model_and_terms(model_name, level=0)
    else:
        print("Generating model")
        model = model_generator.generate_model()
        terms = model_generator.all_terms
    return model, terms

def cluster_for_topic(topic, model_name):
    dataset = get_dataset_for_topic(topic)
    model_generator = ModelGenerator(dataset.data)
    model, terms = get_model_and_terms(model_name, dataset.data, model_generator)
    clusters_information = generate_clusters_for_topic(model, dataset, terms)
    documents_clusters = get_documents(model_generator)
    print("Generating tree")
    tree = generate_tree_for_topic(topic.name, clusters_information, documents_clusters)
    clusters_list = tree.get_clusters_of_level(level=0)
    return clusters_list
