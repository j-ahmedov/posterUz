from rest_framework import serializers
from .models import Post


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

