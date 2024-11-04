from django.urls import path
from .views import DatasheetViewSet

datasheet_list = DatasheetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

datasheet_detail = DatasheetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('datasheet/<int:device_id>/', datasheet_list, name='datasheet-list'),
    path('datasheet/<int:device_id>/<int:pk>/', datasheet_detail, name='datasheet-detail'),
]
