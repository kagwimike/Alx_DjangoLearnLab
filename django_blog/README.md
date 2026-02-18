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