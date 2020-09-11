import datetime
from .models import Tree
from .ClustersGenerator import ClustersGenerator
from .ModelsManager import ModelsManager
from .datasets_manager import generate_dataset
from .documents_selector import short_document_types, select_documents


def tree_already_exist(tree_name):
    tree_search = Tree.objects.filter(name=tree_name)
    if tree_search: return True
    else: return False


class TreeGenerator:

    def __init__(self, tree_name, model_name, documents_options, max_level=1):
        self.documents_options = documents_options
        created = self.create_empty_tree(tree_name)
        if not created: return None
        self.model_name = model_name
        self.max_level = max_level
        self.models_manager = ModelsManager(name=model_name)

    def create_empty_tree(self, tree_name):
        # Avoids trying to create a tree with a name that is already taken
        if tree_already_exist(tree_name):
            self.tree_already_exist = True
            return None
        else:
            self.tree_already_exist = False
            news, comments = short_document_types(self.documents_options["types"])
            self.tree = Tree(name=tree_name, news=news, comments=comments)
            self.tree.save()
            return self.tree

    def get_dataset(self, level):
        if level==0:
            documents = select_documents(self.documents_options)
        else:
            # Gets the reference documents from the inferior level
            documents = self.tree.get_reference_documents(level-1)
        dataset = generate_dataset(documents)
        return dataset

    def generate_level_clusters(self, clusters_generator, level):
        clusters = clusters_generator.get_clusters()
        self.tree.add_clusters(level, clusters)

    def add_documents_to_clusters(self, clusters_generator, documents, level):
        clusters_documents = clusters_generator.predict_clusters_documents(documents)
        print(str(datetime.datetime.now().time())+" - Adding documents to clusters")
        self.tree.add_documents_to_several_clusters(level, clusters_documents)

    def level_iteration(self, level):
        print(str(datetime.datetime.now().time())+" - Generating clusters for level "+str(level) )
        clusters_generator = ClustersGenerator(self.models_manager, level)
        self.generate_level_clusters(clusters_generator, level)
        dataset = self.get_dataset(level)
        self.add_documents_to_clusters(clusters_generator, dataset.data, level)
        if level > 0:
            self.tree.link_children_to_parents(level)

    def generate_tree(self):
        print(str(datetime.datetime.now().time())+" - Generating clusters tree")
        # Iterate through the tree levels
        for level in range(0, self.max_level+1):
            self.level_iteration(level)
        # Returns the clusters from the top level of the tree
        clusters = self.tree.get_clusters_of_level(self.max_level)
        return clusters
