from django.test import TestCase
from topics_identifier.forms import get_documents_options


class FormsTests(TestCase):

    def test_get_documents_options(self):
         options = get_documents_options()
         expected_result = [('news', 'news'), ('comments', 'comments'), ('both', 'both')]
         self.assertEqual(options, expected_result)
