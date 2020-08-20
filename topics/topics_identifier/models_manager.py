from joblib import dump, load
from .ModelGenerator import ModelGenerator
from .datasets_manager import select_documents_level0
from .util import short_document_types

path = "models/sklearn/"
documents_limit = 10000

def get_filename(name, level):
    filename = path + name + "_level" + str(level) + ".joblib"
    return filename

def store_model(model, name, level):
    filename = get_filename(name, level)
    dump(model, filename)
    return filename

def load_model(name, level):
    filename = get_filename(name, level)
    model = load(filename)
    return model

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

def generate_model(documents):
    model_generator = ModelGenerator(documents)
    model = model_generator.generate_model()
    return model

def generate_and_store_model(model_name, documents):
    model = generate_model(documents)
    model_filename = store_model(model, name=model_name, level=0)
    return model_filename
