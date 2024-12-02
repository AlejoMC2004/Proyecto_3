# Importar Modelo
from .models import Campeon
from rest_framework import viewsets
from rest_framework.response import Response
from .serial import CampeonSerializer

# Create your views here.
class CampeonViewSet(viewsets.ModelViewSet):
    queryset = Campeon.objects.all().order_by('coste')
    serializer_class = CampeonSerializer
