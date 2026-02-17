from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),          # List all books
    path('books/add/', views.add_book, name='add_book'),        # Add a new book
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),  # Edit a book
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),  # Delete a book
]
