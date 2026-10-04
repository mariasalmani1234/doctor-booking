from django.urls import path

from .views import (
    TreatmentListCreateView,
    TreatmentDetailView,
)


urlpatterns = [

    path(
        '',
        TreatmentListCreateView.as_view(),
        name='treatment-list-create'
    ),

    path(
        '<int:pk>/',
        TreatmentDetailView.as_view(),
        name='treatment-detail'
    ),

]