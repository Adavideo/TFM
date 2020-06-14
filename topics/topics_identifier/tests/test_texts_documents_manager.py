from django.test import TestCase
from topics_identifier.texts_documents_manager import count_existing_files, store_text_in_file
from topics_identifier.file_paths import texts_path


class DocumentsManagerTests(TestCase):

    def test_count_existing_files_news(self):
        count = count_existing_files(type="news")
        self.assertIs(type(count), type(0))

    def test_count_existing_files_comments(self):
        count = count_existing_files(type="comments")
        self.assertIs(type(count), type(0))

    def test_count_existing_files_comments(self):
        count = count_existing_files(directory=texts_path)
        self.assertIs(type(count), type(0))

    def test_store_text_in_file_news(self):
        content = "Bla bla"
        file_type = "news"
        data_name = "test_delete_me"
        store_text_in_file(content, file_type, data_name, file_number=1)
        filename = texts_path+file_type+"/test_delete_me_1.txt"
        stored_file_content = open(filename, 'r').read()
        self.assertEqual(stored_file_content, content)

    def test_store_text_in_file_comments(self):
        content = "Bla bla"
        file_type = "comments"
        data_name = "test_delete_me"
        store_text_in_file(content, file_type, data_name, file_number=1)
        filename = texts_path+file_type+"/test_delete_me_1.txt"
        stored_file_content = open(filename, 'r').read()
        self.assertEqual(stored_file_content, content)
