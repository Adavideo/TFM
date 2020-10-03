from django import forms
from common.forms import get_documents_options, get_topics_options
from .forms_util import *


class TreeForm(forms.Form):
    tree_name = forms.CharField(max_length=25)
    model_name = forms.ChoiceField(choices=get_models_options())
    document_types = forms.ChoiceField(choices=get_documents_options(), required=False)

class ClusterSeachForm(forms.Form):
    search_terms = forms.CharField(max_length=100)

class AssignTopicToClustersForm(forms.Form):

    def __init__(self, *args, **kwargs):
        search_results = kwargs.pop("search_results", [])
        super(AssignTopicToClustersForm, self).__init__(*args, **kwargs)
        self.fields['topic'] = forms.ChoiceField(choices=get_topics_options(), required=False)
        self.fields['selected_clusters'] = forms.MultipleChoiceField(
                                    label="Select clusters",
                                    choices=get_search_clusters(search_results),
                                    widget=forms.CheckboxSelectMultiple,
                                    required=False)

class AssignTopicToDocumentsForm(forms.Form):

    def __init__(self, *args, **kwargs):
        documents = kwargs.pop("documents", [])
        super(AssignTopicToDocumentsForm, self).__init__(*args, **kwargs)
        self.fields['documents'] = forms.MultipleChoiceField(
                                    label="Documents",
                                    choices=documents,
                                    widget=forms.CheckboxSelectMultiple,
                                    required=False)

class AssignTopicFromFileForm(forms.Form):
    topic = forms.ChoiceField(choices=get_topics_options())
