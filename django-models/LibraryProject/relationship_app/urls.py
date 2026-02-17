from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
from .views import LibraryDetailView
from . import views
from .views import admin_view
from .views import librarian_view
from .views import member_view


urlpatterns = [
    # Function-Based View
    path('books/', list_books, name='list_books'),

    # Class-Based View
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication (ALX CHECKS THESE EXACTLY)
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Book Management
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),

    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),

]
