import datetime
from .models import Tree
from .ClustersGenerator import ClustersGenerator
from .datasets_manager import get_dataset
from .stop_words.stop_words import get_stop_words
from .sklearn_models_manager import store_model


def short_document_types(document_types):
    if document_types == "both":
        news = True
        comments = True
    elif document_types == "news":
        news = True
        comments = False
    else:
        news = False
        comments = True
    return news, comments

def tree_already_exist(tree_name):
    tree_search = Tree.objects.filter(name=tree_name)
    if tree_search:
        return True
    else:
        return False

class TreeGenerator:

    def __init__(self, tree_name, document_types, max_level=1):
        # Avoids trying to create a tree with a name that is already taken
        if tree_already_exist(tree_name):
            self.tree = None
            return None
        else:
            news, comments = short_document_types(document_types)
            self.tree = Tree(name=tree_name, news=news, comments=comments)
            self.tree.save()
            self.max_level = max_level
            self.stop_words = get_stop_words()

    def get_model_name(self, level):
        name = self.tree.name + "_level" + str(level)
        return name

    def cluster_level(self, level):
        print("\nGenerating level "+ str(level)+" clusters")
        dataset = get_dataset(self.tree, level)
        clusters_generator = ClustersGenerator(dataset, self.stop_words)
        clusters_information = clusters_generator.cluster_data()
        model_name = self.get_model_name(level)
        store_model(clusters_generator.model, model_name)
        documents_clusters = clusters_generator.get_documents_clusters()
        return clusters_information, documents_clusters

    def store_information(self, level, clusters_information, documents_clusters):
        if clusters_information:
            self.tree.add_clusters(level, clusters_information)
        if documents_clusters:
            print(str(datetime.datetime.now().time())+" - Adding documents to clusters")
            self.tree.add_documents_to_clusters(level, documents_clusters)

    def generate_tree(self):
        for level in range(0, self.max_level+1):
            clusters_information, documents_clusters = self.cluster_level(level)
            self.store_information(level, clusters_information, documents_clusters)
        print(str(datetime.datetime.now().time())+" - Clustering completed")
        return self.tree
