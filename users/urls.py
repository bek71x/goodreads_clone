

from django.urls import path, include


from users.views import UserCreateView, UserLoginView, ProfileView, LogoutView, EditProfile

app_name = "user"




urlpatterns = [
    path('register/',UserCreateView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile/edit',EditProfile.as_view(),name='edit_profile'),
]

