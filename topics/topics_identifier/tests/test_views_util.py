from django.test import TestCase
from topics_identifier.views_util import *
from .examples import test_model_name
from .mocks import *
from .mock_clusters import mock_clusters_list


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

    def test_get_topic_clusters_with_documents(self):
        topic, topic_clusters = mock_topic_with_clusters()
        clusters_with_documents = get_topic_clusters_with_documents(topic)
        for i in range(len(topic_clusters)):
            cluster = clusters_with_documents[i]["cluster"]
            self.assertEqual(cluster, topic_clusters[i])
            documents = cluster.documents()
            expected = topic_clusters[i].documents()
            self.assertNotEqual(len(expected), 0)
            for i in range(len(expected)):
                self.assertEqual(documents[i].content, expected[i].content )

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
