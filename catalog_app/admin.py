from django.contrib import admin

# Register your models here.

from .models import Book, Magazine, Author, Collection, BookInstance

admin.site.register(Book)
admin.site.register(Magazine)
admin.site.register(Author)
admin.site.register(Collection)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )