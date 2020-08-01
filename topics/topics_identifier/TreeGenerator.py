import datetime
from .models import Tree
from .ClustersGenerator import ClustersGenerator
from .datasets_manager import generate_dataset
from .file_paths import stop_words_filename

class TreeGenerator:

    def get_stop_words(self):
        stop_words = []
        file = open(stop_words_filename, 'r')
        words_from_file = file.read().split("\n")
        file.close()
        for word in words_from_file:
            stop_words.append(word)
        return stop_words

    def __init__(self, tree_name, max_level=1):
        self.max_level = max_level
        self.stop_words = self.get_stop_words()
        self.tree, created = Tree.objects.get_or_create(name=tree_name)
        if created:
            self.tree.save()

    def cluster_level(self, level):
        print("\nGenerating level "+ str(level)+" clusters")
        dataset = generate_dataset(level, self.tree)
        clusters_generator = ClustersGenerator(dataset, self.stop_words)
        clusters_information = clusters_generator.cluster_data()
        documents_clusters = clusters_generator.get_documents_clusters()
        return clusters_information, documents_clusters

    def store_information(self, level, clusters_information, documents_clusters):
        self.tree.add_clusters(level, clusters_information)
        print(str(datetime.datetime.now().time())+" - Adding documents to clusters")
        self.tree.add_documents_to_clusters(level, documents_clusters)

    def generate_tree(self):
        for level in range(0, self.max_level+1):
            clusters_information, documents_clusters = self.cluster_level(level)
            self.store_information(level, clusters_information, documents_clusters)
        print(str(datetime.datetime.now().time())+" - Clustering completed")
        return self.tree
