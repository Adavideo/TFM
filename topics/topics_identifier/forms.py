from django import forms
from .models import Topic

def get_documents_options():
    document_types = ["news", "comments", "both"]
    options = []
    for type in document_types:
        options.append((type, type))
    return options

def get_topics_options():
    try:
        topics_list = Topic.objects.all()
        len(topics_list)
    except:
        topics_list = None

    if not topics_list:
        options = [("","")]
    else:
        options = []
        for topic in topics_list:
            options.append((topic.id, topic))
    return options


class TreeForm(forms.Form):
    tree_name = forms.CharField(max_length=25)
    document_types = forms.ChoiceField(choices=get_documents_options())

class ClusterSeachForm(forms.Form):
    search_terms = forms.CharField(max_length=100)

class AssignTopicFromFileForm(forms.Form):
    topic_name = forms.CharField(max_length=100)

class ClusterTopicForm(forms.Form):
    topic = forms.ChoiceField(choices=get_topics_options())
