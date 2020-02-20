from django import forms

from storage.models import Source, Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'source']


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['name', 'url']
