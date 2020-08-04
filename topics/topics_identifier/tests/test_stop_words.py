from topics_identifier.stop_words import get_stop_words

def test_get_stop_words(self):
    stop_words = get_stop_words()
    self.assertEqual(stop_words, example_stop_words)
