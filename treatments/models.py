from django.conf import settings
from django.db import models

from doctors.models import Doctor
from patients.models import Patient


class Treatment(models.Model):

    class Status(models.TextChoices):

        IN_PROGRESS = (
            'in_progress',
            'در حال انجام'
        )

        COMPLETED = (
            'completed',
            'تکمیل شده'
        )

        INCOMPLETE = (
            'incomplete',
            'نیاز به بررسی'
        )

        CANCELLED = (
            'cancelled',
            'لغو شده'
        )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='treatments',
        verbose_name='بیمار'
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.PROTECT,
        related_name='treatments',
        verbose_name='پزشک'
    )

    title = models.CharField(
        'عنوان درمان',
        max_length=200
    )

    diagnosis = models.TextField(
        'تشخیص',
        blank=True
    )

    tooth_number = models.PositiveSmallIntegerField(
        'شماره دندان',
        null=True,
        blank=True
    )

    status = models.CharField(
        'وضعیت',
        max_length=20,
        choices=Status.choices,
        default=Status.IN_PROGRESS
    )

    start_date = models.DateField(
        'تاریخ شروع'
    )

    end_date = models.DateField(
        'تاریخ پایان',
        null=True,
        blank=True
    )

    description = models.TextField(
        'توضیحات',
        blank=True
    )

    created_at = models.DateTimeField(
        'تاریخ ایجاد',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'آخرین بروزرسانی',
        auto_now=True
    )

    class Meta:

        ordering = [
            '-created_at'
        ]

        verbose_name = 'درمان'

        verbose_name_plural = 'درمان‌ها'

    def __str__(self):

        if self.tooth_number:
            return (
                f'{self.title} - '
                f'دندان {self.tooth_number}'
            )

        return self.title