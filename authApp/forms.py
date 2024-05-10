from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("password1", "password2")

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
  