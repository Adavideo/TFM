from .models import Thread


def store_thread(thread_number):
    filename = "missing_news.txt"
    out_file = open(filename, 'a')
    out_file.write(str(thread_number)+", ")
    out_file.close()

def check_threads_without_news():
    threads_without_title = Thread.objects.filter(title=None)
    threads_without_news = []
    for thread in threads_without_title:
        store_thread(thread.number)
        threads_without_news.append(thread)
    return threads_without_news
