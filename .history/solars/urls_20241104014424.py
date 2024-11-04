from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'solars', views.SolarsViewSet)
router.register(r'output', views.OutputViewSet)

urlpatterns = [
    path('solars/', include(router.urls)),
]
