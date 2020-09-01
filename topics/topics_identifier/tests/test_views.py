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

    def test_trees_index_view(self):
        page = 'trees_index'
        response = validate_page(self, page)

    def test_tree_view_level0(self):
        page = 'tree'
        tree = mock_tree(max_level=0, linked=True, with_documents=True, document_types="both")
        response = validate_page(self, page, arguments=[tree.id])
        validate_contains_tree(self, response, tree)

    def test_tree_view_level1(self):
        page = 'tree'
        tree = mock_tree(max_level=1, linked=True, with_documents=True, document_types="both")
        response = validate_page(self, page, arguments=[tree.id])
        validate_contains_tree(self, response, tree, max_level=1)

    def test_cluster(self):
        page = 'cluster'
        cluster = mock_cluster(with_documents=True)
        cluster.save()
        response = validate_page(self, page, arguments=[cluster.id])
        validate_contains_cluster(self, response, cluster)

    def test_cluster_topic(self):
        page = 'cluster_topic'
        response = validate_page(self, page)
