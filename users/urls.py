from django.urls import path, include

from users.models import Follow
from users.views import UserCreateView, UserLoginView, ProfileView, LogoutView, EditProfile, follow_user, \
    UserDetailView, UserListView, FollowProfileView, unfollow_user

app_name = "user"




urlpatterns = [
    path('register/',UserCreateView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/<int:pk>/', FollowProfileView.as_view(), name='follow_profile'),
    path('follow/<int:pk>/', follow_user, name='follow'),
    path('unfollow/<int:pk>/', unfollow_user, name='unfollow'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('profile/<int:user_id>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/edit',EditProfile.as_view(),name='edit_profile'),
]

