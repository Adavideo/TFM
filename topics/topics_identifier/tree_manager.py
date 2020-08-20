from .models import Tree
from .TreeGenerator import TreeGenerator

def tree_already_exist(tree_name):
    tree_search = Tree.objects.filter(name=tree_name)
    if tree_search:
        return True
    else:
        return False

def generate_tree(tree_name, model_name, documents_options, max_level=1):
    if tree_already_exist(tree_name): return { "tree_exists": True }

    results = { "tree_exists": False }
    # Cluster the documents in two levels and store them in a cluster tree
    generator = TreeGenerator(tree_name, document_types=documents_options["types"], max_level=max_level)
    tree = generator.generate_tree()
    # Prepare the information to show on the web page
    max_level_clusters = tree.get_clusters_of_level(max_level)
    results["clusters"] = max_level_clusters
    return results
