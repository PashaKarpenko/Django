from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Books, Authors
from .forms import CreateBookForm

def list_books(request):
    books = Books.objects.all()
    if request.method == 'GET' and 'Search' in request.GET:
        search = request.GET['Search']
        books = books.filter(title=search)
    context = {'books': books}
    return render(request, 'bookstore/all_books.html', context=context)


def book_detail(request, index):
    book = get_object_or_404(Books, id=index)
    author_id = book.author_id
    author = get_object_or_404(Authors, id=author_id)
    context = {'book': book, 'author': author}
    print(book)
    return render(request, 'bookstore/book_detail.html', context=context)



def author_details(request, index):
    author = get_object_or_404(Authors, id=index)
    author_id = author.id
    context = {'author': author, 'author_id': author_id}
    return render(request, 'bookstore/author.html', context=context)


def books_of_author(request, index):
    books_author = get_list_or_404(Books, author_id=index)
    author = get_object_or_404(Authors, id=index)
    context = {'books_author': books_author, 'author': author}
    return render(request, 'bookstore/books_of_author.html', context=context)


def books_create(request):
    books = Books.objects.all()
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/books/')
    context = {'books': books, 'create_books_form': CreateBookForm}
    return render(request, 'bookstore/books_create.html', context=context)


