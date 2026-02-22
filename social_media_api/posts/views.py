from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class PostPagination(PageNumberPagination):
    page_size = 5


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [SearchFilter]
    search_fields = ['title','content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# ---------------- FEED VIEW ---------------- #
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    """
    Returns posts from users the current user is following,
    ordered by newest first.
    """
    # Get all users the current user is following
    following_users = request.user.following.all()

    # Query posts authored by followed users, newest first
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

    # Serialize and return
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)