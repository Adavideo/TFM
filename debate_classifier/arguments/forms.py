from django import forms
from common.forms_util import get_topics_options


class TopicsForm(forms.Form):
    tree_name = forms.CharField(max_length=25)
    topic = forms.ChoiceField(choices=get_topics_options())
