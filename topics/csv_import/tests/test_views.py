from django.test import TestCase
from django.core.files.uploadedfile import InMemoryUploadedFile
from .views_util import get_response, post_response, validate_page
from .example_csv_to_import import example_csv

class ViewsTests(TestCase):

    def test_import_files_view_form(self):
        page = 'import_files'
        response = get_response(page)
        validate_page(self, response)

    def test_import_files_view_post(self):
        page = 'import_files'
        file = open(example_csv["path"], 'r')
        in_memory_file = InMemoryUploadedFile(
                            file=file, field_name="file",
                            name=example_csv["name"], content_type="text/csv",
                            size=example_csv["size"], charset=None)
        parameters = { "file": in_memory_file }
        response = post_response(page, parameters)
        validate_page(self, response)
        new_registers = len(example_csv["documents"])
        self.assertContains(response, "Processed "+str(new_registers)+" new registers")
        for doc in example_csv["documents"]:
            self.assertContains(response, doc)
