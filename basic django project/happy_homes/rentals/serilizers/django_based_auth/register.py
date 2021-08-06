"""
though this project is a drf project but here i will practice in django
which can be class based or func based in future i will replace it will drf code
but the code will still remain here for my under standing
"""

from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]
