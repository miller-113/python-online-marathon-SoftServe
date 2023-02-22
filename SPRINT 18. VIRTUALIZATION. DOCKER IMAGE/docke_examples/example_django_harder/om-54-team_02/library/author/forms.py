from django import forms
from .models import Author


class AuthorFormModel(forms.ModelForm):
    """Send the data to model Author"""
    class Meta:
        model = Author
        fields = ['name', 'patronymic', 'surname']


class UpdateAuthorFormModel(forms.ModelForm):
    """Send the data to model Author"""
    class Meta:
        model = Author
        exclude = ['books']