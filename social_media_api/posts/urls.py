from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import PostViewSet, CommentViewSet, like_post, unlike_post, user_feed


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', user_feed),
    path('posts/<int:pk>/like/', like_post, name='like-post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike-post')
]