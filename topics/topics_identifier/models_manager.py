from joblib import dump, load
from .ModelGenerator import ModelGenerator
from .datasets_manager import select_documents_level0
from .util import short_document_types

path = "models/sklearn/"
documents_limit = 1000

def get_filename(name, level):
    filename = path + name + "_level" + str(level) + ".joblib"
    return filename

def get_terms_filename(name, level):
    terms_name = name + "_terms"
    filename = get_filename(terms_name, level)
    return filename

def store_model(model, name, level):
    filename = get_filename(name, level)
    dump(model, filename)
    return filename

def store_terms(terms, name, level):
    filename = get_terms_filename(name, level)
    dump(terms, filename)
    return filename

def load_model(name, level):
    filename = get_filename(name, level)
    try:
        model = load(filename)
        return model
    except:
        return None

def load_terms(name, level):
    filename = get_terms_filename(name, level)
    try:
        terms = load(filename)
        return terms
    except:
        return None

def load_model_and_terms(name, level):
    model = load_model(name, level)
    terms = load_terms(name, level)
    return model, terms


def ensure_documents_limit(documents):
    # Cutting to the maximum number of documents, to not overload the aviable memory.
    num_documents = len(documents)
    print("Documents selected: "+str(num_documents))
    if num_documents > documents_limit:
        print("Adjusting to limit of "+str(documents_limit)+" documents")
        documents = documents[:documents_limit]
    return documents

def select_documents(document_types):
    with_news, with_comments = short_document_types(document_types)
    documents = select_documents_level0(with_news, with_comments)
    documents = ensure_documents_limit(documents)
    return documents

def generate_and_store_model(model_name, documents):
    level = 0
    model_generator = ModelGenerator(documents)
    model = model_generator.generate_model()
    model_filename = store_model(model, model_name, level)
    terms = model_generator.get_all_terms()
    store_terms(terms, model_name, level)
    return model_filename
