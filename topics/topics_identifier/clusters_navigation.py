from .models import Cluster

def get_datasets_names_from_clusters():
    datasets_names = []
    for cluster in Cluster.objects.all():
        if cluster.dataset not in datasets_names:
            datasets_names.append(cluster.dataset)
    return datasets_names

def get_max_level(dataset_name):
    clusters = Cluster.objects.filter(dataset=dataset_name)
    max_level = 0
    for cluster in Cluster.objects.all():
        if cluster.level > max_level:
            max_level = cluster.level
    return max_level

def get_datasets_clusters_list():
    datasets_names = get_datasets_names_from_clusters()
    datasets_list = []
    for dataset_name in datasets_names:
        num_clusters = len(Cluster.objects.filter(dataset=dataset_name, level=0))
        max_level = get_max_level(dataset_name)
        info = { "dataset_name": dataset_name, "num_clusters": num_clusters, "levels":max_level+1 }
        datasets_list.append(info)
    return datasets_list

def insert_children(cluster, cluster_info, include_documents):
    children = cluster.children()
    children_tree = compose_clusters_tree(children, include_documents)
    cluster_info["children"] = children_tree

def compose_clusters_tree(clusters, include_documents):
    clusters_tree = []
    for cluster in clusters:
        cluster_info = {"cluster": cluster }
        insert_children(cluster, cluster_info, include_documents)
        if include_documents:
            cluster_info["documents"] = cluster.documents()
        clusters_tree.append(cluster_info)
    return clusters_tree

def get_clusters_tree(dataset_name, include_documents):
    level = get_max_level(dataset_name)
    clusters = Cluster.objects.filter(dataset=dataset_name, level=level)
    clusters_tree = compose_clusters_tree(clusters, include_documents)
    return clusters_tree
