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

def get_terms_from_string(terms_string):
    terms_list = terms_string.split(",")
    characters_to_remove = ["'","[","]"]
    i = 0
    for term in terms_list:
        cleaned_term = term.strip()
        for c in characters_to_remove:
            cleaned_term = cleaned_term.replace(c,'')
        terms_list[i] = cleaned_term
        i += 1
    return terms_list

def get_match_list(search_terms, cluster_terms):
    match_list = []
    for term in search_terms:
        term_match = False
        for cluster_term in cluster_terms:
            if term == cluster_term:
                term_match = True
        match_list.append(term_match)
    return match_list


def terms_match(search_string, cluster_terms_string):
    if not search_string:
        return False
    search_terms = get_terms_from_string(search_string)
    cluster_terms = get_terms_from_string(cluster_terms_string)
    match_list = get_match_list(search_terms, cluster_terms)
    # If any of the terms doesn't match returns False
    for term_match in match_list:
        if not term_match:
            return False
    return True

def cluster_search(dataset_name, search_string):
    clusters_tree = []
    all_clusters = Cluster.objects.filter(dataset=dataset_name)
    for cluster in all_clusters:
        if terms_match(search_string, cluster.terms):
            tree = compose_clusters_tree([cluster], include_documents=False)
            clusters_tree.append(tree)
    return clusters_tree
