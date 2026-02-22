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

📄 Likes & Notifications API Documentation
🔐 Authentication Required

All endpoints below require authentication using Token Authentication.

Add this header in Postman:

Authorization: Token <your_token>
👍 LIKE SYSTEM
1️⃣ Like a Post
➤ Endpoint
POST /api/posts/<post_id>/like/
➤ Description

Allows an authenticated user to like a post.

A user cannot like the same post more than once

Generates a notification to the post author

➤ Example Request
POST http://127.0.0.1:8000/api/posts/1/like/
➤ Headers
Authorization: Token 123abc456token
➤ Success Response
{
  "message": "Post liked successfully"
}
➤ Error Response (Already Liked)
{
  "error": "You already liked this post"
}
2️⃣ Unlike a Post
➤ Endpoint
POST /api/posts/<post_id>/unlike/
➤ Description

Allows an authenticated user to remove their like from a post.

➤ Example Request
POST http://127.0.0.1:8000/api/posts/1/unlike/
➤ Success Response
{
  "message": "Post unliked successfully"
}
➤ Error Response (Like not found)
{
  "error": "You haven't liked this post"
}

🔔 NOTIFICATION SYSTEM

3️⃣ Get User Notifications
➤ Endpoint
GET /api/notifications/
➤ Description

Returns all notifications for the currently authenticated user.

Notifications are generated when:

Someone likes your post ❤️

Someone comments on your post 💬

Someone follows you 👥

Unread notifications appear first.

➤ Example Request
GET http://127.0.0.1:8000/api/notifications/
➤ Headers
Authorization: Token 123abc456token
➤ Example Response
[
  {
    "id": 1,
    "recipient": 2,
    "actor": 3,
    "verb": "liked your post",
    "timestamp": "2026-02-22T10:45:12Z",
    "is_read": false
  },
  {
    "id": 2,
    "recipient": 2,
    "actor": 4,
    "verb": "commented on your post",
    "timestamp": "2026-02-22T09:15:33Z",
    "is_read": true
  }
]

4️⃣ Mark Notification as Read

➤ Endpoint
PATCH /api/notifications/<notification_id>/read/
➤ Description

Marks a notification as read after the user views it.

➤ Example Request
PATCH http://127.0.0.1:8000/api/notifications/1/read/
➤ Success Response
{
  "message": "Notification marked as read"
}