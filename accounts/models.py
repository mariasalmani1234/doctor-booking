from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        PATIENT = 'PATIENT', 'بیمار'
        DOCTOR = 'DOCTOR', 'پزشک'
        ADMIN = 'ADMIN', 'مدیر'

    national_code = models.CharField(
        'کد ملی',
        max_length=10,
        unique=True,
        null=True,
        blank=True
    )

    phone = models.CharField(
        'شماره تلفن',
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )

    role = models.CharField(
        'نقش کاربر',
        max_length=20,
        choices=Role.choices,
        default=Role.PATIENT
    )

    USERNAME_FIELD = 'national_code'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.national_code or self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'