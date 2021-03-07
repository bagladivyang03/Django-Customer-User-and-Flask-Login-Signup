from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','fullname','street','city','pincode','mobile', 'is_staff', 'is_active',)
    list_filter = ('email','fullname','street','city','pincode','mobile', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password','fullname','street','city','pincode','mobile')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','fullname','street','city','pincode','mobile', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)