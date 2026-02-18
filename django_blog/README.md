Authentication System Overview

This project implements Django’s built-in authentication system including:

User registration

Login

Logout

Profile editing

Registration

Users register using a custom form extending UserCreationForm. Email field is included.

Login & Logout

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