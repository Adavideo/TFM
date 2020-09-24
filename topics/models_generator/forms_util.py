from config import max_tree_level, document_types


def get_documents_options():
    options = []
    for type in document_types:
        options.append((type, type))
    return options

def get_tree_levels():
    options = []
    max_level = int(max_tree_level) + 1
    for level in range(max_level):
        options.append((level, str(level)))
    return options
