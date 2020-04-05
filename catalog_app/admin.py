from django.contrib import admin

# Register your models here.

from .models import Book, Magazine, Author, Collection

admin.site.register(Book)
admin.site.register(Magazine)
admin.site.register(Author)
admin.site.register(Collection)