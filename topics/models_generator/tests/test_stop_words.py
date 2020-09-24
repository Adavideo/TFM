from django.test import TestCase
from models_generator.stop_words.stop_words import get_stop_words
from .example_stop_words import example_stop_words


class StopWordsTests(TestCase):

    def test_get_stop_words(self):
        stop_words = get_stop_words()
        self.assertEqual(stop_words, example_stop_words)
