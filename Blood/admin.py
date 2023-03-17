from django.contrib import admin
from .models import BloodModel, BloodRequestModel

# Register your models here.


class BloodMAnaging_Admin(admin.ModelAdmin):
    list_display = ['blood', 'unit']


admin.site.register(BloodModel, BloodMAnaging_Admin)
admin.site.register(BloodRequestModel)
