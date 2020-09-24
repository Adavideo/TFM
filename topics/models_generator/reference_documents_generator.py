from topics_identifier.ClustersGenerator import ClustersGenerator


def generate_reference_documents(models_manager, model, vectorizer, documents, level):
    clusters_generator = ClustersGenerator(models_manager, level, model, vectorizer)
    reference_documents = clusters_generator.get_reference_documents(documents)
    return reference_documents
