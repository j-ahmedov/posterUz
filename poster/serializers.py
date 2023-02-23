from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post, User, Like, Comment, Follow


# -----------------------User Serializers-----------------------------------------------------------

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'username', 'password', 'avatar')

    def create(self, validated_data):
        user = User(
            name=validated_data['name'],
            surname=validated_data['surname'],
            username=validated_data['username'],
            avatar=validated_data['avatar'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_representation(self, obj):
        rep = super(UserSerializer, self).to_representation(obj)
        rep.pop('password', None)
        return rep


# ------------------------Post Serializers------------------------------------------------------------

class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"


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


# -----------------------Comment Serializers-----------------------------------------------------------

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = "__all__"


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
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

