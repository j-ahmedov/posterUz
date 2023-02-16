from django.urls import path
from .views import *


urlpatterns = [
    # --------------urls for API-----------------------------------
    path('api/v1/post-list/', PostAPIView.as_view()),
    path('api/v1/post/<int:pk>', PostAPIView.as_view()),
    path('api/v1/post/update/<int:pk>', PostAPIView.as_view()),
    path('api/v1/post/delete/<int:pk>', PostAPIView.as_view()),

]
