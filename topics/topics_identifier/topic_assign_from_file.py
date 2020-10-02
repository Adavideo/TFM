from .models import Document, Topic
from config import assign_topic_path


def get_filename(topic_name):
    filename = assign_topic_path+topic_name+".txt"
    return filename

def read_file(filename):
    try:
        file = open(filename)
        texts_list = file.read().split("\n")
        return texts_list
    except:
        return []

def find_thread(text):
    all_news = Document.objects.filter(is_news=True)
    for news in all_news:
        if news.thread and news.thread.title in text:
            return news.thread

def find_threads_from_texts(texts_list):
    threads_list = []
    for text in texts_list:
        if not text: continue
        thread = find_thread(text)
        if thread: threads_list.append(thread)
    return threads_list

def assign_topic_from_file(topic_name):
    topic, created = Topic.objects.get_or_create(name=topic_name)
    filename = get_filename(topic_name)
    texts_list = read_file(filename)
    threads_list = find_threads_from_texts(texts_list)
    topic.assign_threads_list(threads_list)
    return threads_list
