from rest_framework import serializers
from .models import Post, Comment, Like

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'likes_count']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']        