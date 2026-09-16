from django.contrib import admin

from .models import Doctor, Specialty


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'name',
    ]

    search_fields = [
        'name',
    ]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = [
        'user',
        'specialty',
        'city',
        'area',
        'experience',
        'rating',
        'is_active',
    ]

    list_filter = [
        'specialty',
        'city',
        'is_active',
    ]

    search_fields = [
        'user__first_name',
        'user__last_name',
        'user__national_code',
    ]

    @admin.display(description='نام پزشک')
    def doctor_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"