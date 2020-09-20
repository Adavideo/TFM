from django.test import TestCase
from topics_identifier.models import Tree, Topic
from .mocks import mock_threads_with_topic
from .mock_documents import mock_documents
from .mock_clusters import mock_cluster
from .mock_trees import mock_tree
from .mock_web_client import get_response, post_response
from .examples_models import test_model_name
from .validations_views import *


class ViewsTests(TestCase):

    def test_home_page(self):
        page = 'topics_identifier'
        response = get_response(page)
        validate_page(self, response)

    def test_generate_model_view_form(self):
        page = 'generate_model'
        response = get_response(page)
        validate_page(self, response)
        self.assertContains(response, "Model name")
        self.assertContains(response, "Document types")
        self.assertContains(response, "Max number of documents")
        self.assertContains(response, "Max tree level")

    def test_generate_model_view_post_level0(self):
        #Initialize
        page = 'generate_model'
        name = "delete_me_generate_model_test"
        max_level = 0
        parameters = {
            "model_name": name,
            "document_types":"both",
            "max_num_documents": 100,
            "max_level": max_level
        }
        mock_documents()
        #Execute
        response = post_response(page, parameters)
        #Validate
        validate_page(self, response)
        self.assertContains(response, "Generated model: "+ name)
        self.assertContains(response, "Filenames:")
        model_filename = "models/sklearn/"+name+"_model_level0.joblib"
        vectorizer_filename = "models/sklearn/"+name+"_vectorizer_level0.joblib"
        ref_docs_filename = "models/sklearn/"+name+"_reference_documents_level0.joblib"
        self.assertContains(response, model_filename)
        self.assertContains(response, vectorizer_filename)
        self.assertContains(response, ref_docs_filename)

    def test_generate_model_view_post_level1(self):
        #Initialize
        page = 'generate_model'
        name = "delete_me_generate_model_test"
        max_level = 1
        parameters = {
            "model_name": name,
            "document_types":"both",
            "max_num_documents": 100,
            "max_level": max_level
        }
        mock_documents()
        #Execute
        response = post_response(page, parameters)
        #Validate
        validate_page(self, response)
        self.assertContains(response, "Generated model: "+ name)
        self.assertContains(response, "Filenames:")
        for level in range(max_level+1):
            model_filename = "models/sklearn/"+name+"_model_level"+str(level)+".joblib"
            vectorizer_filename = "models/sklearn/"+name+"_vectorizer_level"+str(level)+".joblib"
            ref_docs_filename = "models/sklearn/"+name+"_reference_documents_level"+str(level)+".joblib"
            self.assertContains(response, model_filename)
            self.assertContains(response, vectorizer_filename)
            self.assertContains(response, ref_docs_filename)

    def test_generate_tree_view_form(self):
        page = 'generate_tree'
        response = get_response(page)
        validate_page(self, response)
        self.assertContains(response, "Tree name")
        self.assertContains(response, "Model name")
        self.assertContains(response, "Document types")

    def test_generate_tree_view_post(self):
        #Initialize
        page = 'generate_tree'
        tree_name = "prueba"
        parameters = { "tree_name": tree_name,"model_name":test_model_name, "document_types":"both"}
        mock_documents()
        #Execute
        response = post_response(page, parameters)
        #Validate
        validate_generate_tree_view_post(self, response, tree_name)

    def test_trees_index_view_empty(self):
        page = 'trees_index'
        response = get_response(page)
        validate_page(self, response)

    def test_trees_index_view_1tree(self):
        page = 'trees_index'
        tree = mock_tree(max_level=0, with_documents=True, document_types="both")
        response = get_response(page)
        validate_page(self, response)
        self.assertContains(response, tree.name)

    def test_trees_index_view_2trees(self):
        page = 'trees_index'
        tree1 = mock_tree(max_level=0, with_documents=True, document_types="both", name="tree1")
        tree2 = mock_tree(max_level=0, with_documents=True, document_types="both", name="tree2")
        response = get_response(page)
        validate_page(self, response)
        self.assertContains(response, tree1.name)
        self.assertContains(response, tree2.name)

    def test_tree_view_level0_view(self):
        page = 'tree'
        tree = mock_tree(max_level=0, with_documents=True, document_types="both")
        response = get_response(page, arguments=[tree.id])
        validate_page(self, response)
        validate_contains_tree(self, response, tree)

    def test_tree_view_level1_view(self):
        page = 'tree'
        tree = mock_tree(max_level=1, linked=True, with_documents=True, document_types="both")
        response = get_response(page, arguments=[tree.id])
        validate_page(self, response)
        validate_contains_tree(self, response, tree, max_level=1)

    def test_cluster_view(self):
        page = 'cluster'
        cluster = mock_cluster(with_documents=True)
        cluster.save()
        response = get_response(page, arguments=[cluster.id])
        validate_page(self, response)
        validate_contains_cluster(self, response, cluster)

    def test_assign_topic_from_file_view(self):
        page = 'assign_topic_from_file'
        response = get_response(page)
        validate_page(self, response)

    def test_cluster_topic_threads_view_form(self):
        page = 'cluster_topic_threads'
        response = get_response(page)
        validate_page(self, response)
        self.assertContains(response, "Cluster topic threads")
        self.assertContains(response, "Topic")
        self.assertContains(response, "Model name")

    def test_cluster_topic_threads_view_post(self):
        #Initialize
        page = 'cluster_topic_threads'
        topic_name = "topic_test"
        topic = Topic(name=topic_name)
        mock_threads_with_topic(topic)
        parameters = { "model_name":test_model_name, "topic":topic.id}
        #Execute
        response = post_response(page, parameters)
        #Validate
        validate_cluster_topic_threads_post(self, response, topic_name)

    def test_cluster_topic_threads_view_post_same_topic_twice(self):
        #Initialize
        page = 'cluster_topic_threads'
        topic_name = "topic_test"
        topic = Topic(name=topic_name)
        mock_threads_with_topic(topic)
        parameters = { "model_name":test_model_name, "topic":topic.id}
        #Execute
        post_response(page, parameters)
        response = post_response(page, parameters)
        #Validate
        validate_cluster_topic_threads_post(self, response, topic_name+"_2")
