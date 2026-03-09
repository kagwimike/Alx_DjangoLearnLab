DevBlog

DevBlog is a full-stack blogging platform where developers can share posts, comment on discussions, and interact through upvotes. The project combines a Django backend API with a React frontend to create a modern web application.

The platform supports post creation, commenting, authentication, and a simple voting system inspired by community platforms.

Features
User Features

User registration and authentication

View all blog posts Full CRUD

Create new blog posts

Edit and delete your own posts

Comment on posts

Edit and delete your own comments

Upvote posts

Upvote comments

View user profile statistics

Developer Features

RESTful API built with Django REST Framework

React frontend consuming the API

Token-based authentication

Modular Django app structure

CRUD operations for posts and comments

Organized URL routing

Tech Stack
Backend

Python

Django

Django REST Framework

Frontend

React

Axios

Database

Tools

Git

GitHub

Postman

Vercel (frontend deployment)

Project Structure
django_blog/
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── templates/
│
├── django_blog/
│   ├── settings.py
│   ├── urls.py
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   └── api.js
│
├── manage.py
└── README.md
Installation
1. Clone the Repository
git clone https://github.com/your-username/devblog.git
cd devblog
2. Create Virtual Environment
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Run Migrations
python manage.py migrate
5. Create Superuser
python manage.py createsuperuser
6. Start the Backend Server
python manage.py runserver

Backend runs at:

http://127.0.0.1:8000
Running the Frontend

Navigate to the React frontend folder:

cd frontend

Install dependencies:

npm install

Run the development server:

npm start

Frontend runs at:

http://localhost:3000
API Endpoints
Posts
Method	Endpoint	Description
GET	/api/posts/	List posts
POST	/api/posts/	Create post
GET	/api/posts/{id}/	Retrieve post
PATCH	/api/posts/{id}/	Update post
DELETE	/api/posts/{id}/	Delete post
POST	/api/posts/{id}/upvote/	Upvote post
Comments
Method	Endpoint	Description
POST	/api/comments/	Create comment
PATCH	/api/comments/{id}/	Update comment
DELETE	/api/comments/{id}/	Delete comment
POST	/api/comments/{id}/upvote/	Upvote comment
Authentication
Method	Endpoint	Description
POST	/api/register/	Register new user
GET	/api/profile/	Get user profile
Screenshots

Add screenshots of:

Homepage

Post details page

Comment section

Profile page

Future Improvements

Pagination for posts

Nested comments (replies)

Rich text editor for posts

Notification system

Bookmarking posts

Tag filtering improvements

Handled using Django’s built-in LoginView and LogoutView.

Profile Management

Authenticated users can update their username and email via a protected view.

Security

CSRF tokens in all forms

Passwords hashed automatically

@login_required decorator used

Django’s secure authentication backend used

Blog Post Management Features
This project implements full CRUD functionality for blog posts using Django Class-Based Views.

Features:
List all posts

View single post

Create new post (authenticated users only)

Edit post (author only)

Delete post (author only)

Permissions:
LoginRequiredMixin restricts creation

UserPassesTestMixin ensures only authors can edit/delete

Public users can view posts

Security:
CSRF protection enabled

Authentication required for sensitive operations

Author ownership enforced in views


Add Comment: post/<int:pk>/comment/ – authenticated users only

Edit Comment: comment/<int:pk>/update/ – only author

Delete Comment: comment/<int:pk>/delete/ – only author

Comments appear in post_detail.html under each post.

Forms use CSRF protection and proper validation.
