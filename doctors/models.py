from django.conf import settings
from django.db import models


class Specialty(models.Model):

    name = models.CharField(
        'نام تخصص',
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تخصص'
        verbose_name_plural = 'تخصص‌ها'


class Doctor(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctor_profile',
        verbose_name='کاربر'
    )

    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.PROTECT,
        related_name='doctors',
        verbose_name='تخصص'
    )

    city = models.CharField(
        'شهر',
        max_length=100
    )

    area = models.CharField(
        'منطقه',
        max_length=100,
        blank=True
    )

    experience = models.PositiveIntegerField(
        'سابقه کاری',
        default=0
    )

    bio = models.TextField(
        'درباره پزشک',
        blank=True
    )

    image = models.ImageField(
        'تصویر پزشک',
        upload_to='doctors/',
        blank=True,
        null=True
    )

    rating = models.DecimalField(
        'امتیاز',
        max_digits=2,
        decimal_places=1,
        default=0
    )

    is_active = models.BooleanField(
        'فعال',
        default=True
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = 'پزشک'
        verbose_name_plural = 'پزشکان'