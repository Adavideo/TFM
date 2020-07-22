from django.test import TestCase
from topics_identifier.datasets_manager import *
from .examples import example_tree, tree_name
from .util_test_generate_clusters import create_and_store_test_clusters
from .util_test_clusters import mock_documents


class DataClassifierTests(TestCase):

    def test_get_reference_documents(self):
        # Initialize
        level = 0
        mock_documents()
        create_and_store_test_clusters(level=level)
        # Execute
        documents = get_reference_documents(tree_name, level)
        # Verify
        example_clusters = example_tree[0]["clusters"]
        num_clusters = len(example_clusters)
        self.assertEqual(len(documents), num_clusters)
        for index in range(0,num_clusters):
            reference_document = example_clusters[index]["reference_doc"]
            self.assertEqual(documents[index], reference_document)
