from topics_identifier.TreeGenerator import TreeGenerator
from topics_identifier.ClustersGenerator import ClustersGenerator
from topics_identifier.models import Tree
from models_generator.ModelsManager import ModelsManager
from common.models_loader import model_created

min_length_docs = 25


def generate_model(name, documents):
    if not model_created(name):
        print("Generating model")
        documents_content = [ (doc.content )for doc in documents ]
        models_manager = ModelsManager(name=name)
        models_manager.generate_and_store_models(documents_content, max_level=1)

def generate_level0(tree_generator, model_name, documents):
    print("Generating level 0 clusters")
    clusters_generator = ClustersGenerator(model_name, level=0)
    tree_generator.generate_level_clusters(clusters_generator, level=0)
    tree_generator.add_documents_to_clusters(clusters_generator, documents, level=0)

def generate_tree(tree_name, model_name, documents):
    documents_types = "both"
    tree_generator = TreeGenerator(tree_name, model_name, documents_types, max_level=1)
    if tree_generator.tree_already_exist: return None
    # Generate tree levels
    generate_level0(tree_generator, model_name, documents)
    tree_generator.level_iteration(level=1)
    return tree_generator.tree

def get_documents(topic):
    all_documents = topic.get_documents()
    selected_documents = []
    for document in all_documents:
        if len(document.content)>min_length_docs:
            selected_documents.append(document)
    return selected_documents

def generate_tree_with_topic_documents(topic, tree_name):
    documents = get_documents(topic)
    model_name = topic.name
    generate_model(model_name, documents)
    tree = generate_tree(tree_name, model_name, documents)
    return tree
