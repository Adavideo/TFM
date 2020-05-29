from django import forms
from .input_output_files import get_datasets_names

def get_dataset_options():
    datasets_names = get_datasets_names()
    if datasets_names:
        options = []
        for name in datasets_names:
            options.append((name, name))
    else:
        options = [("","")]
    return options


class ImportCSVForm(forms.Form):
    file = forms.FileField()

class ClusterForm(forms.Form):
    dataset_name = forms.ChoiceField(choices=get_dataset_options())

class GenerateDatasetForm(forms.Form):
    dataset_name = forms.CharField(max_length=25)
    description = forms.CharField(max_length=None)
