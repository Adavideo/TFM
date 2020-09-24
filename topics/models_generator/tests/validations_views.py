
def validate_page(test, response):
    test.assertEqual(response.status_code, 200)
    head_text = "Topics identifier"
    test.assertContains(response, head_text)
    return response

def validate_generate_model_view(test, response, name, max_level):
    validate_page(test, response)
    test.assertContains(response, "Model generated: "+ name)
    test.assertContains(response, "Filenames:")
    for level in range(max_level+1):
        model_filename = "models/sklearn/"+name+"_model_level"+str(level)+".joblib"
        vectorizer_filename = "models/sklearn/"+name+"_vectorizer_level"+str(level)+".joblib"
        ref_docs_filename = "models/sklearn/"+name+"_reference_documents_level"+str(level)+".joblib"
        test.assertContains(response, model_filename)
        test.assertContains(response, vectorizer_filename)
        test.assertContains(response, ref_docs_filename)
