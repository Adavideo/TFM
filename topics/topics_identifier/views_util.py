from .TreeGenerator import TreeGenerator


def build_tree_generator(request, level):
    tree_name = request.POST["tree_name"]
    model_name = request.POST["model_name"]
    document_types = request.POST["document_types"]
    documents_options = { "types": document_types,
                          "max_num_documents": None,
                          "batches": True }
    tree_generator = TreeGenerator(tree_name, model_name, documents_options, max_level=level)
    return tree_generator
