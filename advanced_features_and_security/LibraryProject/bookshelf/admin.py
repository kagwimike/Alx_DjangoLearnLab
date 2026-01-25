from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    search_fields = ('title', 'author')                     # Add search box
    list_filter = ('publication_year',)                     # Add filter by year
