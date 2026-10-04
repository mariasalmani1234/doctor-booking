from django.urls import path

from .views import (
    AppointmentListCreateView,
    AppointmentDetailView,
    DoctorScheduleListCreateView,
    MedicalConditionListCreateView,
    MedicalConditionDetailView,
    MedicalRecordListCreateView,
    MedicalRecordDetailView,
)

urlpatterns = [

    path(
        '',
        AppointmentListCreateView.as_view(),
        name='appointment-list-create'
    ),

    path(
        'schedules/',
        DoctorScheduleListCreateView.as_view(),
        name='doctor-schedule-list-create'
    ),

    path(
        '<int:pk>/',
        AppointmentDetailView.as_view(),
        name='appointment-detail'
    ),

    path(
        'medical-conditions/',
        MedicalConditionListCreateView.as_view(),
        name='medical-condition-list-create'
    ),

    path(
        'medical-conditions/<int:pk>/',
        MedicalConditionDetailView.as_view(),
        name='medical-condition-detail'
    ),

    path(
        'medical-records/',
        MedicalRecordListCreateView.as_view(),
        name='medical-record-list-create'
    ),

    path(
        'medical-records/<int:pk>/',
        MedicalRecordDetailView.as_view(),
        name='medical-record-detail'
    ),

]