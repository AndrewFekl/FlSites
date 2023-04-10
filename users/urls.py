from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import ListUserView, DetailUserView, UserUpdateView, UserRegistrationView
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', UserRegistrationView.as_view(), name="create_user"),
    path('users/', ListUserView.as_view(), name='users'),
    path('users/<int:pk>/', DetailUserView.as_view(), name='user'),
    path('update/', UserUpdateView.as_view(), name='update_user'),
    ]
