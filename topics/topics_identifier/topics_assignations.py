from .models import Document, Topic

def read_file(topic_name):
    filename = "topics_identifier/classified/"+topic_name+".txt"
    file = open(filename)
    texts_list = file.read().split("\n")
    return texts_list

def find_thread(text):
    content = "\n"+text
    all_news = Document.objects.filter(is_news=True)
    for news in all_news:
        if news.thread:
            if news.thread.title in text:
                return news.thread

def get_threads_on_the_topic_from_file(topic_name):
    texts_list = read_file(topic_name)
    threads_list = []
    for text in texts_list:
        if text:
            thread = find_thread(text)
            if thread: threads_list.append(thread)
    print(str(len(threads_list))+" threads found")
    return threads_list

def associate_threads_to_topic(topic):
    threads_list = get_threads_on_the_topic_from_file(topic.name)
    for thread in threads_list:
        thread.assign_topic(topic)
    return threads_list

def assign_topic_from_file(topic_name):
    topic, created = Topic.objects.get_or_create(name=topic_name)
    threads_list = associate_threads_to_topic(topic)
    return threads_list