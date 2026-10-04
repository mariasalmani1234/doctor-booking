from rest_framework import serializers

from .models import (
    MedicalCondition,
    MedicalRecord,
)

from patients.models import Patient


class MedicalConditionSerializer(
    serializers.ModelSerializer
):

    patientId = serializers.IntegerField(
        write_only=True
    )

    patientName = serializers.SerializerMethodField()

    doctorId = serializers.IntegerField(
        source='doctor.id',
        read_only=True
    )

    specialtyId = serializers.IntegerField(
        source='specialty.id',
        read_only=True
    )

    specialtyName = serializers.CharField(
        source='specialty.name',
        read_only=True
    )

    diagnosedAt = serializers.DateField(
        source='diagnosed_at'
    )

    class Meta:

        model = MedicalCondition

        fields = [
            'id',
            'patientId',
            'patientName',
            'doctorId',
            'specialtyId',
            'specialtyName',
            'name',
            'diagnosedAt',
            'isActive',
            'notes',
        ]

        read_only_fields = [
            'id',
            'patientName',
            'doctorId',
            'specialtyId',
            'specialtyName',
        ]

    def get_patientName(self, obj):

        return (
            f'{obj.patient.first_name} '
            f'{obj.patient.last_name}'
        ).strip()

    def create(self, validated_data):

        patient_id = validated_data.pop(
            'patientId',
            None
        )

        if not patient_id:

            raise serializers.ValidationError({
                'patientId':
                'شناسه بیمار الزامی است.'
            })

        try:

            patient = Patient.objects.select_related(
                'user'
            ).get(
                id=patient_id
            )

        except Patient.DoesNotExist:

            raise serializers.ValidationError({
                'patientId':
                'بیمار پیدا نشد.'
            })

        doctor = self.context[
            'request'
        ].user.doctor_profile

        validated_data['patient'] = patient.user
        validated_data['doctor'] = doctor
        validated_data['specialty'] = doctor.specialty

        return super().create(
            validated_data
        )


class MedicalRecordSerializer(
    serializers.ModelSerializer
):

    patientId = serializers.IntegerField(
        write_only=True
    )

    patientName = serializers.SerializerMethodField()

    doctorId = serializers.IntegerField(
        source='doctor.id',
        read_only=True
    )

    specialtyId = serializers.IntegerField(
        source='specialty.id',
        read_only=True
    )

    specialtyName = serializers.CharField(
        source='specialty.name',
        read_only=True
    )

    visitDate = serializers.DateField(
        source='visit_date'
    )

    createdAt = serializers.DateTimeField(
        source='created_at',
        read_only=True
    )

    class Meta:

        model = MedicalRecord

        fields = [
            'id',
            'patientId',
            'patientName',
            'doctorId',
            'specialtyId',
            'specialtyName',
            'visitDate',
            'diagnosis',
            'treatment',
            'notes',
            'createdAt',
        ]

        read_only_fields = [
            'id',
            'patientName',
            'doctorId',
            'specialtyId',
            'specialtyName',
            'createdAt',
        ]

    def get_patientName(self, obj):

        return (
            f'{obj.patient.first_name} '
            f'{obj.patient.last_name}'
        ).strip()

    def create(self, validated_data):

        patient_id = validated_data.pop(
            'patientId',
            None
        )

        if not patient_id:

            raise serializers.ValidationError({
                'patientId':
                'شناسه بیمار الزامی است.'
            })

        try:

            patient = Patient.objects.select_related(
                'user'
            ).get(
                id=patient_id
            )

        except Patient.DoesNotExist:

            raise serializers.ValidationError({
                'patientId':
                'بیمار پیدا نشد.'
            })

        doctor = self.context[
            'request'
        ].user.doctor_profile

        validated_data['patient'] = patient.user
        validated_data['doctor'] = doctor
        validated_data['specialty'] = doctor.specialty

        return super().create(
            validated_data
        )