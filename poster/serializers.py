from rest_framework import serializers
from .models import Post, User, Like, Comment, Follow


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def to_representation(self, obj):
        rep = super(UserSerializer, self).to_representation(obj)
        rep.pop('password', None)
        return rep


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        models = Like
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Comment
        fields = "__all__"


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        models = Follow
        fields = "__all__"
