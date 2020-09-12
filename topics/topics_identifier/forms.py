from django import forms
from .views_util import get_documents_options, get_topics_options


class ModelsForm(forms.Form):
    model_name = forms.CharField(max_length=25)
    document_types = forms.ChoiceField(choices=get_documents_options(), required=False)
    max_num_documents = forms.IntegerField(required=False, label="Max number of documents")
    max_level = forms.IntegerField(required=False, label="Max tree level")

class TreeForm(forms.Form):
    tree_name = forms.CharField(max_length=25)
    model_name = forms.CharField(max_length=25)
    document_types = forms.ChoiceField(choices=get_documents_options(), required=False)

class ClusterSeachForm(forms.Form):
    search_terms = forms.CharField(max_length=100)

class AssignTopicFromFileForm(forms.Form):
    topic_name = forms.CharField(max_length=100)

class ClusterTopicForm(forms.Form):
    topic = forms.ChoiceField(choices=get_topics_options(), required=False)
    model_name = forms.CharField(max_length=25)
