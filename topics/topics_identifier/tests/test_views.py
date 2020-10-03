from django.test import TestCase
from topics_identifier.models import ClusterTopic
from .examples import test_model_name, threads_news
from .example_trees import example_terms
from .mocks import get_response, post_response, mock_topic, mock_documents
from .mock_clusters import mock_cluster, mock_clusters_list
from .mock_trees import mock_tree
from .mock_topics import *
from .validations_views import *
from .menus import topic_menu


class ViewsTests(TestCase):

    def test_home_page(self):
        page = 'topics_identifier'
        response = get_response(page)
        validate_page(self, response)

    # Test generate_tree_view

    def test_generate_tree_view_form(self):
        page = 'generate_tree'
        response = get_response(page)
        validate_page(self, response)
        self.assertContains(response, "Tree name")
        self.assertContains(response, "Model name")
        self.assertContains(response, "Document types")

    def test_generate_tree_view_post(self):
        #Initialize
        page = 'generate_tree'
        tree_name = "prueba"
        parameters = { "tree_name": tree_name,"model_name":test_model_name, "document_types":"both"}
        mock_documents()
        #Execute
        response = post_response(page, parameters)
        #Validate
        validate_generate_tree_view_post(self, response, tree_name)

    # Test trees_index_view

    def test_trees_index_view_empty(self):
        page = 'trees_index'
        response = get_response(page)
        validate_page(self, response)

    def test_trees_index_view_1tree(self):
        page = 'trees_index'
        tree = mock_tree(max_level=0, with_documents=True, document_types="both")
        response = get_response(page)
        validate_page(self, response)
        self.assertContains(response, tree.name)

    def test_trees_index_view_2trees(self):
        page = 'trees_index'
        tree1 = mock_tree(max_level=0, with_documents=True, document_types="both", name="tree1")
        tree2 = mock_tree(max_level=0, with_documents=True, document_types="both", name="tree2")
        response = get_response(page)
        validate_page(self, response)
        self.assertContains(response, tree1.name)
        self.assertContains(response, tree2.name)

    # Test tree_view

    def test_tree_view_level0(self):
        page = 'tree'
        tree = mock_tree(max_level=0, with_documents=True, document_types="both")
        response = get_response(page, arguments=[tree.id])
        validate_page(self, response)
        validate_contains_tree(self, response, tree)

    def test_tree_view_level1(self):
        page = 'tree'
        tree = mock_tree(max_level=1, linked=True, with_documents=True, document_types="both")
        response = get_response(page, arguments=[tree.id])
        validate_page(self, response)
        validate_contains_tree(self, response, tree, max_level=1)

    def test_tree_view_search_post_valid_search(self):
        #Initialize
        page = 'tree'
        tree = mock_tree(max_level=1, linked=True, with_documents=True, document_types="both")
        arguments = [ tree.id ]
        valid_term = 'inmunidad'
        parameters = { "search_terms": valid_term }
        #Execute
        response = post_response(page, parameters, arguments)
        #Validate
        validate_page(self, response)
        self.assertContains(response, "Topic")
        self.assertContains(response, 'Search for: '+str(valid_term))
        self.assertContains(response, "Select clusters")
        self.assertContains(response, "Level 0 - Cluster 2")

    def test_tree_view_search_post_empty_search(self):
        #Initialize
        page = 'tree'
        tree = mock_tree(max_level=1, linked=True, with_documents=True, document_types="both")
        arguments = [ tree.id ]
        parameters = { "search_terms": "" }
        #Execute
        response = post_response(page, parameters, arguments)
        #Validate
        validate_page(self, response)

    def test_tree_view_search_post_invalid_search(self):
        #Initialize
        page = 'tree'
        tree = mock_tree(max_level=1, linked=True, with_documents=True, document_types="both")
        arguments = [ tree.id ]
        parameters = { "search_terms": "aeiou" }
        #Execute
        response = post_response(page, parameters, arguments)
        #Validate
        validate_page(self, response)

    # Test cluster_view

    def test_cluster_view(self):
        page = 'cluster'
        cluster = mock_cluster(with_documents=True)
        cluster.save()
        response = get_response(page, arguments=[cluster.id])
        validate_page(self, response)
        validate_contains_cluster(self, response, cluster)

    # Test topics_index_view

    def test_topics_index_view(self):
        page = 'topics_index'
        topic1 = mock_topic(name="topic1")
        topic2 = mock_topic(name="topic2")
        response = get_response(page)
        validate_page(self, response)
        self.assertContains(response, topic1.name)
        self.assertContains(response, topic2.name)

    # Test topic_view

    def test_topic_view_empty(self):
        # Initialize
        page = "topic"
        topic = mock_topic()
        # Execute
        response = get_response(page, arguments=[topic.id])
        # Validate
        validate_page(self, response, menu=topic_menu)

    def test_topic_view_with_documents(self):
        # Initialize
        page = "topic"
        topic = mock_topic()
        threads_list = mock_threads_with_topic(topic)
        # Execute
        response = get_response(page, arguments=[topic.id])
        # Validate
        validate_page(self, response, menu=topic_menu)
        for thread in threads_list:
            news_content = thread.news().content
            validate_contains_document(self, response, news_content)

    # Test topic_clusters_view

    def test_topic_clusters_view(self):
        # Initialize
        page = 'topic_clusters'
        topic, topic_clusters = mock_topic_with_clusters()
        # Execute
        response = get_response(page, arguments=[topic.id])
        # Validate
        validate_page(self, response, menu=topic_menu)
        self.assertContains(response, topic.name)
        for cluster in topic_clusters:
            cluster_text = "Level 0 - Cluster "+str(cluster.number)
            self.assertContains(response, cluster_text)
            for doc in cluster.documents():
                validate_contains_document(self, response, doc.content)

    # Test assign_topic_to_clusters_view

    def test_assign_topic_to_clusters_view(self):
        #Initialize
        page = "assign_topic_to_clusters"
        mocked_topic = mock_topic()
        mocked_clusters = mock_clusters_list(num=3)
        clusters_ids = [ cluster.id for cluster in mocked_clusters ]
        parameters = { "topic": mocked_topic.id, "selected_clusters": clusters_ids }
        #Execute
        response = post_response(page, parameters)
        #Validate
        validate_page(self, response)
        self.assertContains(response, mocked_topic.name)
        for cluster in mocked_clusters:
            text = "Level "+ str(cluster.level)+" - Cluster "+str(cluster.number)
            self.assertContains(response, text)

    # Test label_documents_view

    def test_label_documents_view_get_no_clusters(self):
        #Initialize
        page = "label_documents"
        topic = mock_topic()
        # Execute
        response = get_response(page, arguments=[topic.id])
        # Validate
        validate_page(self, response, menu=topic_menu)
        self.assertContains(response, topic.name)

    def test_label_documents_view_get_with_clusters(self):
        #Initialize
        page = "label_documents"
        topic, topic_clusters = mock_topic_with_clusters()
        # Execute
        response = get_response(page, arguments=[topic.id])
        # Validate
        validate_page(self, response, menu=topic_menu)
        self.assertContains(response, topic.name)
        for cluster in topic_clusters:
            for doc in cluster.documents():
                validate_contains_document(self, response, doc.content)

    def test_label_documents_view_post(self):
        #Initialize
        page = "label_documents"
        topic = mock_threads_and_clusters_with_topic()
        threads = topic.get_threads()
        documents_ids = [ threads[0].news().id, threads[1].news().id ]
        parameters = {"documents": documents_ids}
        # Execute
        response = post_response(page, parameters, arguments=[topic.id])
        # Validate
        validate_page(self, response, menu=topic_menu)
        self.assertContains(response, topic.name)

    # Test assign_topic_from_file_view

    def test_assign_topic_from_file_view_form(self):
        page = 'assign_topic_from_file'
        response = get_response(page)
        validate_page(self, response)
        self.assertContains(response, "Topic:")

    def test_assign_topic_from_file_view_post(self):
        #Initialize
        page = 'assign_topic_from_file'
        topic = mock_topic("prueba")
        threads = mock_threads_with_topic(topic)
        parameters = { "topic": topic.id }
        # Execute
        response = post_response(page, parameters)
        validate_page(self, response)
        head_text = "Threads of topic "+topic.name
        self.assertContains(response, head_text)
        for content in threads_news:
            self.assertContains(response, content[:10])

    def test_assign_topic_from_file_view_post_no_threads(self):
        page = 'assign_topic_from_file'
        topic = mock_topic("prueba")
        parameters = { "topic": topic.id }
        response = post_response(page, parameters)
        validate_page(self, response)
