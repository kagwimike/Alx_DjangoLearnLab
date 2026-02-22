from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from notifications.serializers import NotificationSerializer

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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def notifications_list(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)