from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from notifications.models import Notification
from notifications.serializers import NotificationSerializer

class PostPagination(PageNumberPagination):
    page_size = 5


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# ---------------- FEED VIEW ---------------- #
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_feed(request):
    """
    Returns posts from users the current user is following,
    ordered by newest first.
    """
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(post=post, user=request.user)

    if created:
        # Create notification for post author if someone likes their post
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
        return Response({'message': 'Post liked successfully'})
    return Response({'message': 'You already liked this post'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    deleted, _ = Like.objects.filter(post=post, user=request.user).delete()
    if deleted:
        return Response({'message': 'Post unliked successfully'})
    return Response({'message': 'You have not liked this post'})