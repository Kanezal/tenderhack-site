from django.contrib.auth.forms import UserCreationForm
from . import models
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = models.TenderUser
        fields = ['first_name', 'role', 'email', 'password1', 'password2']

