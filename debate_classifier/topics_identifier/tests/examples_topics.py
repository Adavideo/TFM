from .examples import news_content, example_documents, news_titles


example_labeled_documents = [ news_content[0], news_content[1]]

example_documents_to_label = [
    news_content[2], news_content[3], news_content[4],
    news_content[5], news_content[6], news_content[7],
    news_content[8], news_content[9], news_content[10] ]

example_clusters_documents = example_documents_to_label + example_labeled_documents

example_titles_list = [ news_titles[0], news_titles[1], '']

example_news_titles_file = {
    "path": "topics_identifier/tests/example_titles.txt",
    "name": "example_titles.txt",
    "size": 334,
    "type": "text/plain",
    "charset": "utf8",
    "documents": example_titles_list
}
