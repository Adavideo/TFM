

def get_search_clusters(search_results):
    clusters_options = []
    for cluster_info in search_results:
        cluster = cluster_info["cluster"]
        cluster_name = "Level "+str(cluster.level)+" - cluster "+str(cluster.number)
        option = ( cluster.id, cluster_name )
        clusters_options.append(option)
    return clusters_options
