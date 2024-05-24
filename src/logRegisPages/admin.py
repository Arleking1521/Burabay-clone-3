from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('name', 'surename', 'email', 'phone')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'surename', 'email', 'phone', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'username', 'name', 'surename', 'is_staff')
    search_fields = ('email', 'username', 'name', 'surename')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
