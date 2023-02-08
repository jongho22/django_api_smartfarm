from django.db import models

class SensorData(models.Model) :
    rev_date = models.DateTimeField(auto_now_add=True)
    temp = models.IntegerField()
    humi = models.IntegerField()
    light = models.IntegerField()
    rain = models.IntegerField()
    water = models.IntegerField()