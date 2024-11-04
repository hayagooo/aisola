from rest_framework import serializers
from .models import Datasheet

class DatasheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datasheet
        fields = '__all__'


class IncidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidents
        fields = '__all__'