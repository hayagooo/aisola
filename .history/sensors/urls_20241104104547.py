from django.urls import path
from .views import SensorViewSet

sensor_list = SensorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

sensor_detail = SensorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('sensors/<int:device_id>/', sensor_list, name='sensor-list'),
    path('sensors/<int:device_id>/<int:pk>/', sensor_detail, name='sensor-detail'),
]
