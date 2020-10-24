from common.testing.validations_threads import validate_thread
from common.testing.validations_documents import validate_content, validate_documents_content
from common.testing.validations_views import validate_page


def validate_threads_list_view(test, response, threads_list):
    for thread in threads_list:
        test.assertContains(response, thread.title[:10])
