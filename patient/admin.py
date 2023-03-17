from django.contrib import admin
from .models import patientModel

# Register your models here.


class PatientAmdin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'bloodtype',]


admin.site.register(patientModel, PatientAmdin)
