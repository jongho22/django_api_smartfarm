from django.shortcuts import render
from .models import SensorData
from .serializers import SensorSerializer

from rest_framework import viewsets
# Create your views here.
class SensorViewset(viewsets.ModelViewSet) :
    queryset = SensorData.objects.all()
    serializer_class = SensorSerializer