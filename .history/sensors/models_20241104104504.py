from django.db import models
from devices.models import Device

class Sensor(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)
    min = models.FloatField()
    mid = models.FloatField()
    max = models.FloatField()
    interface = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.device.name}"
