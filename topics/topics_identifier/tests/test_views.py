from django.test import TestCase
from .examples import test_model_name
from .example_trees import example_terms
from .mocks import mock_topic, mock_documents, get_response, post_response
from .mock_clusters import mock_cluster, mock_clusters_list
from .mock_trees import mock_tree
from .validations_views import *


class ViewsTests(TestCase):

    def test_home_page(self):
        page = 'topics_identifier'
        response = get_response(page)
        validate_page(self, response)

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
        valid_term = example_terms[8]
        parameters = { "search_terms": valid_term }
        #Execute
        response = post_response(page, parameters, arguments)
        #Validate
        validate_page(self, response)
        self.assertContains(response, "Topic")
        self.assertContains(response, 'Search for: '+str(valid_term))
        self.assertContains(response, "Select clusters")
        self.assertContains(response, "Level 0 - Cluster 1")

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

    def test_cluster_view(self):
        page = 'cluster'
        cluster = mock_cluster(with_documents=True)
        cluster.save()
        response = get_response(page, arguments=[cluster.id])
        validate_page(self, response)
        validate_contains_cluster(self, response, cluster)

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

    def test_assign_topic_from_file_view(self):
        page = 'assign_topic_from_file'
        response = get_response(page)
        validate_page(self, response)
