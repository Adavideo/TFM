
def validate_page(test, response, head_text):
    test.assertEqual(response.status_code, 200)
    test.assertContains(response, head_text)
    return response
