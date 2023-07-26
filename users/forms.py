from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('full_name', 'phone_number', 'is_phone_confirmed', 'image', 'role', 'is_active')



class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('full_name', 'phone_number', 'is_phone_confirmed', 'image', 'role', 'is_active')
