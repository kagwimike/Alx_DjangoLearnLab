from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# ------------------------
# Template Views (HTML)
# ------------------------
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    PostByTagListView,
)

# ------------------------
# API Views (React Frontend)
# ------------------------
from .views import (
    RegisterAPI,
    PostListAPI,
    PostDetailAPI,
    CommentCreateAPI,
    CommentDetailAPI,
)

urlpatterns = [

    # ====================================
    # Home & Authentication
    # ====================================
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    path(
        "login/",
        auth_views.LoginView.as_view(template_name="blog/login.html"),
        name="login",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="blog/logout.html"),
        name="logout",
    ),

    # ====================================
    # Blog Posts (Template Views)
    # ====================================
    
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # ====================================
    # Comments (Template Views)
    # ====================================
    path(
        "post/<int:pk>/comments/new/",
        CommentCreateView.as_view(),
        name="comment-create",
    ),

    path(
        "comment/<int:pk>/update/",
        CommentUpdateView.as_view(),
        name="comment-update",
    ),

    path(
        "comment/<int:pk>/delete/",
        CommentDeleteView.as_view(),
        name="comment-delete",
    ),

    # ====================================
    # Search
    # ====================================
    path("search/", views.search_posts, name="search-posts"),

    # ====================================
    # Posts by Tag
    # ====================================
    path(
        "tags/<slug:tag_slug>/",
        PostByTagListView.as_view(),
        name="posts-by-tag",
    ),

    # ====================================
    # API ENDPOINTS (React Frontend)
    # ====================================

    # Auth
    path("api/register/", RegisterAPI.as_view(), name="api-register"),
    path("api/profile/", views.user_profile_api, name="api-profile"),

    # Posts API
    path("api/posts/", PostListAPI.as_view(), name="api-posts"),
    path("api/posts/<int:pk>/", PostDetailAPI.as_view(), name="api-post-detail"),
    path("api/posts/<int:pk>/upvote/", views.upvote_post, name="api-post-upvote"),

    # Comments API
    path("api/comments/", CommentCreateAPI.as_view(), name="api-comment-create"),
    path("api/comments/<int:pk>/", CommentDetailAPI.as_view(), name="api-comment-detail"),
    path(
        "api/comments/<int:pk>/upvote/",
        views.comment_upvote,
        name="api-comment-upvote",
    ),
]