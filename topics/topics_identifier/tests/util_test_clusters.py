from topics_identifier.models import Cluster, Document
from .examples_text_datasets_and_documents import test_dataset, example_documents

def mock_cluster(num_cluster=0, level=1, documents=False):
    dataset_name = test_dataset["name"]
    cluster_info = test_dataset["clusters"][num_cluster]
    cluster = Cluster(dataset=dataset_name, number=num_cluster, terms=cluster_info["terms"], level=level)
    cluster.assign_reference_document(cluster_info["reference_doc"])
    cluster.save()
    if documents:
        for doc in cluster_info["documents"]:
            cluster.add_document(doc)
    return cluster

def mock_document(type="short"):
    if type == "short":
        content = example_documents["short"][0]
    else:
        content = example_documents["long"][0]
    doc = Document(content=content)
    doc.save()
    return doc
