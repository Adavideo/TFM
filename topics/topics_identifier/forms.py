from django import forms

class ImportCSVForm(forms.Form):
    file = forms.FileField()

class ClusterForm(forms.Form):
    dataset_name = forms.CharField(max_length=25)

class ClusterSeachForm(forms.Form):
    search_terms = forms.CharField(max_length=100)
