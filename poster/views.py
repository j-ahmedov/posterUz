from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly, ObjectIsOwnerOrReadOnly


#  --------------------UserAPIView----------------------------------------------
class UserCreateAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserListAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class UserPostsAPI(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserPostsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class UserLikeListAPI(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserLikeSerializer
    permission_classes = (ObjectIsOwnerOrReadOnly,)


# ------------------------PostAPIView--------------------------------------------
class PostCreateAPI(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PostListAPI(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-published_at')
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)


class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (ObjectIsOwnerOrReadOnly,)


class PostCommentsListAPI(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    permission_classes = (ObjectIsOwnerOrReadOnly,)


class PostLikeListAPI(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = (ObjectIsOwnerOrReadOnly,)


# ------------------------LikeAPIView--------------------------------------------
class LikeCreateAPI(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeCreateSerializer
    permission_classes = (IsAuthenticated,)


class LikeListAPI(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LikeDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (ObjectIsOwnerOrReadOnly,)


# ------------------------CommentAPIView--------------------------------------------
class CommentCreateAPI(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated,)


class CommentListAPI(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (ObjectIsOwnerOrReadOnly,)


# ------------------------FollowAPIView--------------------------------------------
class FollowCreateAPI(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowCreateSerializer
    permission_classes = (IsAuthenticated,)


class FollowListAPI(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FollowDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (ObjectIsOwnerOrReadOnly,)


class ParseTokenView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            avatar = None
            if user.avatar:
                avatar = f'http://localhost:8000{user.avatar.url}'
            user_data = {
                'user_id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'avatar': avatar
            }
            return Response(user_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)