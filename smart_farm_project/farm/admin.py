from django.contrib import admin
from .models import SensorData
# Register your models here.

@admin.register(SensorData)
class SensorAdmin(admin.ModelAdmin) :
   list_display = (
    'rev_date',
    'temp',
    'humi',
    'light',
    'rain',
    'water'
   )