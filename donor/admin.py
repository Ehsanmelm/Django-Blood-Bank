from django.contrib import admin
from .models import DonorModel, DonateRequestModel

# Register your models here.


class DonorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'bloodtype']


admin.site.register(DonorModel, DonorAdmin)
admin.site.register(DonateRequestModel)
