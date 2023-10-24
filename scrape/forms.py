from django import forms
from .models import Page

class TitleForm(forms.ModelForm):
    link = forms.CharField(label='', widget=forms.URLInput(attrs={'placeholder': 'Add new page'}))
    class Meta:
        model = Page
        fields = ['link']