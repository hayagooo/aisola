from django.db import models
from devices.models import Device  # Import Device model

class Actuator(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)
    min = models.FloatField()
    max = models.FloatField()
    modules = models.JSONField()
    speed = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.device.name}"
