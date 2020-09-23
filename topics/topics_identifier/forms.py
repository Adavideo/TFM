from django import forms
from .forms_util import *
from .config import default_documents_limit


class ModelsForm(forms.Form):
    model_name = forms.CharField(max_length=25)
    document_types = forms.ChoiceField(choices=get_documents_options())
    max_level = forms.ChoiceField(label="Max tree level", choices=get_tree_levels())
    max_num_documents = forms.IntegerField( initial= default_documents_limit,
                                            label= "Max number of documents",
                                            help_text= "Number of documents used to generate the model")

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

class AssignTopicFromFileForm(forms.Form):
    topic_name = forms.CharField(max_length=100)

class ClusterTopicThreadsForm(forms.Form):
    topic = forms.ChoiceField(choices=get_topics_options())
    model_name = forms.ChoiceField(choices=get_models_options())
