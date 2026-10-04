from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Treatment
from .serializers import TreatmentSerializer

from doctors.models import Doctor


class TreatmentListCreateView(
    generics.ListCreateAPIView
):

    serializer_class = TreatmentSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        doctor = (
            Doctor.objects
            .filter(
                user=self.request.user
            )
            .first()
        )

        if doctor is None:

            return Treatment.objects.none()

        queryset = (
            Treatment.objects
            .select_related(
                'patient',
                'patient__user',
                'doctor',
                'doctor__user'
            )
            .filter(
                doctor=doctor
            )
        )

        patient_id = (
            self.request.query_params
            .get('patient_id')
        )

        if patient_id:

            queryset = queryset.filter(
                patient_id=patient_id
            )

        tooth_number = (
            self.request.query_params
            .get('tooth_number')
        )

        if tooth_number:

            queryset = queryset.filter(
                tooth_number=tooth_number
            )

        return queryset


class TreatmentDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = TreatmentSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        doctor = (
            Doctor.objects
            .filter(
                user=self.request.user
            )
            .first()
        )

        if doctor is None:

            return Treatment.objects.none()

        return (
            Treatment.objects
            .select_related(
                'patient',
                'patient__user',
                'doctor',
                'doctor__user'
            )
            .filter(
                doctor=doctor
            )
        )