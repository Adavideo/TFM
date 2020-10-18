import datetime
from .models import Tree
from .ClustersGenerator import ClustersGenerator
from .documents_selector import select_documents, get_number_of_documents
from .batches_util import get_number_of_batches


class TreeGenerator:

    def __init__(self, tree_name, model_name, documents_types, max_level=1):
        self.documents_types = documents_types
        self.max_level = max_level
        created = self.create_empty_tree(tree_name)
        if not created: return None
        self.model_name = model_name


    # GENERATE TREE STRUCTURE

    def create_empty_tree(self, tree_name):
        # Avoids trying to create a tree with a name that is already taken
        self.tree_already_exist = (not len(Tree.objects.filter(name=tree_name))==0)
        if self.tree_already_exist: return None
        else:
            news = (self.documents_types=="news" or self.documents_types=="both")
            comments = (self.documents_types=="comments" or self.documents_types=="both")
            self.tree = Tree(name=tree_name, news=news, comments=comments)
            self.tree.max_level = self.max_level
            self.tree.save()
            return self.tree

    def generate_level_clusters(self, clusters_generator, level):
        clusters = clusters_generator.get_clusters()
        self.tree.add_clusters(level, clusters)


    # ADD DOCUMENTS TO CLUSTERS

    def add_documents_to_clusters(self, clusters_generator, documents, level):
        clusters_documents = clusters_generator.predict_clusters_documents(documents)
        print(str(datetime.datetime.now().time())+" - Adding documents to clusters")
        for i in range(len(clusters_documents)):
            self.tree.add_documents_to_cluster(level, i, clusters_documents[i])

    def add_documents_level0(self, clusters_generator, level):
        num_documents = get_number_of_documents(self.documents_types)
        num_of_batches = get_number_of_batches(num_documents)
        for batch_number in range(1, num_of_batches+1):
            documents = select_documents(self.documents_types, batch_number)
            self.add_documents_to_clusters(clusters_generator, documents, level)

    # Gets the reference documents from the inferior level
    def get_upper_level_documents(self, level):
        documents = self.tree.get_reference_documents(level-1)
        return documents

    def add_documents(self, clusters_generator, level):
        if level==0:
            self.add_documents_level0(clusters_generator, level)
        else:
            documents = self.get_upper_level_documents(level)
            self.add_documents_to_clusters(clusters_generator, documents, level)
            self.tree.link_children_to_parents(level)


    # MAIN LOOP

    def level_iteration(self, level):
        print(str(datetime.datetime.now().time())+" - Generating clusters for level "+str(level) )
        clusters_generator = ClustersGenerator(self.model_name, level)
        self.generate_level_clusters(clusters_generator, level)
        self.add_documents(clusters_generator, level)

    def generate_tree(self):
        print(str(datetime.datetime.now().time())+" - Generating clusters tree")
        # Iterate through the tree levels
        for level in range(0, self.max_level+1):
            self.level_iteration(level)
        return self.tree
