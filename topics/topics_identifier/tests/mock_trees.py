from topics_identifier.models import Tree, Document, Cluster
from topics_identifier.documents_selector import short_document_types
from .examples import news_content, comments_content
from .example_trees import example_tree, tree_name
from .mocks import mock_documents


def mock_empty_tree(document_types="both", name=tree_name):
    if not Document.objects.all():
        mock_documents()
    with_news, with_comments = short_document_types(document_types)
    tree = Tree(name=name, news=with_news, comments=with_comments)
    tree.save()
    return tree

# We can not import mock cluster because it already imports mock_empty_tree
def mock_cluster_for_tree(tree, num_cluster, level, with_documents):
    cluster_info = example_tree[level]["clusters"][num_cluster]
    cluster = Cluster(tree=tree, number=num_cluster, terms=cluster_info["terms"], level=level)
    cluster.assign_reference_document(cluster_info["reference_doc"])
    cluster.save()
    if with_documents:
        for doc in cluster_info["documents"]:
            cluster.add_document(doc)
    return cluster

def mock_tree(max_level=0, linked=False, with_documents=True, document_types="both", name=tree_name):
    mock_documents()
    tree = mock_empty_tree(document_types, name)
    tree.max_level = max_level
    tree.save()
    for level in range(0, max_level+1):
        num_clusters = len(example_tree[level]["clusters"])
        for n in range(0, num_clusters):
            mock_cluster_for_tree(tree, n, level, with_documents)
        if linked:
            tree.link_children_to_parents(level)
    return tree
