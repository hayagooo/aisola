from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Sensor
from devices.models import Device
from .serializers import SensorSerializer

class SensorViewSet(viewsets.ViewSet):
    def list(self, request, device_id=None):
        sensors = Sensor.objects.filter(device_id=device_id)
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)

    def create(self, request, device_id=None):
        data = request.data.copy()  # Create a mutable copy of request.data
        data['device'] = device_id  # Set device ID in data

        serializer = SensorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, device_id=None, pk=None):
        try:
            sensor = Sensor.objects.get(device_id=device_id, pk=pk)
        except Sensor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)

    def update(self, request, device_id=None, pk=None):
        try:
            sensor = Sensor.objects.get(device_id=device_id, pk=pk)
        except Sensor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = SensorSerializer(sensor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, device_id=None, pk=None):
        try:
            sensor = Sensor.objects.get(device_id=device_id, pk=pk)
        except Sensor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        sensor.delete()
        return Response({"status": "success", "message": "Sensor deleted"}, status=status.HTTP_200_OK)
