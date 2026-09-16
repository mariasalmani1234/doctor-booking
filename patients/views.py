from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Patient
from .serializers import PatientSerializer


class PatientSearchView(generics.RetrieveAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        national_code = self.request.query_params.get('national_code')

        if not national_code:
            return None

        return Patient.objects.select_related('user').filter(
            user__national_code=national_code
        ).first()

    def retrieve(self, request, *args, **kwargs):
        patient = self.get_object()

        if patient is None:
            return Response(
                {'detail': 'بیمار با این کد ملی پیدا نشد.'},
                status=404
            )

        serializer = self.get_serializer(patient)

        return Response(serializer.data)