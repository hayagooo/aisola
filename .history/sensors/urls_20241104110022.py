from django.urls import path
from .views import SensorViewSet, SensorValuesViewSet, SensorPredictedViewSet

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

sensor_values_list = SensorValuesViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
sensor_values_detail = SensorValuesViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

sensor_predicted_list = SensorPredictedViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
sensor_predicted_detail = SensorPredictedViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

urlpatterns = [
    # Sensor URLs
    path('sensors/<int:device_id>/', sensor_list, name='sensor-list'),
    path('sensors/<int:device_id>/<int:pk>/', sensor_detail, name='sensor-detail'),

    # SensorValues URLs
    path('sensors/<int:sensor_id>/values/', sensor_values_list, name='sensor-values-list'),
    path('sensors/<int:sensor_id>/values/<int:pk>/', sensor_values_detail, name='sensor-values-detail'),

    # SensorPredicted URLs
    path('devices/<int:device_id>/predictions/', sensor_predicted_list, name='sensor-predicted-list'),
    path('devices/<int:device_id>/predictions/<int:pk>/', sensor_predicted_detail, name='sensor-predicted-detail'),
]
