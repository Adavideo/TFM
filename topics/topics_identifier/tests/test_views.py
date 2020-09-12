from django.test import TestCase
from topics_identifier.models import Tree
from .mocks import mock_documents
from .mock_clusters import mock_cluster
from .mock_trees import mock_tree
from .examples import test_model_name
from .views_util import get_response, post_response
from .validations_views import *


class ViewsTests(TestCase):

    def test_home_page(self):
        page = 'topics_identifier'
        response = get_response(page)
        validate_page(self, response)

    def test_generate_model_view_form(self):
        page = 'generate_model'
        response = get_response(page)
        validate_page(self, response)
        self.assertContains(response, "Model name")
        self.assertContains(response, "Document types")
        self.assertContains(response, "Max number of documents")
        self.assertContains(response, "Max tree level")

    def test_generate_model_view_post(self):
        #Initialize
        page = 'generate_model'
        name = "delete_me_generate_model_test"
        parameters = {
            "model_name": name,
            "document_types":"both",
            "max_num_documents": 100,
            "max_level": 1
        }
        mock_documents()
        #Execute
        response = post_response(page, parameters)
        #Validate
        validate_page(self, response)
        self.assertContains(response, "Generated model: "+ name)
        self.assertContains(response, "Filename:")
        model_filename = "models/sklearn/"+name+"_model_level1.joblib"
        self.assertContains(response, model_filename)

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
        validate_page(self, response)
        self.assertContains(response, "Generating tree: "+tree_name)
        tree = Tree.objects.get(name=tree_name)
        for cluster in tree.get_clusters_of_level(level=1):
            validate_contains_cluster(self, response, cluster, with_documents=False)

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

    def test_tree_view_level0_view(self):
        page = 'tree'
        tree = mock_tree(max_level=0, with_documents=True, document_types="both")
        response = get_response(page, arguments=[tree.id])
        validate_page(self, response)
        validate_contains_tree(self, response, tree)

    def test_tree_view_level1_view(self):
        page = 'tree'
        tree = mock_tree(max_level=1, linked=True, with_documents=True, document_types="both")
        response = get_response(page, arguments=[tree.id])
        validate_page(self, response)
        validate_contains_tree(self, response, tree, max_level=1)

    def test_cluster_view(self):
        page = 'cluster'
        cluster = mock_cluster(with_documents=True)
        cluster.save()
        response = get_response(page, arguments=[cluster.id])
        validate_page(self, response)
        validate_contains_cluster(self, response, cluster)

    def test_assign_topic_from_file_view(self):
        page = 'assign_topic_from_file'
        response = get_response(page)
        validate_page(self, response)

    def test_cluster_topic_view(self):
        page = 'cluster_topic'
        response = get_response(page)
        validate_page(self, response)
