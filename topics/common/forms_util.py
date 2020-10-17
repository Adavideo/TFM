import os
from config import document_types, sklearn_models_path
from timeline.models import Topic


# Documents types

def get_documents_options():
    options = []
    for type in document_types:
        options.append((type, type))
    return options


# Topics

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
            options.append((topic.id, topic.name))
    return options


# Models names

def get_model_name_from_filename(filename):
    parts = filename.split("_")
    if parts[0] == "delete" or parts[0] == "test":
        return None
    name = parts[0]
    for text in parts[1:]:
        if text == "model":
            return name
        elif text == "vectorizer" or text == "reference_document":
            return None
        else:
            name += "_" + text
    return None

def get_models_names():
    files = os.listdir(sklearn_models_path)
    models_names = []
    for filename in files:
        name = get_model_name_from_filename(filename)
        if name and (name not in models_names):
            models_names.append(name)
    return models_names

def get_models_options():
    models_names = get_models_names()
    if models_names:
        options = []
        for name in models_names:
            options.append((name, name))
    else:
        options = [("","")]
    return options
