from .example_documents import example_author, example_date


# Compares the content of the document with the example documents
def validate_documents(test, documents, expected_content_list):
    for i in range(len(expected_content_list)):
        test.assertEqual(documents[i].content, expected_content_list[i])
        test.assertEqual(documents[i].author, example_author)
        test.assertEqual(documents[i].date, example_date)

# Validate that all the documents content is in the content_list
def validate_documents_content(test, documents_list, content_list):
    test.assertEqual(len(documents_list), len(content_list))
    for doc in documents_list:
        test.assertTrue(doc.content in content_list)
