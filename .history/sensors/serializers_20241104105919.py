from rest_framework import serializers
from .models import Sensor, SensorPredicted, SensorValues

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class SensorValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorValues
        fields = '__all__'

class SensorPredictedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorPredicted
        fields = '__all__'