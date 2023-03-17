from django.db import models
from django.conf import settings
from django.contrib import admin
# Create your models here.


class DonorModel(models.Model):
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
    donor = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True)

    bloodtype = models.CharField(
        default=None, max_length=10, choices=BLOOD_TYPE)

    address = models.TextField()
    mobile = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    @admin.display(ordering='donor__first_name')
    def first_name(self):
        return self.donor.first_name

    @admin.display(ordering='donor__last_name')
    def last_name(self):
        return self.donor.last_name


class DonateRequestModel(models.Model):
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

    requested_donor_id = models.PositiveIntegerField()

    disease = models.CharField(max_length=255)
    bloodtype = models.CharField(
        choices=BLOOD_TYPE, max_length=10, default=None)
    unit = models.PositiveIntegerField()
    status = models.CharField(
        default='Pending', max_length=20, choices=STATUS_STEP)

    date = models.DateField(auto_now=True)
