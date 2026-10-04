from django.urls import path

from .views import (
    PatientSearchView,
    PatientDetailView
)


urlpatterns = [

    path(
        'search/',
        PatientSearchView.as_view(),
        name='patient-search'
    ),

    path(
        '<int:pk>/',
        PatientDetailView.as_view(),
        name='patient-detail'
    ),

]