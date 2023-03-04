from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Post, User, Like, Comment, Follow
from django.core.serializers import serialize
import json


# -----------------------User Serializers-----------------------------------------------------------

# Main User serializer that represents all data except password
class UserSerializer(serializers.ModelSerializer):

    followers_count = serializers.SerializerMethodField(read_only=True)
    followings_count = serializers.SerializerMethodField(read_only=True)

    def get_followers_count(self, user):
        return Follow.objects.filter(following_user=user.id).count()

    def get_followings_count(self, user):
        return Follow.objects.filter(user=user).count()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'avatar', 'followers_count', 'followings_count')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            avatar=validated_data['avatar'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_representation(self, obj):
        rep = super(UserCreateSerializer, self).to_representation(obj)
        rep.pop('password', None)
        rep.pop('groups', None)
        rep.pop('user_permissions', None)
        rep.pop('last_login', None)
        return rep


# Serializer to return User data in comments and posts
class UserInShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'avatar')


class PostForDataSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField(read_only=True)

    def get_comments_count(self, post):
        return post.comments.count()

    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, obj):
        rep = super(PostForDataSerializer, self).to_representation(obj)
        rep.pop('user', None)
        return rep


class UserPostsSerializer(serializers.ModelSerializer):

    posts = PostForDataSerializer(many=True)

    class Meta:
        model = User
        fields = ('posts',)


# -----------------------Comment Serializers-----------------------------------------------------------


class CommentSerializer(serializers.ModelSerializer):
    user = UserInShortSerializer()

    class Meta:
        model = Comment
        fields = "__all__"


class CommentForDataSerializer(serializers.ModelSerializer):

    user = UserInShortSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'user', 'commented_at')


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = "__all__"


# ------------------------Post Serializers------------------------------------------------------------

class PostSerializer(serializers.ModelSerializer):
    user = UserInShortSerializer()

    comments_count = serializers.SerializerMethodField(read_only=True)

    def get_comments_count(self, post):
        return post.comments.count()

    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"


class PostCommentSerializer(serializers.ModelSerializer):

    comments = CommentForDataSerializer(many=True)

    class Meta:
        model = Post
        fields = ('comments',)


# -----------------------Like Serializers-----------------------------------------------------------

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Like
        fields = "__all__"


class LikeCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = "__all__"


# -----------------------Follow Serializers-----------------------------------------------------------

class FollowSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Follow
        fields = "__all__"


class FollowCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, data):
        try:
            User.objects.get(pk=data['following_user'])
        except User.DoesNotExist:
            raise ValidationError("User to follow doesn't exist")

        try:
            follow = Follow.objects.filter(user=data['user'].id, following_user=data['following_user'])
            if follow.exists():
                raise ValidationError("User is already following")
        except Follow.DoesNotExist:
            pass

        if data['user'].id == data['following_user']:
            raise ValidationError("User cannot follow himself/herself")

        return data

    class Meta:
        model = Follow
        fields = "__all__"
