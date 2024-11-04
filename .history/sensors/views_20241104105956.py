from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Sensor
from devices.models import Device
from .serializers import SensorSerializer, SensorPredictedSerializer, SensorValuesSerializer

class SensorViewSet(viewsets.ViewSet):
    def list(self, request, device_id=None):
        sensors = Sensor.objects.filter(device_id=device_id)
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)

    def create(self, request, device_id=None):
        data = request.data.copy()
        data['device'] = device_id

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


class SensorValuesViewSet(viewsets.ViewSet):
    def list(self, request, sensor_id=None):
        values = SensorValues.objects.filter(sensor_id=sensor_id)
        serializer = SensorValuesSerializer(values, many=True)
        return Response(serializer.data)

    def create(self, request, sensor_id=None):
        data = request.data.copy()
        data['sensor'] = sensor_id
        serializer = SensorValuesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, sensor_id=None, pk=None):
        try:
            value = SensorValues.objects.get(sensor_id=sensor_id, pk=pk)
        except SensorValues.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SensorValuesSerializer(value)
        return Response(serializer.data)

    def destroy(self, request, sensor_id=None, pk=None):
        try:
            value = SensorValues.objects.get(sensor_id=sensor_id, pk=pk)
        except SensorValues.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        value.delete()
        return Response({"status": "success", "message": "Value deleted"}, status=status.HTTP_200_OK)


class SensorPredictedViewSet(viewsets.ViewSet):
    def list(self, request, device_id=None):
        predicted = SensorPredicted.objects.filter(device_id=device_id)
        serializer = SensorPredictedSerializer(predicted, many=True)
        return Response(serializer.data)

    def create(self, request, device_id=None):
        data = request.data.copy()
        data['device'] = device_id
        serializer = SensorPredictedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, device_id=None, pk=None):
        try:
            prediction = SensorPredicted.objects.get(device_id=device_id, pk=pk)
        except SensorPredicted.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SensorPredictedSerializer(prediction)
        return Response(serializer.data)

    def destroy(self, request, device_id=None, pk=None):
        try:
            prediction = SensorPredicted.objects.get(device_id=device_id, pk=pk)
        except SensorPredicted.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        prediction.delete()
        return Response({"status": "success", "message": "Prediction deleted"}, status=status.HTTP_200_OK)