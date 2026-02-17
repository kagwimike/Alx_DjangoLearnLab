from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

# FBV imports
from .views import list_books
from .views import add_book
from .views import edit_book
from .views import delete_book
from .views import register

# CBV imports
from .views import LibraryDetailView

# Role-based views
from .views import admin_view
from .views import librarian_view
from .views import member_view

urlpatterns = [
    # Function-Based View
    path('books/', list_books, name='list_books'),

    # Book Management
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),

    # Class-Based View
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based views
    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),
]
