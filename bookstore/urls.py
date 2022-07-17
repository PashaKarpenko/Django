from django.urls import path
from .views import author_details, books_of_author, books_create, list_books, BookDetailView

urlpatterns = [
    path('', list_books, name="all_books"),
    path('books/<int:pk>/', BookDetailView.as_view(), name="book_detail"),
    path('authors/<int:index>/', author_details, name="author_details"),
    path('books/author/<int:index>/', books_of_author, name='books_of_author'),
    path('books/create/', books_create, name='books_create')
]
