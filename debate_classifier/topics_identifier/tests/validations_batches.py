from .example_trees import example_tree
from .examples import test_batch_size


def get_expected_batch_documents(documents_list, batch_size, batch_number):
    num_documents = len(documents_list)
    end = batch_size * batch_number
    start = end - batch_size
    batch = documents_list[start:end]
    return batch

def validate_batch_documents(test, level, batch_number, documents):
    level_documents = example_tree[level]["documents"]
    expected = get_expected_batch_documents(level_documents, test_batch_size, batch_number)
    test.assertEqual(documents, expected)
