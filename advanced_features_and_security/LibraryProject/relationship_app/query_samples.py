import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)

    print("Books by", author_name)
    for book in books:
        print("-", book.title)


def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()

    print("Books in", library_name)
    for book in books:
        print("-", book.title)


def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)

    print("Librarian of", library_name, ":", librarian.name)
