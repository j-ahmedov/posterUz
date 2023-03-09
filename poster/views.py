from rest_framework import generics
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
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


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


