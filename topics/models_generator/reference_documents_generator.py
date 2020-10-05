from topics_identifier.ClustersGenerator import ClustersGenerator


def generate_reference_documents(model_name, documents, level):
    clusters_generator = ClustersGenerator(model_name, level)
    reference_documents = clusters_generator.get_reference_documents(documents)
    return reference_documents
