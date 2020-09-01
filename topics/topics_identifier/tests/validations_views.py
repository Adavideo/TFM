from django.urls import reverse

def validate_page(test, page, arguments=[]):
    if arguments:
        url = reverse(page, args=arguments)
    else:
        url = reverse(page)
    response = test.client.get(url)
    test.assertEqual(response.status_code, 200)
    test.assertContains(response, "Topics identifier")
    return response

def validate_contains_cluster(test, response, cluster, with_documents=True):
    test.assertContains(response, cluster.reference_document.content)
    if with_documents:
        for doc in cluster.documents():
            test.assertContains(response, doc.content)

def validate_contains_tree(test, response, tree, max_level=0):
    clusters_max_level = tree.get_clusters_of_level(max_level)
    for cluster in clusters_max_level:
        validate_contains_cluster(test, response, cluster, with_documents=False)
