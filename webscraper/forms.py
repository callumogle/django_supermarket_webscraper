from django import forms
#from django.forms import ModelForm


class SearchForm(forms.Form):
    item_to_search = forms.CharField(label="search term", max_length=50)