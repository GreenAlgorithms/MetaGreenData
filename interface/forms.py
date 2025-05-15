from django import forms


class MetaDataForm(forms.Form):
    meta1 = forms.CharField(label="Meta data 1", max_length=100)
    meta2 = forms.CharField(label="Meta data 2", max_length=100)
    meta3 = forms.CharField(label="Meta data 3", max_length=100)
