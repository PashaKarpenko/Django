from django import forms
from .models import Books, Authors


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'released_year', 'author_id']
