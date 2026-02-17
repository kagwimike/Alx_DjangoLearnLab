# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing simple ListAPIView route
    path('books/', BookList.as_view(), name='book-list'),

    # Include all routes from the router (CRUD operations)
    path('', include(router.urls)),

    # Endpoint to get auth token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
