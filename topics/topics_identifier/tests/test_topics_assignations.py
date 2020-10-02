from django.test import TestCase
from topics_identifier.models import Topic
from topics_identifier.topics_assignations import *
from config import assign_topic_path
from .examples import news_content, news_titles
from .examples_topics import example_texts_list
from .mocks import mock_thread, mock_threads_list
from .validations import validate_threads_list

topic = Topic(name="prueba")


class TopicsTests(TestCase):

    def test_get_filename(self):
        topic_name = "test"
        filename = get_filename(topic_name)
        self.assertEqual(filename, assign_topic_path+topic_name+".txt")

    def test_read_file(self):
        filename = get_filename(topic.name)
        texts_list = read_file(filename)
        self.assertEqual(len(texts_list), 3)
        self.assertEqual(texts_list[0], news_titles[0])
        self.assertEqual(texts_list[1], news_titles[1])

    def test_find_thread(self):
        mocked_thread = mock_thread(thread_number=0, with_documents=True, news_number=0)
        thread = find_thread(news_content[0])
        self.assertEqual(thread, mocked_thread)
        news = thread.news()
        self.assertEqual(news.content, news_content[0])

    def test_find_threads_from_texts(self):
        expected_threads = mock_threads_list()
        topic_threads = find_threads_from_texts(example_texts_list)
        validate_threads_list(self, topic_threads, expected_threads)

    def test_assign_topic_from_file(self):
        expected_threads = mock_threads_list()
        threads_list = assign_topic_from_file(topic.name)
        validate_threads_list(self, threads_list, expected_threads)
