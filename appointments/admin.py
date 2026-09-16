from django.contrib import admin

from .models import (
    Appointment,
    DoctorSchedule,
    MedicalCondition,
    MedicalRecord,
)


@admin.register(DoctorSchedule)
class DoctorScheduleAdmin(admin.ModelAdmin):

    list_display = [
        'doctor',
        'day_of_week',
        'start_time',
        'end_time',
        'is_active',
    ]

    list_filter = [
        'day_of_week',
        'is_active',
    ]


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = [
        'doctor',
        'patient',
        'date',
        'time',
        'status',
        'created_at',
    ]

    list_filter = [
        'status',
        'date',
    ]

    search_fields = [
        'doctor__user__first_name',
        'doctor__user__last_name',
        'patient__national_code',
    ]


@admin.register(MedicalCondition)
class MedicalConditionAdmin(admin.ModelAdmin):

    list_display = [
        'patient',
        'name',
        'doctor',
        'specialty',
        'diagnosed_at',
        'is_active',
    ]

    list_filter = [
        'specialty',
        'is_active',
        'diagnosed_at',
    ]

    search_fields = [
        'patient__national_code',
        'patient__first_name',
        'patient__last_name',
        'doctor__user__first_name',
        'doctor__user__last_name',
        'name',
    ]


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):

    list_display = [
        'patient',
        'doctor',
        'specialty',
        'visit_date',
        'diagnosis',
        'created_at',
    ]

    list_filter = [
        'specialty',
        'visit_date',
    ]

    search_fields = [
        'patient__national_code',
        'patient__first_name',
        'patient__last_name',
        'doctor__user__first_name',
        'doctor__user__last_name',
        'diagnosis',
    ]