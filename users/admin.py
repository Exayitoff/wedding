from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['full_name', 'phone_number', 'is_phone_confirmed', 'image', 'role', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('full_name', 'phone_number', 'is_phone_confirmed', 'image', 'role', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('full_name', 'phone_number', 'is_phone_confirmed', 'image', 'role', )}),
    )

admin.site.register(User, CustomUserAdmin)
