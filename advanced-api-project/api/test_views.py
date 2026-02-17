from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints.
    Tests CRUD operations, filtering, searching, ordering,
    and authentication/permission enforcement.
    """

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Create author
        self.author = Author.objects.create(name="J.K. Rowling")

        # Create book
        self.book = Book.objects.create(
            title="Harry Potter",
            publication_year=1997,
            author=self.author
        )

        # URLs
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book.id])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book.id])
        self.delete_url = reverse("book-delete", args=[self.book.id])

    # ---------------------------
    # CRUD TESTS
    # ---------------------------

    def test_get_books_list(self):
        """Test retrieving book list (unauthenticated allowed)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book_authenticated(self):
        """Test creating book with authentication."""
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """Test creating book without authentication fails."""
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2023,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_update_book(self):
        """Test updating a book."""
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Updated Title",
            "publication_year": 1998,
            "author": self.author.id
        }

        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        """Test deleting a book."""
        self.client.login(username="testuser", password="testpassword")

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # ---------------------------
    # FILTERING TESTS
    # ---------------------------

    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        response = self.client.get(self.list_url + "?title=Harry Potter")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_publication_year(self):
        """Test filtering books by publication year."""
        response = self.client.get(self.list_url + "?publication_year=1997")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # ---------------------------
    # SEARCH TESTS
    # ---------------------------

    def test_search_books(self):
        """Test searching books by title."""
        response = self.client.get(self.list_url + "?search=Harry")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # ---------------------------
    # ORDERING TESTS
    # ---------------------------

    def test_order_books(self):
        """Test ordering books by publication_year."""
        Book.objects.create(
            title="Another Book",
            publication_year=2005,
            author=self.author
        )

        response = self.client.get(self.list_url + "?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
