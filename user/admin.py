from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import AdminUserCreationForm, AdminUserChangeForm
from .models import User, UserRole


# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = AdminUserChangeForm
    add_form = AdminUserCreationForm

    list_display = (
        'first_name', 'last_name', 'email', 'active', 'admin'
    )
    list_filter = (
        'admin', 'staff', 'active',
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Information', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'first_name', 'last_name', 'password', 'password2'),
        }),
    )
    search_fields = (
        'email', 'first_name', 'last_name'
    )
    ordering = (
        'email',
    )
    filter_horizontal = ()

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'role',
    )
    list_filter = (
        'role',
    )
