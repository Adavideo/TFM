from topics_identifier.models import Tree, Document, Cluster
from .examples import news_content, comments_content
from .example_trees import example_tree, tree_name
from .mocks import ensure_documents, mock_document


def mock_empty_tree(document_types="both", name=tree_name, max_level=0):
    with_news = (document_types=="both" or document_types=="news")
    with_comments = (document_types=="both" or document_types=="comments")
    ensure_documents(with_news, with_comments)
    tree = Tree(name=name, news=with_news, comments=with_comments, max_level=max_level)
    tree.save()
    return tree

# We can not import mock cluster because it already imports mock_empty_tree
def mock_cluster_for_tree(tree, num_cluster, level, with_documents):
    cluster_info = example_tree[level]["clusters"][num_cluster]
    cluster = Cluster(tree=tree, number=num_cluster, terms=cluster_info["terms"], level=level)
    cluster.assign_reference_document(cluster_info["reference_doc"])
    cluster.save()
    if with_documents:
        for content in cluster_info["documents"]:
            doc = mock_document(content)
            cluster.add_document(doc)
    return cluster

def mock_tree(max_level=0, linked=False, with_documents=True, document_types="both", name=tree_name):
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
