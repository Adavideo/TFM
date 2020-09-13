from django import forms
from .views_util import get_documents_options, get_topics_options, get_tree_levels
from .config import default_document_limit


class ModelsForm(forms.Form):
    model_name = forms.CharField(max_length=25)
    document_types = forms.ChoiceField(choices=get_documents_options())
    max_level = forms.ChoiceField(label="Max tree level", choices=get_tree_levels())
    max_num_documents = forms.IntegerField( initial= default_document_limit,
                                            label= "Max number of documents",
                                            help_text= "Number of documents used to generate the model")

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
