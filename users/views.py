from multiprocessing.resource_tracker import register

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from users.forms import RegisterForm


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
    def get(self,request):
        login_form = AuthenticationForm()

        return  render(request,'user/login.html',{'form':login_form})

    def post(self,request):

        login_form = AuthenticationForm(data= request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            return redirect("landing_page")
        else:
            return render(request, 'user/login.html', {'form': login_form})
