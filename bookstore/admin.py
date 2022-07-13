from django.contrib import admin
from .models import Books, Authors


admin.site.register(Authors)


class BooksAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Books._meta.fields]
    search_fields = [field.name for field in Books._meta.fields]
    list_filter = ['author_id']
    list_editable = ('description',)

    class Meta:
        model = Books

admin.site.register(Books, BooksAdmin)


