from sklearn.cluster import AffinityPropagation
from topics_identifier.datasets_manager import load_dataset
from topics_identifier.generate_clusters import store_clusters, process_data

def create_and_store_clusters(dataset_name, documents, level=1):
    dataset = load_dataset(dataset_name)
    vectorized_documents, terms = process_data(dataset)
    model = AffinityPropagation()
    model.fit(vectorized_documents)
    store_clusters(model, dataset_name, terms, documents)
