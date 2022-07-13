# Generated by Django 4.0.5 on 2022-07-12 05:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0008_review_alter_authors_options_alter_books_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='book_id',
            field=models.IntegerField(),
        ),
    ]