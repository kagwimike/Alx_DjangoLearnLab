from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    CustomLoginView,
    CustomLogoutView,
    register,
    add_book,
    edit_book,
    delete_book,
)

urlpatterns = [
    # Function-Based View (FBV)
    path('books/', list_books, name='list_books'),

    # Class-Based View (CBV)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),

    # Book Management
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),
]
