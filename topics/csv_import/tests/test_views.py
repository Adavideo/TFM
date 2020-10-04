from django.test import TestCase
from .example_csv_to_import import example_csv
from .mocks import get_response, post_response, mock_file
from .validations import validate_page


head_text = "Import CSV file"

class ViewsTests(TestCase):

    def test_import_files_view_form(self):
        page = 'import_files'
        response = get_response(page)
        validate_page(self, response, head_text)

    def test_import_files_view_post(self):
        page = 'import_files'
        file = mock_file(example_csv)
        parameters = { "file": file }
        response = post_response(page, parameters)
        validate_page(self, response, head_text)
        new_registers = len(example_csv["documents"])
        self.assertContains(response, "Processed "+str(new_registers)+" new registers")
        for doc in example_csv["documents"]:
            self.assertContains(response, doc)
