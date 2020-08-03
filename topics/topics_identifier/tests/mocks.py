from sklearn.datasets.base import Bunch
from topics_identifier.models import Cluster, Document, Tree
from topics_identifier.ClustersGenerator import ClustersGenerator
from topics_identifier.TreeGenerator import TreeGenerator, short_document_types
from .examples import example_documents, tree_name, example_tree, example_stop_words, example_news

# Simulate that half the documents are news and the other half are comments
def select_example_documents(document_types, documents=example_documents):
    # If we ask for both types of documents, it return all of them
    if document_types == "both":
        return documents

    half = int(len(example_documents)/2)
    if document_types == "news":
        # If we ask for news documents, returns the first half of the list
        return documents[:half]
    else:
        # If we want comments documents, returns the second half of the list
        return documents[half:]

def mock_document(content, is_news):
    doc, created = Document.objects.get_or_create(content=content, is_news=is_news, date=example_news["date"], author=example_news["author"])
    if created: doc.save()
    return doc

def mock_documents():
    # Mock half the documents as news
    news_documents = select_example_documents(document_types="news")
    for content in news_documents:
        mock_document(content, is_news=True)
    # Mock half the documents as comments
    comments_documents = select_example_documents(document_types="comments")
    for content in comments_documents:
        mock_document(content, is_news=False)

def mock_empty_tree(document_types="both"):
    if not Document.objects.all():
        mock_documents()
    news, comments = short_document_types(document_types)
    tree = Tree(name=tree_name, news=news, comments=comments)
    tree.save()
    return tree

def mock_cluster(tree=None, num_cluster=0, level=0, with_documents=False):
    if not tree:
        tree = mock_empty_tree()
    cluster_info = example_tree[level]["clusters"][num_cluster]
    cluster = Cluster(tree=tree, number=num_cluster, terms=cluster_info["terms"], level=level)
    cluster.assign_reference_document(cluster_info["reference_doc"])
    cluster.save()
    if with_documents:
        for doc in cluster_info["documents"]:
            cluster.add_document(doc)
    return cluster

def mock_tree(max_level=0, linked=False, with_documents=True, document_types="both"):
    tree = mock_empty_tree(document_types)
    for level in range(0, max_level+1):
        num_clusters = len(example_tree[level]["clusters"])
        for n in range(0, num_clusters):
            mock_cluster(tree, num_cluster=n, level=level, with_documents=with_documents)
        if linked:
            tree.link_children_to_parents(level)
    return tree

def mock_clusters_information(level):
    clusters_list = example_tree[level]["clusters"]
    terms = []
    reference_documents = []
    for cluster in clusters_list:
        terms.append(cluster["terms"])
        reference_documents.append(cluster["reference_doc"])
    clusters_information = { "terms": terms, "reference_documents": reference_documents}
    return clusters_information

def mock_dataset():
    dataset = Bunch()
    dataset.data = example_documents
    return dataset

def mock_cluster_generator():
    dataset = mock_dataset()
    generator = ClustersGenerator(dataset, example_stop_words)
    return generator

def mock_tree_generator(max_level, document_types="both"):
    return TreeGenerator(tree_name, document_types, max_level)
