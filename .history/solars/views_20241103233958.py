from rest_framework import viewsets
from .models import Solars, Output
from .serializers import SolarsSerializer, OutputSerializer

class SolarsViewSet(viewsets.ModelViewSet):
    queryset = Solars.objects.all()
    serializer_class = SolarsSerializer

class OutputViewSet(viewsets.ModelViewSet):
    queryset = Output.objects.all()
    serializer_class = OutputSerializer
