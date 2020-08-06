from .examples import example_author, example_date


# Compares the content of the document with the example documents
def validate_documents(test, documents, expected_content_list):
    test.assertEqual(len(documents), len(expected_content_list))
    doc_index = 0
    for doc in documents:
        test.assertEqual(doc.content, expected_content_list[doc_index])
        test.assertEqual(doc.author, example_author)
        test.assertEqual(doc.date, example_date)
        doc_index +=1

# Compares a list of strings with the example documents
def validate_documents_content(test, documents_content, expected_content):
    num_of_documents = len(documents_content)
    test.assertEqual(num_of_documents, len(expected_content))
    for i in range(0, num_of_documents):
        test.assertEqual(documents_content[i], expected_content[i])
