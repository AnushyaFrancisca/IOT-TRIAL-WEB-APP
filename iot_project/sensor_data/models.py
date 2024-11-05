from django.db import models
from django.utils import timezone

class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Temp: {self.temperature}, Humidity: {self.humidity}, Time: {self.timestamp}"

# Create your models here.
