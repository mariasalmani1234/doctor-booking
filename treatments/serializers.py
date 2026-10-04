from rest_framework import serializers

from .models import Treatment

from patients.models import Patient
from doctors.models import Doctor


class TreatmentSerializer(
    serializers.ModelSerializer
):

    patientId = serializers.PrimaryKeyRelatedField(
        source='patient',
        queryset=Patient.objects.all()
    )

    doctorId = serializers.PrimaryKeyRelatedField(
        source='doctor',
        read_only=True
    )

    patientName = serializers.SerializerMethodField()

    doctorName = serializers.SerializerMethodField()

    toothNumber = serializers.IntegerField(
        source='tooth_number',
        required=False,
        allow_null=True
    )

    startDate = serializers.DateField(
        source='start_date'
    )

    endDate = serializers.DateField(
        source='end_date',
        required=False,
        allow_null=True
    )

    createdAt = serializers.DateTimeField(
        source='created_at',
        read_only=True
    )

    updatedAt = serializers.DateTimeField(
        source='updated_at',
        read_only=True
    )

    class Meta:

        model = Treatment

        fields = [
            'id',
            'patientId',
            'patientName',
            'doctorId',
            'doctorName',
            'title',
            'diagnosis',
            'toothNumber',
            'status',
            'startDate',
            'endDate',
            'description',
            'createdAt',
            'updatedAt',
        ]

        read_only_fields = [
            'id',
            'patientName',
            'doctorId',
            'doctorName',
            'createdAt',
            'updatedAt',
        ]

    def get_patientName(self, obj):

        return (
            f'{obj.patient.user.first_name} '
            f'{obj.patient.user.last_name}'
        ).strip()

    def get_doctorName(self, obj):

        return (
            f'{obj.doctor.user.first_name} '
            f'{obj.doctor.user.last_name}'
        ).strip()

    def validate_toothNumber(self, value):

        if value is None:
            return value

        valid_teeth = {
            11, 12, 13, 14, 15, 16, 17, 18,
            21, 22, 23, 24, 25, 26, 27, 28,
            31, 32, 33, 34, 35, 36, 37, 38,
            41, 42, 43, 44, 45, 46, 47, 48,
        }

        if value not in valid_teeth:

            raise serializers.ValidationError(
                'شماره دندان معتبر نیست.'
            )

        return value

    def create(self, validated_data):

        doctor = (
            Doctor.objects
            .filter(
                user=self.context['request'].user
            )
            .first()
        )

        if doctor is None:

            raise serializers.ValidationError({
                'doctor':
                'برای کاربر فعلی پروفایل پزشک وجود ندارد.'
            })

        validated_data['doctor'] = doctor

        return super().create(
            validated_data
        )