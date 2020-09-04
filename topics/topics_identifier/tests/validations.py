from timeline.tests.validations_threads import validate_threads_list


def validate_dataset(test, dataset, expected_content):
    test.assertEqual(str(type(dataset)), "<class 'sklearn.utils.Bunch'>")
    test.assertEqual(dataset.data, expected_content)
