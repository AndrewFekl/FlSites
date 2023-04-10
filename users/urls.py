from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CreateUserView, LoginUserView, ListUserView, DetailUserView, UpdateUserView
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', CreateUserView.as_view(), name="create_user"),
    path('login/', LoginUserView.as_view(), name="login_user"),
    path('users/', ListUserView.as_view(), name='users'),
    path('users/<int:pk>/', DetailUserView.as_view(), name='user'),
    path('update/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    ]
