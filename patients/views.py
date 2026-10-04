from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from doctors.models import Doctor
from .models import Patient
from .serializers import PatientSerializer


class PatientSearchView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(
        self,
        request
    ):

        national_code = (
            request.query_params.get(
                'national_code'
            )
        )

        if not national_code:

            return Response(
                {
                    'detail':
                    'کد ملی الزامی است.'
                },
                status=400
            )

        patient = (
            Patient.objects
            .select_related('user')
            .filter(
                user__national_code=national_code
            )
            .first()
        )

        if patient is None:

            return Response(
                {
                    'detail':
                    'بیمار با این کد ملی پیدا نشد.'
                },
                status=404
            )

        serializer = PatientSerializer(
            patient
        )

        return Response(
            serializer.data
        )


class PatientDetailView(
    generics.RetrieveAPIView
):

    serializer_class = PatientSerializer

    permission_classes = [
        IsAuthenticated
    ]

    queryset = (
        Patient.objects
        .select_related('user')
    )

class PatientDetailView(
    generics.RetrieveAPIView
):

    serializer_class = PatientSerializer

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
            return Patient.objects.none()

        return (
            Patient.objects
            .select_related('user')
            .all()
        )    