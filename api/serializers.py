from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "body",
            "is_published",
            "author",
            "created_at",
            "updated_at",
        ]


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "user",
            "name",
            "email",
            "body",
            "is_active",
            "created_at",
            "updated_at",
        ]

