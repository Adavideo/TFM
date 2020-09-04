from .examples import example_author, example_date


# Compares the content of the document with the example documents
def validate_documents(test, documents, expected_content_list):
    for i in range(len(documents)):
        test.assertEqual(documents[i].content, expected_content_list[i])
        test.assertEqual(documents[i].author, example_author)
        test.assertEqual(documents[i].date, example_date)
