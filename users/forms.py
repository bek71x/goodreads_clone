from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','first_name', 'last_name', 'gender','profile_picture' ]

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','first_name', 'last_name', 'gender','profile_picture' ]