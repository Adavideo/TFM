from django.test import TestCase
from topics_identifier.tree_manager import generate_tree


class TreeManagerTests(TestCase):

    def test_generate_tree(self):
        # Initialize
        tree_name = "test_tree"
        model_name = "test_model"
        documents_options = { "types": "both" }
        # Execution
        results = generate_tree(tree_name, model_name, documents_options)
        # Validation
        clusters = results["clusters"]
        self.assertEqual(len(clusters), 0)
