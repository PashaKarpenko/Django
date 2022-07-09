from django.db import models


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


class Books(models.Model):
    author_id = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    released_year = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    @staticmethod
    def create_book():
        for book in books:
            book = Books(title=book['title'], description=book['description'], released_year=book['released_year'], author_id=book['author_id'])
            book.save()


class Authors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def create_author():
        for author in authors:
            author = Authors(first_name=author['first_name'], last_name=author['last_name'], age=author['age'])
            author.save()
