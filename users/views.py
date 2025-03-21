from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from users.forms import RegisterForm, ProfileForm
from users.models import CustomUser  # To'g'ri import

class UserCreateView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Bu yerda CustomUser modeli asosida foydalanuvchi yaratiladi
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
        else:
            return render(request, 'user/login.html', {'form': login_form})

class ProfileView(View):
    def get(self, request):
        # CustomUser modelidan foydalanamiz
        user = CustomUser.objects.get(id=request.user.id)
        context = {'user': user}
        if user.is_authenticated:
            return render(request, 'user/profile.html', context)
        else:
            return redirect("user:login")

class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.info(request, "Siz tizimdan chiqdingiz📤")
        return redirect("landing_page")

class EditProfile(View):
    def get(self, request):
        user_form = ProfileForm(instance=request.user)
        context = {'user_form': user_form}
        return render(request, 'user/edit_profile.html', context)

    def post(self, request):
        user_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        context = {'user_form': user_form}
        if user_form.is_valid():
            user_form.save()
            return redirect('user:profile')
        return render(request, 'user/edit_profile.html', context)
