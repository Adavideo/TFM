from django.test import TestCase
from topics_identifier.topics_manager import *
from .mocks import mock_thread
from .examples import news_content, all_threads_content
from .test_datasets_manager import validate_dataset
from .mock_datasets import mock_dataset_from_topics
from .example_topics import topic, example_terms, example_reference_documents


class TopicsTests(TestCase):

    def test_read_file(self):
        texts_list = read_file(topic)
        self.assertEqual(len(texts_list), 3)
        self.assertEqual(texts_list[0], news_content[0])
        self.assertEqual(texts_list[1], news_content[1])

    def test_find_thread(self):
        mocked_thread = mock_thread(thread_number=0, with_documents=True, news_number=0)
        thread = find_thread(news_content[0])
        self.assertEqual(thread, mocked_thread)
        news = thread.news()
        self.assertEqual(news.content, news_content[0])

    def test_get_threads_on_the_topic(self):
        thread0 = mock_thread(thread_number=0, with_documents=True, news_number=0)
        thread1 = mock_thread(thread_number=1, with_documents=True, news_number=1)
        topic_threads = get_threads_on_the_topic(topic)
        self.assertEqual(len(topic_threads), 2)
        self.assertEqual(topic_threads[0], thread0)
        self.assertEqual(topic_threads[1], thread1)

    def test_get_dataset_for_topic(self):
        mock_thread(thread_number=0, with_documents=True, news_number=0)
        mock_thread(thread_number=1, with_documents=True, news_number=1)
        dataset = get_dataset_for_topic(topic)
        validate_dataset(self, dataset, all_threads_content)

    def test_generate_clusters_for_topic(self):
        dataset = mock_dataset_from_topics(topic)
        clusters_information, documents_clusters = generate_clusters_for_topic(dataset)
        self.assertEqual(len(clusters_information), 2)
        self.assertEqual(clusters_information["terms"], example_terms)
        self.assertEqual(clusters_information["reference_documents"], example_reference_documents)

    def test_cluster_for_topic(self):
        mock_dataset_from_topics(topic)
        clusters_list = cluster_for_topic(topic)
        self.assertEqual(len(clusters_list), len(example_terms))
        self.assertEqual(str(clusters_list[0]), "Cluster - tree prueba, level 0, num cluster 0")
