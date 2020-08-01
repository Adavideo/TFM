from django import forms

class ImportCSVForm(forms.Form):
    file = forms.FileField()

class TreeForm(forms.Form):
    tree_name = forms.CharField(max_length=25)

class ClusterSeachForm(forms.Form):
    search_terms = forms.CharField(max_length=100)
