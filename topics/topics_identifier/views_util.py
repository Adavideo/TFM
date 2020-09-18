from .models import Topic
from .TreeGenerator import TreeGenerator
from .config import max_tree_level


def get_documents_options():
    document_types = ["news", "comments", "both"]
    options = []
    for type in document_types:
        options.append((type, type))
    return options

def get_topics_options():
    try:
        topics_list = Topic.objects.all()
        len(topics_list)
    except:
        topics_list = None

    if not topics_list:
        options = [("","")]
    else:
        options = []
        for topic in topics_list:
            options.append((topic.id, topic))
    return options

def get_tree_levels():
    options = []
    max_level = int(max_tree_level) + 1
    for level in range(max_level):
        options.append((level, str(level)))
    return options

def build_tree_generator(request, level):
    tree_name = request.POST["tree_name"]
    model_name = request.POST["model_name"]
    document_types = request.POST["document_types"]
    documents_options = { "types": document_types,
                          "max_num_documents": None,
                          "batches": True }
    tree_generator = TreeGenerator(tree_name, model_name, documents_options, max_level=level)
    return tree_generator
