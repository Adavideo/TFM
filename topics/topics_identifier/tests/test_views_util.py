from django.test import TestCase
from topics_identifier.views_util import *
from .mock_documents import mock_documents
from .mock_clusters import mock_clusters_list
from testing_commons.mock_web_client import post_request
from .mocks import mock_topic
from .examples_models import test_model_name


class ViewsUtilTests(TestCase):

    def test_build_tree_generator(self):
        #Initialize
        level=1
        page = 'generate_tree'
        tree_name = "prueba"
        parameters = { "tree_name": tree_name,"model_name":test_model_name, "document_types":"both"}
        mock_documents()
        request = post_request(page, parameters)
        #Execute
        tree_generator = build_tree_generator(request, level)
        #Validate
        self.assertEqual(str(type(tree_generator)), "<class 'topics_identifier.TreeGenerator.TreeGenerator'>")
        self.assertEqual(tree_generator.tree.name, tree_name)

    def test_assign_topic_to_clusters(self):
        #Initialize
        page = "assign_topic_to_clusters"
        mocked_topic = mock_topic()
        mocked_clusters = mock_clusters_list(num=3)
        clusters_ids = [ cluster.id for cluster in mocked_clusters ]
        parameters = { "topic": mocked_topic.id, "selected_clusters": clusters_ids }
        request = post_request(page, parameters)
        #Execute
        topic, clusters_list = assign_topic_to_clusters(request)
        #Validate
        self.assertEqual(topic, mocked_topic)
        self.assertEqual(len(clusters_list), 3)
        self.assertEqual(clusters_list, mocked_clusters)
