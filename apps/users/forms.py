from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class CusomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'first_name', 'last_name']
        error_class = "error"


class CusomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        error_class = "error"
