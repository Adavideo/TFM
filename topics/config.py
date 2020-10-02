# models generator
sklearn_models_path = "models/sklearn/"
default_documents_limit = 10000
max_tree_level = 1
terms_max_length = 20000
reference_documents_max_length = 25000
document_types = ["news", "comments", "both"]

# topics identifier
tree_name_max_length = 25
batch_size = 1000
assign_topic_path = "topics_identifier/classified/"

# metrics
sample_size = 100

# csv import
headers_types = [
    { "file_type":"comments",
      "header": '"comment_id","comment_link_id","comment_user_id","comment_date","comment_content"'
    },
    { "file_type":"news",
      "header": 'link_id,link_author,link_date,link_uri,link_url_title,link_title,link_content'
    },
]
