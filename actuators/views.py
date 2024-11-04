from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Actuator
from .serializers import ActuatorSerializer

class ActuatorViewSet(viewsets.ViewSet):
    def list(self, request, device_id=None):
        actuators = Actuator.objects.filter(device_id=device_id)
        serializer = ActuatorSerializer(actuators, many=True)
        return Response(serializer.data)

    def create(self, request, device_id=None):
        data = request.data.copy()
        data['device'] = device_id

        serializer = ActuatorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, device_id=None, pk=None):
        try:
            actuator = Actuator.objects.get(device_id=device_id, pk=pk)
        except Actuator.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ActuatorSerializer(actuator)
        return Response(serializer.data)

    def update(self, request, device_id=None, pk=None):
        try:
            actuator = Actuator.objects.get(device_id=device_id, pk=pk)
        except Actuator.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data = request.data.copy()
        serializer = ActuatorSerializer(actuator, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, device_id=None, pk=None):
        try:
            actuator = Actuator.objects.get(device_id=device_id, pk=pk)
        except Actuator.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        actuator.delete()
        return Response({"status": "success", "message": "Actuator deleted"}, status=status.HTTP_200_OK)
