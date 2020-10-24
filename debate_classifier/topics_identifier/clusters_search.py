from .models import Cluster
from .clusters_navigation import compose_cluster_information


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

def cluster_search(tree, search_string):
    search_results = []
    all_clusters = Cluster.objects.filter(tree=tree)
    for cluster in all_clusters:
        if terms_match(search_string, cluster.terms):
            cluster_info = compose_cluster_information(cluster, include_documents=False)
            search_results.append(cluster_info)
    return search_results
