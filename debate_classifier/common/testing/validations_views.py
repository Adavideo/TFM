

def validate_menu(test, response, menu):
    for text in menu:
        test.assertContains(response, text)

def validate_page(test, response, head_text, menu=None):
    test.assertEqual(response.status_code, 200)
    test.assertContains(response, head_text)
    if menu: validate_menu(test, response, menu)
