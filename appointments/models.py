from django.conf import settings
from django.db import models

from doctors.models import Doctor


class DoctorSchedule(models.Model):

    class WeekDay(models.IntegerChoices):
        SATURDAY = 5, 'شنبه'
        SUNDAY = 6, 'یکشنبه'
        MONDAY = 0, 'دوشنبه'
        TUESDAY = 1, 'سه‌شنبه'
        WEDNESDAY = 2, 'چهارشنبه'
        THURSDAY = 3, 'پنجشنبه'
        FRIDAY = 4, 'جمعه'

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='schedules',
        verbose_name='پزشک'
    )

    day_of_week = models.IntegerField(
        choices=WeekDay.choices,
        verbose_name='روز هفته'
    )

    start_time = models.TimeField(
        verbose_name='ساعت شروع'
    )

    end_time = models.TimeField(
        verbose_name='ساعت پایان'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='فعال'
    )

    def __str__(self):
        return f"{self.doctor} - {self.get_day_of_week_display()}"

    class Meta:
        verbose_name = 'برنامه کاری پزشک'
        verbose_name_plural = 'برنامه‌های کاری پزشکان'


class Appointment(models.Model):

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'در انتظار'
        CONFIRMED = 'CONFIRMED', 'تایید شده'
        CANCELLED = 'CANCELLED', 'لغو شده'
        COMPLETED = 'COMPLETED', 'انجام شده'

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments',
        verbose_name='پزشک'
    )

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='appointments',
        verbose_name='بیمار'
    )

    date = models.DateField(
        verbose_name='تاریخ نوبت'
    )

    time = models.TimeField(
        verbose_name='ساعت نوبت'
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name='وضعیت'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ثبت'
    )

    class Meta:
        ordering = ['date', 'time']

        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'date', 'time'],
                name='unique_doctor_appointment'
            )
        ]

        verbose_name = 'نوبت'
        verbose_name_plural = 'نوبت‌ها'

    def __str__(self):
        return f"{self.doctor} - {self.patient} - {self.date} {self.time}"


class MedicalCondition(models.Model):

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='medical_conditions',
        verbose_name='بیمار'
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.PROTECT,
        related_name='diagnosed_conditions',
        verbose_name='پزشک تشخیص‌دهنده'
    )

    specialty = models.ForeignKey(
        'doctors.Specialty',
        on_delete=models.PROTECT,
        related_name='medical_conditions',
        verbose_name='تخصص'
    )

    name = models.CharField(
        max_length=200,
        verbose_name='نام بیماری'
    )

    diagnosed_at = models.DateField(
        verbose_name='تاریخ تشخیص'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='بیماری فعال'
    )

    notes = models.TextField(
        blank=True,
        verbose_name='توضیحات'
    )

    def __str__(self):
        return f"{self.patient} - {self.name}"

    class Meta:
        verbose_name = 'بیماری'
        verbose_name_plural = 'بیماری‌ها'


class MedicalRecord(models.Model):

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='medical_records',
        verbose_name='بیمار'
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.PROTECT,
        related_name='medical_records',
        verbose_name='پزشک'
    )

    specialty = models.ForeignKey(
        'doctors.Specialty',
        on_delete=models.PROTECT,
        related_name='medical_records',
        verbose_name='تخصص'
    )

    visit_date = models.DateField(
        verbose_name='تاریخ مراجعه'
    )

    diagnosis = models.TextField(
        blank=True,
        verbose_name='تشخیص'
    )

    treatment = models.TextField(
        blank=True,
        verbose_name='درمان'
    )

    notes = models.TextField(
        blank=True,
        verbose_name='یادداشت پزشک'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ثبت'
    )

    def __str__(self):
        return (
            f"{self.patient} - "
            f"{self.specialty} - "
            f"{self.visit_date}"
        )

    class Meta:
        verbose_name = 'سابقه پزشکی'
        verbose_name_plural = 'سوابق پزشکی'