from .models import Thread
from config import assign_topic_path


def read_titles_file(file):
    try:
        file_content = file.read()
        if not type(file_content) == type(""):
            file_content = file_content.decode("utf-8")
        titles_list = file_content.split("\n")
        return titles_list
    except:
        print("ERROR: Could not open the file")
        return []

def find_thread(title):
    thread_search = Thread.objects.filter(title=title)
    if thread_search:
        return thread_search[0]

def find_threads_from_titles(titles_list):
    threads_list = []
    for title in titles_list:
        if not title: continue
        thread = find_thread(title)
        if thread: threads_list.append(thread)
    return threads_list

def assign_topic_from_file(topic, file):
    titles_list = read_titles_file(file)
    if titles_list:
        print("Finding threads for "+str(len(titles_list))+" news titles.")
        threads_list = find_threads_from_titles(titles_list)
        print("Assigning topic "+topic.name+" to "+str(len(threads_list))+" threads.")
        topic.assign_threads_list(threads_list)
    else:
        threads_list = []
    return threads_list
