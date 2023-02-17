from rest_framework import serializers
from .models import Post, User


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    surname = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    avatar = serializers.ImageField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.surname = validated_data.get("surname", instance.surname)
        instance.username = validated_data.get("username", instance.username)
        instance.password = validated_data.get("password", instance.password)
        instance.avatar = validated_data.get("avatar", instance.avatar)
        instance.save()
        return instance

    class Meta:
        model = User

    def to_representation(self, obj):
        rep = super(UserSerializer, self).to_representation(obj)
        rep.pop('password', None)
        return rep


class PostSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    title = serializers.CharField(max_length=50)
    content = serializers.CharField()
    post_image = serializers.ImageField()
    published_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get("user_id", instance.user_id)
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.post_image = validated_data.get("post_image", instance.post_image)
        instance.save()
        return instance

    class Meta:
        model = Post
        fields = ('user_id', 'title', 'content', 'post_image', 'published_at')
