from django.urls import path, include
from .views import *


urlpatterns = [

    # ---------------urls for User API------------------------------------
    path('api/v1/user/list/', UserListAPI.as_view()),
    path('api/v1/user/create/', UserCreateAPI.as_view()),
    path('api/v1/user/detail/<int:pk>', UserDetailAPI.as_view()),
    path('api/v1/user/post/list/<int:pk>', UserPostsAPI.as_view()),
    path('api/v1/user/following/list/<int:pk>', UserFollowingsAPI.as_view()),

    # --------------urls for Post API-----------------------------------
    path('api/v1/post/list/', PostListAPI.as_view()),
    path('api/v1/post/create/', PostCreateAPI.as_view()),
    path('api/v1/post/detail/<int:pk>', PostDetailAPI.as_view()),
    path('api/v1/post/comment/detail/<int:pk>', PostCommentsListAPI.as_view()),

    # ---------------urls for Like API------------------------------------
    path('api/v1/like/list/', LikeListAPI.as_view()),
    path('api/v1/like/create/', LikeCreateAPI.as_view()),
    path('api/v1/like/detail/<int:pk>', LikeDetailAPI.as_view()),

    # ---------------urls for Comment API------------------------------------
    path('api/v1/comment/list/', CommentListAPI.as_view()),
    path('api/v1/comment/create/', CommentCreateAPI.as_view()),
    path('api/v1/comment/detail/<int:pk>', CommentDetailAPI.as_view()),

    # ---------------urls for Follow API------------------------------------
    path('api/v1/follow/list/', FollowListAPI.as_view()),
    path('api/v1/follow/create/', FollowCreateAPI.as_view()),
    path('api/v1/follow/detail/<int:pk>', FollowDetailAPI.as_view()),

]
