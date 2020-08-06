from .example_trees import example_tree, tree_name, news_content, comments_content
from .mock_clusters import mock_cluster
from .mocks import mock_documents
from topics_identifier.models import Tree, Document
from topics_identifier.TreeGenerator import short_document_types


def mock_empty_tree(document_types="both"):
    with_news, with_comments = short_document_types(document_types)
    tree = Tree(name=tree_name, news=with_news, comments=with_comments)
    tree.save()
    return tree

def mock_tree(max_level=0, linked=False, with_documents=True, document_types="both"):
    mock_documents()
    tree = mock_empty_tree(document_types)
    for level in range(0, max_level+1):
        num_clusters = len(example_tree[level]["clusters"])
        for n in range(0, num_clusters):
            mock_cluster(tree, num_cluster=n, level=level, with_documents=with_documents)
        if linked:
            tree.link_children_to_parents(level)
    return tree
