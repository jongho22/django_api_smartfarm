from .models import SensorData
from rest_framework import serializers

class SensorSerializer(serializers.ModelSerializer):

    class Meta :
        model = SensorData
        fields = ['rev_date','temp','humi','light','rain','water']