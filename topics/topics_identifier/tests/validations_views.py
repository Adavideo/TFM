from topics_identifier.models import Tree

def validate_menu(test, response):
    menu_texts = ["Generate clusters tree", "Cluster topic threads", "Show trees"]
    for text in menu_texts:
        test.assertContains(response, text)

def validate_page(test, response):
    test.assertEqual(response.status_code, 200)
    head_text = "Topics identifier"
    test.assertContains(response, head_text)
    validate_menu(test, response)
    return response

def validate_generate_model_view_post(test, response, name, max_level):
    validate_page(test, response)
    test.assertContains(response, "Generated model: "+ name)
    test.assertContains(response, "Filenames:")
    for level in range(max_level+1):
        model_filename = "models/sklearn/"+name+"_model_level"+str(level)+".joblib"
        vectorizer_filename = "models/sklearn/"+name+"_vectorizer_level"+str(level)+".joblib"
        ref_docs_filename = "models/sklearn/"+name+"_reference_documents_level"+str(level)+".joblib"
        test.assertContains(response, model_filename)
        test.assertContains(response, vectorizer_filename)
        test.assertContains(response, ref_docs_filename)

def validate_generate_tree_view_post(test, response, tree_name):
    validate_page(test, response)
    test.assertContains(response, "Generating tree: "+tree_name)
    tree = Tree.objects.get(name=tree_name)
    for cluster in tree.get_clusters_of_level(level=1):
        validate_contains_cluster(test, response, cluster, with_documents=False)

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

def validate_cluster_topic_threads_post(test, response, topic_name):
    validate_page(test, response)
    test.assertContains(response, topic_name)
    tree = Tree.objects.get(name=topic_name)
    test.assertContains(response, tree.name)
    for cluster in tree.get_clusters_of_level(level=0):
        validate_contains_cluster(test, response, cluster, with_documents=False)
