import datetime
from config import batch_size
from .models import Tree
from .ClustersGenerator import ClustersGenerator
from .documents_selector import short_document_types, select_documents, get_documents_batch
from .batches_util import *


def tree_already_exist(tree_name):
    tree_search = Tree.objects.filter(name=tree_name)
    if tree_search: return True
    else: return False


class TreeGenerator:

    def __init__(self, tree_name, model_name, documents_options, max_level=1):
        self.documents_options = documents_options
        self.max_level = max_level
        created = self.create_empty_tree(tree_name)
        if not created: return None
        self.model_name = model_name


    # GENERATE TREE STRUCTURE

    def create_empty_tree(self, tree_name):
        # Avoids trying to create a tree with a name that is already taken
        if tree_already_exist(tree_name):
            self.tree_already_exist = True
            return None
        else:
            self.tree_already_exist = False
            news, comments = short_document_types(self.documents_options["types"])
            self.tree = Tree(name=tree_name, news=news, comments=comments)
            self.tree.max_level = self.max_level
            self.tree.save()
            return self.tree

    def generate_level_clusters(self, clusters_generator, level):
        clusters = clusters_generator.get_clusters()
        self.tree.add_clusters(level, clusters)


    # ADD DOCUMENTS TO CLUSTERS

    def get_all_level_documents(self, level):
        if level==0:
            documents_options = { "types": self.documents_options["types"],
                                  "max_num_documents": None,
                                  "batches": False }
            documents = select_documents(documents_options)
        else:
            # Gets the reference documents from the inferior level
            documents = self.tree.get_reference_documents(level-1)
        return documents

    def get_documents(self, level, batch_number=None, size=batch_size):
        all_documents = self.get_all_level_documents(level)
        if not self.documents_options["batches"] or not batch_number:
            return all_documents
        else:
            batch_options = get_batch_options(self.documents_options, batch_number, size)
            batch_documents = get_documents_batch(all_documents, batch_options)
            return batch_documents

    def get_number_of_documents(self, level):
        num_documents = len(self.get_all_level_documents(level))
        return num_documents

    def add_documents_to_clusters(self, clusters_generator, documents, level):
        clusters_documents = clusters_generator.predict_clusters_documents(documents)
        self.tree.add_documents_to_several_clusters(level, clusters_documents)

    def add_documents_to_clusters_in_batches(self, clusters_generator, level, size=batch_size):
        num_documents = self.get_number_of_documents(level)
        num_of_batches = get_number_of_batches(num_documents, size)
        for batch_number in range(1, num_of_batches+1):
            documents = self.get_documents(level, batch_number, size)
            self.add_documents_to_clusters(clusters_generator, documents, level)

    def add_documents(self, clusters_generator, level, size=batch_size):
        print(str(datetime.datetime.now().time())+" - Adding documents to clusters")
        if self.documents_options["batches"]:
            self.add_documents_to_clusters_in_batches(clusters_generator, level, size)
        else:
            documents = self.get_documents(level)
            self.add_documents_to_clusters(clusters_generator, documents, level)


    # MAIN LOOP

    def level_iteration(self, level):
        print(str(datetime.datetime.now().time())+" - Generating clusters for level "+str(level) )
        clusters_generator = ClustersGenerator(self.model_name, level)
        self.generate_level_clusters(clusters_generator, level)
        self.add_documents(clusters_generator, level)
        if level > 0:
            self.tree.link_children_to_parents(level)

    def generate_tree(self):
        print(str(datetime.datetime.now().time())+" - Generating clusters tree")
        # Iterate through the tree levels
        for level in range(0, self.max_level+1):
            self.level_iteration(level)
        return self.tree
