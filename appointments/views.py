from patients.models import Patient

from .models import (
    Appointment,
    DoctorSchedule,
    MedicalCondition,
    MedicalRecord,
)

class MedicalConditionListCreateView(
    generics.ListCreateAPIView
):

    serializer_class = MedicalConditionSerializer

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

            return MedicalCondition.objects.none()

        queryset = (
            MedicalCondition.objects
            .select_related(
                'patient',
                'doctor',
                'specialty'
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

            patient = (
                Patient.objects
                .filter(id=patient_id)
                .first()
            )

            if patient is None:

                return queryset.none()

            queryset = queryset.filter(
                patient=patient.user
            )

        return queryset


class MedicalConditionDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = MedicalConditionSerializer

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

            return MedicalCondition.objects.none()

        return (
            MedicalCondition.objects
            .select_related(
                'patient',
                'doctor',
                'specialty'
            )
            .filter(
                doctor=doctor
            )
        )


class MedicalRecordListCreateView(
    generics.ListCreateAPIView
):

    serializer_class = MedicalRecordSerializer

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

            return MedicalRecord.objects.none()

        queryset = (
            MedicalRecord.objects
            .select_related(
                'patient',
                'doctor',
                'specialty'
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

            patient = (
                Patient.objects
                .filter(id=patient_id)
                .first()
            )

            if patient is None:

                return queryset.none()

            queryset = queryset.filter(
                patient=patient.user
            )

        return queryset


class MedicalRecordDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = MedicalRecordSerializer

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

            return MedicalRecord.objects.none()

        return (
            MedicalRecord.objects
            .select_related(
                'patient',
                'doctor',
                'specialty'
            )
            .filter(
                doctor=doctor
            )
        )