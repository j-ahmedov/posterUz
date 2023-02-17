from django.urls import path
from .views import *


urlpatterns = [
    # --------------urls for Post API-----------------------------------
    path('api/v1/post-list/', PostAPIView.as_view()),
    path('api/v1/post/create/', PostAPIView.as_view()),
    path('api/v1/post/<int:pk>', PostAPIView.as_view()),
    path('api/v1/post/update/<int:pk>', PostAPIView.as_view()),
    path('api/v1/post/delete/<int:pk>', PostAPIView.as_view()),


    # ---------------urls for User API------------------------------------
    path('api/v1/user-list/', UserAPIView.as_view()),
    path('api/v1/user/create/', UserAPIView.as_view()),
    path('api/v1/user/<int:pk>', UserAPIView.as_view()),
    path('api/v1/user/update/<int:pk>', UserAPIView.as_view()),
    path('api/v1/user/delete/<int:pk>', UserAPIView.as_view()),

]
