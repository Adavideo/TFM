from joblib import dump, load
from .ModelGenerator import ModelGenerator
from .ClustersGenerator import ClustersGenerator
from .datasets_manager import select_documents_level0
from .util import short_document_types
from .paths import sklearn_models_path

documents_limit = 1000

def get_model_filename(name, level):
    filename = sklearn_models_path + name + "_model_level" + str(level) + ".joblib"
    return filename

def get_vectorizer_filename(name, level):
    filename = sklearn_models_path + name + "_vectorizer_level" + str(level) + ".joblib"
    return filename

def store_model(model, name, level):
    filename = get_model_filename(name, level)
    dump(model, filename)
    return filename

def store_vectorizer(vectorizer, name, level):
    filename = get_vectorizer_filename(name, level)
    dump(vectorizer, filename)
    return filename

def load_model(name, level):
    filename = get_model_filename(name, level)
    try:
        model = load(filename)
        return model
    except:
        return None

def load_vectorizer(name, level):
    filename = get_vectorizer_filename(name, level)
    try:
        vectorizer = load(filename)
        return vectorizer
    except:
        return None

def load_model_and_vectorizer(name, level):
    model = load_model(name, level)
    vectorizer = load_vectorizer(name, level)
    return model, vectorizer

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

def get_next_level_documents(model, vectorizer, documents):
    clusters_generator = ClustersGenerator(model, vectorizer, documents)
    clusters_information = clusters_generator.get_clusters_information()
    return clusters_information["reference_documents"]

def generate_and_store_models(model_name, documents, max_level):
    for level in range(0, max_level+1):
        model_generator = ModelGenerator(documents)
        model = model_generator.generate_model()
        model_filename = store_model(model, model_name, level)
        vectorizer = model_generator.vectorizer
        store_vectorizer(vectorizer, model_name, level)
        if level < max_level+1:
            documents = get_next_level_documents(model, vectorizer, documents)

    return model_filename
