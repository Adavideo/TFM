
def compose_cluster_information(cluster, include_documents):
    cluster_info = {"cluster": cluster }
    insert_children(cluster, cluster_info, include_documents)
    if include_documents:
        cluster_info["documents"] = cluster.documents()
    return cluster_info

def compose_clusters_list(clusters, include_documents):
    clusters_list = []
    for cluster in clusters:
        cluster_info = compose_cluster_information(cluster, include_documents)
        clusters_list.append(cluster_info)
    return clusters_list

def insert_children(cluster, cluster_info, include_documents):
    children = cluster.children()
    children_tree = compose_clusters_list(children, include_documents)
    cluster_info["children"] = children_tree
