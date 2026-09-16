from django.contrib import admin

from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = [
        'user',
        'birth_date',
        'address',
    ]

    search_fields = [
        'user__national_code',
        'user__first_name',
        'user__last_name',
    ]