from django.db import models
from django.conf import settings
from django.contrib import admin

# Create your models here.


class patientModel(models.Model):
    BLOOD_TYPE = [
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O+', 'O+'),
        ('AB+', 'AB+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('AB-', 'AB-'),
    ]

    patient = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True)
    age = models.PositiveIntegerField(default=None)

    bloodtype = models.CharField(
        max_length=10, choices=BLOOD_TYPE)
    disease = models.CharField(max_length=255)

    address = models.TextField()
    mobile = models.CharField(max_length=20, null=False)

    # is_donor = models.BooleanField(default=False)
    # is_patient = models.BooleanField(default=False)

    @admin.display(ordering='patient__first_name')
    def first_name(self):
        return self.patient.first_name

    @admin.display(ordering='patient__last_name')
    def last_name(self):
        return self.patient.last_name
