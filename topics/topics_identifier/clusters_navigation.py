from .models import Cluster

def get_datasets_names_from_clusters():
    datasets_names = []
    for cluster in Cluster.objects.all():
        if cluster.dataset not in datasets_names:
            datasets_names.append(cluster.dataset)
    return datasets_names

def get_datasets_clusters_list():
    datasets_names = get_datasets_names_from_clusters()
    datasets_list = []
    for dataset_name in datasets_names:
        num_clusters = len(Cluster.objects.filter(dataset=dataset_name))
        info = { "dataset_name": dataset_name, "num_clusters": num_clusters }
        datasets_list.append(info)
    return datasets_list

def insert_children(cluster, cluster_info):
    print("\ninsert_children")
    print(cluster)
    children = cluster.children()
    print(children)
    children_with_documents = get_clusters_list_with_documents(children)
    cluster_info["children"] = children_with_documents

def get_clusters_list_with_documents(clusters, include_children=False):
    clusters_list = []
    for cluster in clusters:
        docs = cluster.documents()
        cluster_info = {"cluster": cluster, "documents": docs}
        if include_children:
            insert_children(cluster, cluster_info)
        clusters_list.append(cluster_info)
    return clusters_list

def get_clusters_with_documents(dataset_name="", level=0, include_children=False):
    if dataset_name:
        clusters = Cluster.objects.filter(dataset=dataset_name, level=level)
    else:
        clusters = Cluster.objects.all()
    clusters_list = get_clusters_list_with_documents(clusters, include_children)
    return clusters_list
