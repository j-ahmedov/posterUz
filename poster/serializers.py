from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Post, User, Like, Comment, Follow


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
        fields = ('id', 'name', 'surname', 'username', 'avatar', 'followers_count', 'followings_count')

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


# Serializer to return User data in comments and posts
class UserInShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'avatar')


# -----------------------Comment Serializers-----------------------------------------------------------


class CommentSerializer(serializers.ModelSerializer):
    user = UserInShortSerializer()

    class Meta:
        model = Comment
        fields = "__all__"


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

