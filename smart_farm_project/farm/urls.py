from django.urls import path,include
from .views import SensorViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('SensorData', SensorViewset, basename='SensorData')

urlpatterns = [
    path('', include(router.urls)),
]