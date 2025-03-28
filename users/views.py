from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from users.forms import RegisterForm, ProfileForm
from users.models import Follow

User = get_user_model()

@login_required
def follow_user(request, pk):
    user_to_follow = get_object_or_404(User, pk=pk)
    if request.user != user_to_follow and not Follow.objects.filter(follower=request.user, following=user_to_follow).exists():
        Follow.objects.create(follower=request.user, following=user_to_follow)
    return redirect('user:follow_profile', pk=pk)

@login_required
def unfollow_user(request, pk):
    user_to_unfollow = get_object_or_404(User, pk=pk)
    Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    return redirect('user:follow_profile', pk=pk)
@method_decorator(login_required(login_url='user:login'), name='dispatch')
class FollowProfileView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        is_following = Follow.objects.filter(follower=request.user, following=user).exists()
        return render(request, 'user/user_detail.html', {'user': user, 'is_following': is_following})

class UserListView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        users = User.objects.exclude(id=request.user.id)

        if query:
            users = users.filter(username__icontains=query)

        return render(request, 'user/user_list.html', {'users': users, 'query': query})


class UserDetailView(View):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        is_following = Follow.objects.filter(follower=request.user, following=user).exists()
        return render(request, 'user/user_detail.html', {'user': user, 'is_following': is_following})

class UserCreateView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
        return render(request, 'user/register.html', {'form': form})

class UserLoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, 'user/login.html', {'form': login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, f"Siz akkauntingizga kirdingiz {user.username}!✅")
            return redirect("landing_page")
        return render(request, 'user/login.html', {'form': login_form})

class ProfileView(View):
    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)
        context = {'user': user}
        return render(request, 'user/profile.html', context)

class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.info(request, "Siz tizimdan chiqdingiz📤")
        return redirect("landing_page")

class EditProfile(View):
    def get(self, request):
        user_form = ProfileForm(instance=request.user)
        return render(request, 'user/edit_profile.html', {'user_form': user_form})

    def post(self, request):
        user_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('user:profile')
        return render(request, 'user/edit_profile.html', {'user_form': user_form})
