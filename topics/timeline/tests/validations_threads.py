
def validate_thread(test, thread, expected, is_news):
    test.assertEqual(thread.number, expected["thread_number"])
    if is_news:
        test.assertEqual(thread.title, expected["title"])
        test.assertEqual(thread.uri, expected["uri"])

def validate_threads_list(test, threads_list, expected_threads):
    test.assertEqual(len(threads_list), len(expected_threads))
    for i in range(0, len(expected_threads)):
        test.assertEqual(threads_list[i], expected_threads[i])    
