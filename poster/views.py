from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Post, User, Like, Comment, Follow
from .serializers import PostSerializer, UserSerializer, LikeSerializer, CommentSerializer, FollowSerializer
from django.db.models import ProtectedError


#  --------------------UserAPIView----------------------------------------------
class UserCreateAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ------------------------PostAPIView--------------------------------------------
class PostCreateAPI(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# ------------------------LikeAPIView--------------------------------------------
class LikeCreateAPI(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeListAPI(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


# ------------------------CommentAPIView--------------------------------------------
class CommentCreateAPI(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListAPI(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# ------------------------FollowAPIView--------------------------------------------
class FollowCreateAPI(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class FollowListAPI(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class FollowDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
