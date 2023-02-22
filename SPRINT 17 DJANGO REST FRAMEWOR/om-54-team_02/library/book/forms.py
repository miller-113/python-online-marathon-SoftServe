from django import forms
from .models import Book


class BookFormModel(forms.ModelForm):
    """Send the data to model Book"""
    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'publication_year', 'id']


class UpdateBookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['date_of_issue']