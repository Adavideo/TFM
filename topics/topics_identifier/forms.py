from django import forms

def get_documents_options():
    document_types = ["news", "comments", "both"]
    options = []
    for type in document_types:
        options.append((type, type))
    return options


class ImportCSVForm(forms.Form):
    file = forms.FileField()

class TreeForm(forms.Form):
    tree_name = forms.CharField(max_length=25)
    document_types = forms.ChoiceField(choices=get_documents_options())

class ClusterSeachForm(forms.Form):
    search_terms = forms.CharField(max_length=100)
