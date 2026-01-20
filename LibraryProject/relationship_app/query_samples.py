# relationship_app/query_samples.py
# This script demonstrates queries for advanced model relationships in Django

from relationship_app.models import Author, Book, Library, Librarian

# -----------------------------
# Create sample data
# -----------------------------
# Clear existing objects (use only for testing, safe in a dev DB)
Author.objects.all().delete()
Book.objects.all().delete()
Library.objects.all().delete()
Librarian.objects.all().delete()

# Create Authors
author1 = Author.objects.create(name="George Orwell")
author2 = Author.objects.create(name="J.K. Rowling")

# Create Books
book1 = Book.objects.create(title="1984", author=author1)
book2 = Book.objects.create(title="Animal Farm", author=author1)
book3 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author2)

# Create Libraries
library1 = Library.objects.create(name="Central Library")
library2 = Library.objects.create(name="City Library")

# Add books to libraries (ManyToMany)
library1.books.set([book1, book3])
library2.books.set([book2])

# Create Librarians (OneToOne)
librarian1 = Librarian.objects.create(name="Alice", library=library1)
librarian2 = Librarian.objects.create(name="Bob", library=library2)

# -----------------------------
# Sample Queries
# -----------------------------

# 1️⃣ Query all books by George Orwell
print("Books by George Orwell:")
books_orwell = Author.objects.get(name="George Orwell").books.all()
for book in books_orwell:
    print(f"- {book.title}")
# Expected Output:
# - 1984
# - Animal Farm

# 2️⃣ List all books in Central Library
print("\nBooks in Central Library:")
books_central = Library.objects.get(name="Central Library").books.all()
for book in books_central:
    print(f"- {book.title}")
# Expected Output:
# - 1984
# - Harry Potter and the Sorcerer's Stone

# 3️⃣ Retrieve the librarian for City Library
print("\nLibrarian of City Library:")
librarian = Library.objects.get(name="City Library").librarian
print(f"- {librarian.name}")
# Expected Output:
# - Bob
quit