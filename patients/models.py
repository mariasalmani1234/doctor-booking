from django.conf import settings
from django.db import models


class Patient(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient_profile',
        verbose_name='کاربر'
    )

    birth_date = models.DateField(
        'تاریخ تولد',
        null=True,
        blank=True
    )

    address = models.TextField(
        'آدرس',
        blank=True
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = 'بیمار'
        verbose_name_plural = 'بیماران'
        