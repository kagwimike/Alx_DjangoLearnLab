from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Secure view to display a list of books.

    Security measures implemented:
    - Permission-based access control using @permission_required
    - Protection against SQL injection by using Django ORM
    - User input validation and sanitization using Django Forms
    """

    # Initialize ExampleForm with GET data (safe input handling)
    form = ExampleForm(request.GET or None)

    # Base queryset using Django ORM (safe by default)
    books = Book.objects.all()

    # Validate user input before filtering
    if form.is_valid():
        name = form.cleaned_data.get("name")
        if name:
            # ORM filtering prevents SQL injection
            books = books.filter(title__icontains=name)

    return render(
        request,
        "bookshelf/book_list.html",
        {
            "books": books,
            "form": form
        }
    )
