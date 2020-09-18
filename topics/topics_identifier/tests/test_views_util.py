from django.test import TestCase
from topics_identifier.views_util import build_tree_generator
from .mock_documents import mock_documents
from .mock_web_client import post_request
from .examples import test_model_name


class ViewsUtilTests(TestCase):

    def test_build_tree_generator(self):
        #Initialize
        level=1
        page = 'generate_tree'
        tree_name = "prueba"
        parameters = { "tree_name": tree_name,"model_name":test_model_name, "document_types":"both"}
        mock_documents()
        request = post_request(page, parameters)
        self.assertEqual(request.method, "POST")
        #Execute
        tree_generator = build_tree_generator(request, level)
        #Validate
        self.assertEqual(str(type(tree_generator)), "<class 'topics_identifier.TreeGenerator.TreeGenerator'>")
        self.assertEqual(tree_generator.tree.name, tree_name)
