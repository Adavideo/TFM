from django.urls import reverse

def validate_menu(test, response):
    menu_texts = ["Generate model", "Generate clusters tree", "Cluster for topic", "Show trees"]
    for text in menu_texts:
        test.assertContains(response, text)

def validate_page(test, page, arguments=[]):
    if arguments:
        url = reverse(page, args=arguments)
    else:
        url = reverse(page)
    response = test.client.get(url)
    test.assertEqual(response.status_code, 200)
    head_text = "Topics identifier"
    test.assertContains(response, head_text)
    validate_menu(test, response)
    return response

def validate_terms(test, response, terms_list):
    for term in terms_list:
        test.assertContains(response, term)

def validate_contains_cluster(test, response, cluster, with_documents=True):
    test.assertContains(response, cluster.reference_document)
    validate_terms(test, response, cluster.get_terms())
    if with_documents:
        for doc in cluster.documents():
            test.assertContains(response, doc.content)

def validate_contains_tree(test, response, tree, max_level=0):
    clusters_max_level = tree.get_clusters_of_level(max_level)
    for cluster in clusters_max_level:
        validate_contains_cluster(test, response, cluster, with_documents=False)
