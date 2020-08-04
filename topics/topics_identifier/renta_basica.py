from .models import Document

def read_file():
    filename = "topics_identifier/classified/noticias_renta_basica.txt"
    file = open(filename)
    texts_list = file.read().split("\n")
    return texts_list

def find_document(text):
    content = "\n"+text
    all_news = Document.objects.filter(is_news=True)
    for news in all_news:
        if news.thread.title in text:
            return news

def get_documents():
    texts_list = read_file()
    documents_list = []
    for text in texts_list:
        if text:
            doc = find_document(text)
            if doc: documents_list.append(doc)
    return documents_list
