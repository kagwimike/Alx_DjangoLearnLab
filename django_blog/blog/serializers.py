from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    replies = serializers.SerializerMethodField()
    upvote_count = serializers.IntegerField(source="upvotes.count", read_only=True)
    user_has_upvoted = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "author",
            "content",
            "created_at",
            "updated_at",
            "parent",
            "replies",
            "upvote_count",
            "user_has_upvoted"
        ]

    def get_replies(self, obj):
        # recursively serialize child comments
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True, context=self.context).data
        return []

    def get_user_has_upvoted(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return obj.upvotes.filter(id=request.user.id).exists()
        return False

class PostSerializer(serializers.ModelSerializer):

    # ⭐ THIS IS THE FIX
    comments = CommentSerializer(many=True, read_only=True)

    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "author",
            "published_date",
            "created_at",
            "updated_at",
            "tags",
            "comments"   # ⭐ include comments in response
        ]