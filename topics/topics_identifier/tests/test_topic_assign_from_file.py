from django.test import TestCase
from topics_identifier.models import Topic
from topics_identifier.topic_assign_from_file import *
from config import assign_topic_path
from .examples import news_content, news_titles
from .examples_topics import example_titles_list, example_news_titles_file
from .mocks import mock_thread, mock_threads_list, mock_file
from .validations import validate_threads_list

topic = Topic(name="prueba")


class AssignTopicsTests(TestCase):

    def test_read_titles_file(self):
        file = mock_file(example_news_titles_file)
        titles_list = read_titles_file(file)
        self.assertEqual(len(titles_list), 3)
        self.assertEqual(titles_list[0], news_titles[0])
        self.assertEqual(titles_list[1], news_titles[1])

    def test_find_thread(self):
        mocked_thread = mock_thread(thread_number=0, with_documents=True, news_number=0)
        thread = find_thread(news_titles[0])
        self.assertEqual(thread, mocked_thread)
        news = thread.news()
        self.assertEqual(news.content, news_content[0])

    def test_find_threads_from_titles(self):
        expected_threads = mock_threads_list()
        topic_threads = find_threads_from_titles(example_titles_list)
        validate_threads_list(self, topic_threads, expected_threads)

    def test_find_threads_from_titles_empty(self):
        topic_threads = find_threads_from_titles(titles_list=[])
        validate_threads_list(self, topic_threads, [])

    def test_assign_topic_from_file(self):
        expected_threads = mock_threads_list()
        file = mock_file(example_news_titles_file)
        topic.save()
        threads_list = assign_topic_from_file(topic, file)
        validate_threads_list(self, threads_list, expected_threads)
