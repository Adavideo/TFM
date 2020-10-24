from common.testing.example_documents import *
from common.testing.example_models import test_model_name
from common.testing.example_threads import news_titles, threads_news


test_batch_size = 4

doc_options_with_batches = { "types":"both", "batches": True }

filenames_test_list = [
    "delete_me_model_level0.joblib",
    "test_model_level0.joblib",
    "test_model_level1.joblib",
    "test_vectorizer_level0.joblib",
    "test_reference_documents_level0.joblib",
    "news_model_level0.joblib",
    "news_model_level1.joblib",
    "news_vectorizer_level0.joblib",
    "news_reference_documents_level0.joblib"
]
