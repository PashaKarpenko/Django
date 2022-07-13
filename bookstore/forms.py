from django import forms
from .models import Books, Review


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'released_year', 'author_id']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['description']
