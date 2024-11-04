from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('devices.urls')),
    path('api/', include('sensors.urls')), 
    path('api/', include('actuators.urls')), 
    path('api/', include('industries.urls')), 
]
