
from django.contrib import admin
from django.urls import path, include

from config.urls import app_name
from users.views import UserCreateView, UserLoginView

app_name = "user"
urlpatterns = [
    path('register/',UserCreateView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
]

