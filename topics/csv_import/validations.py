
def validate_document(test, doc, expected, is_news):
    test.assertEqual(doc.content, expected["content"])
    test.assertEqual(doc.is_news, is_news)
    test.assertEqual(doc.author, expected["author"])
    test.assertEqual(doc.date, expected["date"])

def validate_processed_line(test, result, expected, is_news):
    test.assertEqual(result["thread_number"], expected["thread_number"])
    test.assertEqual(result["content"], expected["content"])
    test.assertEqual(result["author"], expected["author"])
    test.assertEqual(result["date"], expected["date"])
    if is_news:
        test.assertEqual(result["title"], expected["title"])
        test.assertEqual(result["uri"], expected["uri"])
