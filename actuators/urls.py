from django.urls import path
from .views import ActuatorViewSet

actuator_list = ActuatorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

actuator_detail = ActuatorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('actuators/<int:device_id>/', actuator_list, name='actuator-list'),
    path('actuators/<int:device_id>/<int:pk>/', actuator_detail, name='actuator-detail'),
]
