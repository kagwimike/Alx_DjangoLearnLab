from django.urls import path
from . import api_views

urlpatterns = [
    # Posts
    path("posts/", api_views.PostListCreateAPIView.as_view(), name="api-posts"),
    path("posts/<int:pk>/", api_views.PostRetrieveUpdateDestroyAPIView.as_view(), name="api-post-detail"),

    # Comments
    path("comments/", api_views.CommentListCreateAPIView.as_view(), name="api-comments"),
    path("comments/<int:pk>/", api_views.CommentRetrieveUpdateDestroyAPIView.as_view(), name="api-comment-detail"),
]