# Social Media API

## Setup Instructions

1. Clone Repo
2. Create Virtual Environment
3. Install Requirements
pip install django djangorestframework

4. Run Migrations
python manage.py makemigrations
python manage.py migrate

5. Run Server
python manage.py runserver

## API Endpoints

Register:
POST /api/accounts/register/

Login:
POST /api/accounts/login/

Profile:
GET /api/accounts/profile/

Use Token Authentication
Authorization: Token your_token_here

## Custom User Model Fields

- username
- email
- bio
- profile_picture
- followers


## Posts Endpoints

GET /api/posts/
POST /api/posts/
PUT /api/posts/{id}/
DELETE /api/posts/{id}/

Search Posts:
/api/posts/?search=keyword

## Comments Endpoints

GET /api/comments/
POST /api/comments/
PUT /api/comments/{id}/
DELETE /api/comments/{id}/


## Follow System

Follow User:
POST /api/accounts/follow/{user_id}/

Unfollow User:
POST /api/accounts/unfollow/{user_id}/

## Feed

GET /api/feed/

Returns posts from followed users ordered by latest