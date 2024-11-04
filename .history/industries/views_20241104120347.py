from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Datasheet
from .serializers import DatasheetSerializer

class DatasheetViewSet(viewsets.ViewSet):
    def list(self, request, device_id=None):
        datasheets = Datasheet.objects.filter(device_id=device_id)
        serializer = DatasheetSerializer(datasheets, many=True)
        return Response(serializer.data)

    def create(self, request, device_id=None):
        data = request.data.copy()
        data['device'] = device_id

        serializer = DatasheetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, device_id=None, pk=None):
        try:
            datasheet = Datasheet.objects.get(device_id=device_id, pk=pk)
        except Datasheet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DatasheetSerializer(datasheet)
        return Response(serializer.data)

    def update(self, request, device_id=None, pk=None):
        try:
            datasheet = Datasheet.objects.get(device_id=device_id, pk=pk)
        except Datasheet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data = request.data.copy()
        serializer = DatasheetSerializer(datasheet, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, device_id=None, pk=None):
        try:
            datasheet = Datasheet.objects.get(device_id=device_id, pk=pk)
        except Datasheet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        datasheet.delete()
        return Response({"status": "success", "message": "Datasheet deleted"}, status=status.HTTP_200_OK)


class IncidentsViewSet(viewsets.ModelViewSet):
    queryset = Incidents.objects.all()
    serializer_class = IncidentsSerializer