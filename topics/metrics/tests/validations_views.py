
def validate_page(test, response):
    test.assertEqual(response.status_code, 200)
    head_text = "Metrics"
    test.assertContains(response, head_text)
    return response
