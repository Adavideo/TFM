from django.test import TestCase
from .mock_clusters import mock_cluster
from .mock_trees import mock_tree
from .validations_views import *


class ViewsTests(TestCase):

    def test_home_page(self):
        page = 'topics_identifier'
        response = validate_page(self, page)

    def test_generate_model_view(self):
        page = 'generate_model'
        response = validate_page(self, page)

    def test_generate_tree_view(self):
        page = 'generate_tree'
        response = validate_page(self, page)

    def test_trees_index_view_empty(self):
        page = 'trees_index'
        response = validate_page(self, page)

    def test_trees_index_view_1tree(self):
        page = 'trees_index'
        tree = mock_tree(max_level=0, with_documents=True, document_types="both")
        response = validate_page(self, page)
        self.assertContains(response, tree.name)

    def test_trees_index_view_2trees(self):
        page = 'trees_index'
        tree1 = mock_tree(max_level=0, with_documents=True, document_types="both", name="tree1")
        tree2 = mock_tree(max_level=0, with_documents=True, document_types="both", name="tree2")
        response = validate_page(self, page)
        self.assertContains(response, tree1.name)
        self.assertContains(response, tree2.name)

    def test_tree_view_level0_view(self):
        page = 'tree'
        tree = mock_tree(max_level=0, with_documents=True, document_types="both")
        response = validate_page(self, page, arguments=[tree.id])
        validate_contains_tree(self, response, tree)

    def test_tree_view_level1_view(self):
        page = 'tree'
        tree = mock_tree(max_level=1, linked=True, with_documents=True, document_types="both")
        response = validate_page(self, page, arguments=[tree.id])
        validate_contains_tree(self, response, tree, max_level=1)

    def test_cluster_view(self):
        page = 'cluster'
        cluster = mock_cluster(with_documents=True)
        cluster.save()
        response = validate_page(self, page, arguments=[cluster.id])
        validate_contains_cluster(self, response, cluster)

    def test_assign_topic_from_file_view(self):
        page = 'assign_topic_from_file'
        response = validate_page(self, page)

    def test_cluster_topic_view(self):
        page = 'cluster_topic'
        response = validate_page(self, page)
