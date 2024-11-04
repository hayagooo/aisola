from django.db import models
from devices.models import Device  # Import Device model

class Datasheet(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    application = models.CharField(max_length=100)
    serial = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    values = models.JSONField()
    maintenances = models.JSONField()
    operationals = models.JSONField()
    faults = models.JSONField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.device.name}"
