from django.db import models

class Solars(models.Model):
    user_id = models.IntegerField()
    voltage = models.FloatField()
    current = models.FloatField()
    azimuth = models.FloatField()
    direction = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Solar {self.user_id} - {self.timestamp}"

class Output(models.Model):
    solar = models.ForeignKey(Solars, on_delete=models.CASCADE)
    voltage = models.FloatField()
    current = models.FloatField()
    power = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Output for Solar {self.solar.user_id} - {self.timestamp}"
