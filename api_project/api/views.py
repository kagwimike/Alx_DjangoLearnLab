from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# NEW: ViewSet for full CRUD

class BookViewSet(viewsets.ModelViewSet):
    """
    Handles all CRUD operations for Book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer