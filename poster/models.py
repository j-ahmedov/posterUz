from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', blank=True)


    def __str__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey('User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_image = models.ImageField(upload_to='post-images/%Y/%m/%d/')
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    post = models.ForeignKey('Post', related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey('User', related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f"Like of post {self.post.id}"


class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    comment = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment of post {self.post.id}"


class Follow(models.Model):
    following = models.ForeignKey('User', related_name='followings', on_delete=models.CASCADE)
    follower = models.ForeignKey('User', related_name='followers', on_delete=models.CASCADE)

    def __str__(self):
        return f"Follow of {self.following.id} by {self.follower}"
