from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            'اطلاعات سامانه',
            {
                'fields': (
                    'national_code',
                    'phone',
                    'role',
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'اطلاعات سامانه',
            {
                'fields': (
                    'national_code',
                    'phone',
                    'role',
                )
            },
        ),
    )

    list_display = [
        'national_code',
        'first_name',
        'last_name',
        'email',
        'phone',
        'role',
        'is_staff',
    ]

    list_filter = [
        'role',
        'is_staff',
    ]

    search_fields = [
        'national_code',
        'first_name',
        'last_name',
        'phone',
    ]