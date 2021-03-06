from common.testing.validations_views import validate_page
from topics_identifier.models import Tree


def validate_generate_tree_view_post(test, response, tree_name):
    test.assertContains(response, "Generating tree: "+tree_name)
    tree = Tree.objects.get(name=tree_name)
    for cluster in tree.get_clusters_of_level(level=1):
        validate_contains_cluster(test, response, cluster, with_documents=False)

def validate_terms(test, response, terms_list):
    for term in terms_list:
        test.assertContains(response, term)

def validate_contains_document(test, response, doc_content):
    test.assertContains(response, doc_content[:10])

def validate_contains_cluster(test, response, cluster, with_documents=True):
    validate_contains_document(test, response, cluster.reference_document)
    validate_terms(test, response, cluster.get_terms())
    if with_documents:
        for doc in cluster.documents():
            validate_contains_document(test, response, doc.content)

def validate_contains_tree(test, response, tree, max_level=0):
    clusters_max_level = tree.get_clusters_of_level(max_level)
    for cluster in clusters_max_level:
        validate_contains_cluster(test, response, cluster, with_documents=False)

def validate_document_view(test, response, document):
    if document.is_news:
        test.assertContains(response, document.thread.title[:10])
    else:
        test.assertContains(response, document.content)
