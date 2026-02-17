## API Endpoints

### Book Endpoints

GET /api/books/
- Retrieve all books (Public access)

GET /api/books/<id>/
- Retrieve a single book (Public access)

POST /api/books/create/
- Create a new book (Authenticated users only)

PUT /api/books/<id>/update/
- Update an existing book (Authenticated users only)

DELETE /api/books/<id>/delete/
- Delete a book (Authenticated users only)

Permissions:
- Read operations are public
- Write operations require authentication
