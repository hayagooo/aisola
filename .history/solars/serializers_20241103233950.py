from rest_framework import serializers
from .models import Solars, Output

class SolarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solars
        fields = '__all__'

class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Output
        fields = '__all__'
