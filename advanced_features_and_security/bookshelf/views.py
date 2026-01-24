from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookSearchForm


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Secure view to display a list of books.

    Security measures implemented:
    - Permission-based access control using @permission_required
    - Safe querying using Django ORM (prevents SQL injection)
    - User input validation using Django Forms
    """

    # Initialize form with GET data for safe input handling
    form = BookSearchForm(request.GET or None)

    # Base queryset using Django ORM (safe by default)
    books = Book.objects.all()

    # Validate and sanitize user input before filtering
    if form.is_valid():
        title = form.cleaned_data.get('title')
        if title:
            # ORM filtering automatically parameterizes queries
            books = books.filter(title__icontains=title)

    return render(request, 'bookshelf/book_list.html', {
        'books': books,
        'form': form
    })
