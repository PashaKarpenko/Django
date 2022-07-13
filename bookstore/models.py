from django.contrib.auth import get_user_model
from django.db import models


class Books(models.Model):
    author_id = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    released_year = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title},  {self.released_year}'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Authors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Review(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    description = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
