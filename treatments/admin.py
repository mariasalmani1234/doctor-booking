from django.contrib import admin

from .models import Treatment


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'patient',
        'doctor',
        'title',
        'tooth_number',
        'status',
        'start_date',
        'end_date',
        'created_at',
    ]

    list_filter = [
        'status',
        'start_date',
        'end_date',
    ]

    search_fields = [
        'title',
        'diagnosis',
        'patient__user__national_code',
        'patient__user__first_name',
        'patient__user__last_name',
        'doctor__user__national_code',
    ]

    ordering = [
        '-created_at'
    ]