from .models import Document, Tree, Topic
from .datasets_manager import generate_dataset_from_threads
from .ClustersGenerator import ClustersGenerator


def read_file(topic_name):
    filename = "topics_identifier/classified/"+topic_name+".txt"
    file = open(filename)
    texts_list = file.read().split("\n")
    return texts_list

def find_thread(text):
    content = "\n"+text
    all_news = Document.objects.filter(is_news=True)
    for news in all_news:
        if news.thread:
            if news.thread.title in text:
                return news.thread

def get_threads_on_the_topic_from_file(topic_name):
    texts_list = read_file(topic_name)
    threads_list = []
    for text in texts_list:
        if text:
            thread = find_thread(text)
            if thread: threads_list.append(thread)
    print(str(len(threads_list))+" threads found")
    return threads_list

def associate_threads_to_topic(topic):
    threads_list = get_threads_on_the_topic_from_file(topic.name)
    for thread in threads_list:
        thread.assign_topic(topic)

def get_dataset_for_topic(topic):
    print("Getting threads for topic: " + topic.name)
    topic_threads = topic.get_threads()
    print("Generating dataset")
    dataset = generate_dataset_from_threads(topic_threads)
    return dataset

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

def cluster_for_topic(topic_name):
    topic, created = Topic.objects.get_or_create(name=topic_name)
    associate_threads_to_topic(topic)
    dataset = get_dataset_for_topic(topic)
    clusters_information, documents_clusters = generate_clusters_for_topic(dataset)
    tree = generate_tree_for_topic(topic.name, clusters_information, documents_clusters)
    clusters_list = tree.get_clusters_of_level(level=0)
    return clusters_list
