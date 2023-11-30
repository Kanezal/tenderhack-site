from django.contrib.auth.forms import UserCreationForm
from . import models

class RegisterForm(UserCreationForm):
    class Meta:
        model = models.TenderUser
        fields = ['name', 'email', 'role', 'description', 'password1', 'password2']

