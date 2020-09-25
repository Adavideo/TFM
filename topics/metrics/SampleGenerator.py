from random import randint, shuffle
import io
from topics_identifier.models import ClusterTopic
from timeline.models import Document
from config import sample_size


def get_random_index(num_documents):
    i = randint(0, num_documents-1)
    return i

def select_random_document(documents):
    num_documents = len(documents)
    i = get_random_index(num_documents)
    selected = documents[i]
    return selected


class SampleGenerator:

    def __init__(self, topic, filename):
        self.filename = filename + "_"+ topic.name + ".txt"
        self.clusters = [ i.cluster for i in ClusterTopic.objects.filter(topic=topic) ]
        self.clusters_documents = self.get_clusters_documents()
        self.num_total_documents = len(Document.objects.filter(is_news=True))

    def get_clusters_documents(self):
        documents = []
        for cluster in self.clusters:
            documents.extend( cluster.documents() )
        return documents

    def select_document(self, from_clusters):
        if from_clusters:
            doc = select_random_document(self.clusters_documents)
        else:
            i = get_random_index(self.num_total_documents)
            doc = Document.objects.filter(is_news=True)[i]
        return doc

    def generate_partial_sample(self, from_clusters):
        sample = []
        while len(sample) < sample_size/2:
            doc = self.select_document(from_clusters)
            if doc not in sample:
                sample.append(doc.content)
        return sample

    def generate_sample(self):
        clusters_sample = self.generate_partial_sample(from_clusters=True)
        rest_sample = self.generate_partial_sample(from_clusters=False)
        sample = []
        sample.extend(clusters_sample)
        sample.extend(rest_sample)
        shuffle(sample)
        self.store_sample(sample)
        return sample

    def store_sample(self, sample):
        out_file = open(self.filename, 'a')
        for doc in sample:
            out_file.write(doc+"\n\n")
        out_file.close()
