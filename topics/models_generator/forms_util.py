from config import max_tree_level


def get_documents_options():
    document_types = ["news", "comments", "both"]
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
