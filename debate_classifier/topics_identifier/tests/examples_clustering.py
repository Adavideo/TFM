from common.testing.example_documents import comments_content
from .example_trees import clusters_documents, example_predicted_clusters, tree_documents


example1 = {
    "documents": tree_documents[0],
    "predicted_clusters": example_predicted_clusters[0],
    "clusters_documents": clusters_documents[0]
}

example2 = {
    "documents": comments_content,
    "predicted_clusters": [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    "clusters_documents": [
        [ comments_content[2], comments_content[5] ],
        [ comments_content[0], comments_content[1],
          comments_content[3], comments_content[4],
          comments_content[6], comments_content[7],
          comments_content[8], comments_content[9], comments_content[10] ]
    ]
}
