from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ==========================================
# Book List View
# ==========================================
class BookListView(generics.ListAPIView):
    """
    GET: Retrieve all books.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ==========================================
# Book Detail View
# ==========================================
class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve a single book by its ID.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ==========================================
# Book Create View
# ==========================================
class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book.
    Only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom behavior hook.
        Ensures serializer validation runs properly before saving.
        """
        serializer.save()


# ==========================================
# Book Update View
# ==========================================
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update an existing book.
    Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom behavior hook.
        Ensures validation runs before updating.
        """
        serializer.save()


# ==========================================
# Book Delete View
# ==========================================
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book.
    Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
