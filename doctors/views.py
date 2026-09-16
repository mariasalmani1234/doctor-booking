from rest_framework import viewsets

from .models import Doctor, Specialty
from .serializers import DoctorSerializer, SpecialtySerializer


class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.select_related(
        'user',
        'specialty'
    ).all()

    serializer_class = DoctorSerializer

    def get_queryset(self):
        queryset = self.queryset

        specialty = self.request.query_params.get('specialty')
        city = self.request.query_params.get('city')
        area = self.request.query_params.get('area')
        search = self.request.query_params.get('search')

        if specialty:
            queryset = queryset.filter(specialty_id=specialty)

        if city:
            queryset = queryset.filter(city__icontains=city)

        if area:
            queryset = queryset.filter(area__icontains=area)

        if search:
            queryset = queryset.filter(
                user__first_name__icontains=search
            ) | queryset.filter(
                user__last_name__icontains=search
            )

        return queryset