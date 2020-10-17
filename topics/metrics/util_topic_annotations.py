

# Get a list of all the threads ids
def get_threads_ids(annotations_list):
    threads_ids = []
    for annotation in annotations_list:
        id = annotation.thread.id
        if id not in threads_ids: threads_ids.append(id)
    return threads_ids
