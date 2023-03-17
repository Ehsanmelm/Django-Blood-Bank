from django.db import models
from django.conf import settings

# Create your models here.


class BloodModel(models.Model):
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
    blood = models.CharField(default=None, choices=BLOOD_TYPE, max_length=10)
    unit = models.PositiveIntegerField()


class BloodRequestModel(models.Model):
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
    STATUS_STEP = [
        ('Pending', 'Pending'),
        ('Accept', 'Accept'),
        ('Denied', 'Denied'),
    ]
    requested_patient_id = models.PositiveIntegerField(null=True)
    requested_donor_id = models.PositiveIntegerField(null=True)
    reason = models.TextField(default=None)
    bloodtype = models.CharField(
        choices=BLOOD_TYPE, max_length=255, default=None)
    unit = models.PositiveIntegerField()
    status = models.CharField(
        choices=STATUS_STEP,
        max_length=255, default='Pending')
    date = models.DateField(auto_now=True)

    # is_donor = models.BooleanField(default=False)
    # is_patient = models.BooleanField(default=False)
