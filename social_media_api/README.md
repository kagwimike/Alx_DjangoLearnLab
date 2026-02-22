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