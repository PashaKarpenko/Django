from django.shortcuts import render
from django.http import HttpResponseNotFound

books = [
    {
        "id": 1,
        "author_id": 1,
        "title": "Fluent Python",
        "released_year": 2015,
        "description": "Python’s simplicity lets you become productive quickly, but this often means you aren’t using everything it has to offer. With this hands-on guide, you’ll learn how to write effective, idiomatic Python code by leveraging its best—and possibly most neglected—features. Author Luciano Ramalho takes you through Python’s core language features and libraries, and shows you how to make your code shorter, faster, and more readable at the same time."
    },
    {
        "id": 2,
        "author_id": 2,
        "title": "Інтернат",
        "released_year": 2021,
        "description": "Одного разу, прокинувшись, ти бачиш за вікном вогонь. Ти його не розпалював. Але гасити його доведеться й тобі Січень 2015 року. Донбас. Паша, вчитель однієї зі шкіл, спостерігає, як лінія фронту неухильно наближається до його дому. Стається так, що він змушений цю лінію перетнути. Щоби потім повернутись назад. І для цього йому щонайменше потрібно визначитись, на чиєму боці його дім"
    },
    {
        "id": 3,
        "author_id": 3,
        "title": "From 'Letters to Ukraine'",
        "released_year": 2020,
        "description": "Переклад окремих творів зі збірки Листи в Україну, виконаний Ніною Шевчук-Мюррей."
    },
    {
        "id": 4,
        "author_id": 4,
        "title": "Акорди (збірка)",
        "released_year": 1914,
        "description": "Книгу було видано 1914 року в Києві у видавництві «Життя й мистецтво». Примірник із колекції Джона Лучківа."

    },
    {
        "id": 5,
        "author_id": 2,
        "title": "Життя Марії",
        "released_year": 2015,
        "description": "Найлегше заняття в часи війни — ненавидіти чужих. Найважче — досягати порозуміння. Навіть зі своїми. Але треба намагатися, інакше війна ніколи не закінчиться. А щоб порозумітися, необхідно розмовляти. З ким завгодно, як завгодно і про що завгодно. Головне — не втрачаючи людяності, тобто любові й уваги. У поетичній збірці «Життя Марії» Сергій Жадан розмовляє — про найдорожчі листи і спалені мости, втрачені місця і зруйновані міста. Розмовляє римованими віршами й верлібрами, власними і перекладеними словами. Розмовляє зі своїми й чужими, зі святими й не дуже, з убитими військовими і живими біженцями, з Рільке, Мілошем і, звісно, з нами. Щоб врятувати — якщо не нас, то хоча би наших дітей."
    }
]

authors = [
    {
        'id': 1,
        'first_name': 'Luciano',
        'last_name': 'Ramalho',
        'age': 51
    },
    {
        'id': 2,
        'first_name': 'Жадан',
        'last_name': 'Сергій',
        'age': 42
    },
    {
        'id': 3,
        'first_name': 'Юрій',
        'last_name': 'Андрухович',
        'age': 42
    },
    {
        'id': 4,
        'first_name': 'Джон',
        'last_name': 'Луквіч',
        'age': 56
    }
]


def list_books(request):
    return render(request, 'bookstore/all_books.html', context={'books': books})


def book_detail(request, index):
    try:
        book = books[index - 1]
        author_id = book['author_id']
        author = authors[author_id - 1]
        return render(request, 'bookstore/book_detail.html', context={'book': book, 'author': author})
    except IndexError:
        return HttpResponseNotFound(f"Сторінка з {index = } не знайдена")


def author_details(request, index):
    try:
        author = authors[index - 1]
        author_id = authors[index - 1]['id']
        return render(request, 'bookstore/author.html', context={'author': author, 'author_id': author_id})
    except IndexError:
        return HttpResponseNotFound(f"Сторінка з {index = } не знайдена")


def books_of_author(request, index):
    try:
        books_author = [book for book in books if book['author_id'] == index]
        author = authors[index - 1]
        return render(request, 'bookstore/books_of_author.html', context={'books_author': books_author, 'author': author})
    except:
        return HttpResponseNotFound(f"Сторінка з {index = } не знайдена")
