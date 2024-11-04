from django.urls import path
from .views import DatasheetViewSet, IncidentsViewSet
from rest_framework.routers import DefaultRouter

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

router = DefaultRouter()
router.register(r'incidents', IncidentsViewSet)

urlpatterns = [
    path('datasheet/<int:device_id>/', datasheet_list, name='datasheet-list'),
    path('datasheet/<int:device_id>/<int:pk>/', datasheet_detail, name='datasheet-detail'),
]
