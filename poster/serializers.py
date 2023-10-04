from django.core.exceptions import FieldError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Post, User, Like, Comment, Follow


# -----------------------User Serializers-----------------------------------------------------------

# Main User serializer that represents all data except password
class UserSerializer(serializers.ModelSerializer):

    followers_count = serializers.SerializerMethodField(read_only=True)
    followings_count = serializers.SerializerMethodField(read_only=True)

    def get_followers_count(self, user):
        try:
            followers_count = Follow.objects.filter(following_user=user.id).count()
        except FieldError:
            return 0
        return followers_count

    def get_followings_count(self, user):
        try:
            followings_count = Follow.objects.filter(user=user).count()
        except FieldError:
            return 0
        return followings_count

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'avatar', 'followers_count', 'followings_count')


# User Create serializer
class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

        extra_kwargs = {
            'avatar': {'required': False}
        }

    def create(self, validated_data):
        avatar = ''
        try:
            avatar = validated_data['avatar']
        except Exception as e:
            print(e)

        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            avatar=avatar,
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


# Serializer to return Post data for user and comment data in API
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


# Serializer to represent posts of user
class UserPostsSerializer(serializers.ModelSerializer):

    posts = PostForDataSerializer(many=True)

    class Meta:
        model = User
        fields = ('posts',)


# -----------------------Comment Serializers-----------------------------------------------------------

# Comment serializer
class CommentSerializer(serializers.ModelSerializer):
    user = UserInShortSerializer()

    class Meta:
        model = Comment
        fields = "__all__"


# Comment serializer to represent comment data in API
class CommentForDataSerializer(serializers.ModelSerializer):

    user = UserInShortSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'user', 'commented_at')


# Comment serializer to create comment
class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = "__all__"


# ------------------------Post Serializers------------------------------------------------------------

# Post serializer to represent in API
class PostSerializer(serializers.ModelSerializer):
    user = UserInShortSerializer()

    comments_count = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    user_liked = serializers.SerializerMethodField(read_only=True)

    def get_comments_count(self, post):
        return post.comments.count()

    def get_likes_count(selfs, post):
        return post.likes.count()

    def get_user_liked(self, post):

        user = self.context.get('request').user if 'request' in self.context else None

        if user and user.is_authenticated:
            return post.likes.filter(user=user).exists()

        return False

    class Meta:
        model = Post
        fields = "__all__"


# Post Create serializer to create post
class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"


# Serializer to return comments of post
class PostCommentSerializer(serializers.ModelSerializer):

    comments = CommentForDataSerializer(many=True)

    class Meta:
        model = Post
        fields = ('comments',)


# -----------------------Like Serializers-----------------------------------------------------------

# Like serializer to return like data in API
class LikeSerializer(serializers.ModelSerializer):
    user = UserInShortSerializer()
    post = PostForDataSerializer()

    class Meta:
        model = Like
        fields = "__all__"


# Serializer to create like
class LikeCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, data):
        try:
            like = Like.objects.filter(user=data['user'].id, post=data['post'])
            if like.exists():
                raise ValidationError('This post is already liked')
        except Like.DoesNotExist:
            pass

        return data

    class Meta:
        model = Like
        fields = "__all__"


# Serializer to represent like data for post
class LikeForPostSerializer(serializers.ModelSerializer):
    user = UserInShortSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'user')


# Serializer to represent like data for user
class LikeForUserSerializer(serializers.ModelSerializer):
    post = PostForDataSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'post')


# Serializer to represent likes of post
class PostLikeSerializer(serializers.ModelSerializer):

    likes = LikeForPostSerializer(many=True)

    class Meta:
        model = Post
        fields = ('likes',)


# Serializer to represent likes of user
class UserLikeSerializer(serializers.ModelSerializer):

    likes = LikeForUserSerializer(many=True)

    class Meta:
        model = Post
        fields = ('likes',)


# -----------------------Follow Serializers-----------------------------------------------------------

# Follow serializer to represent all data of follow object
class FollowSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Follow
        fields = "__all__"


# Serializer to create follow object
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
