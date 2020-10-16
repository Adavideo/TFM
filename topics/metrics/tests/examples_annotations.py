
annotations_examples = {
    "agreement": [
        [True, False, False, True],  # annotator1
        [True, False, False, True],  # annotator2
        [True, False, False, True]   # annotator3
    ],
    "small disagreement": [
        [True, False, False, True],  # annotator1
        [True, True, False, True],   # annotator2
        [True, False, False, True]   # annotator3
    ],
    "big disagreement": [
        [True, False, False, False],  # annotator1
        [False, True, False, True],   # annotator2
        [True, False, True, True]     # annotator3
    ]
}
