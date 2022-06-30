from django.urls import path
from .views import list_books, book_detail, author_details, books_of_author

urlpatterns = [
    path('books/', list_books, name="all_books"),
    path('books/<int:index>/', book_detail, name="book_detail"),
    path('authors/<int:index>/', author_details, name="author_details"),
    path('books/author/<int:index>/', books_of_author, name='books_of_author')
]
