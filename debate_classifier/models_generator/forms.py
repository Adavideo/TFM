from django import forms
from config import default_documents_limit
from common.forms_util import get_documents_options
from .forms_util import get_tree_levels


class ModelsForm(forms.Form):
    model_name = forms.CharField(max_length=25)
    document_types = forms.ChoiceField(choices=get_documents_options())
    max_level = forms.ChoiceField(label="Max tree level", choices=get_tree_levels())
    max_num_documents = forms.IntegerField( initial= default_documents_limit,
                                            label= "Max number of documents",
                                            help_text= "Number of documents used to generate the model")
