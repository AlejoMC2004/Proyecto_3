from rest_framework import serializers

from .models import Campeon

class CampeonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campeon
        fields = ['id', 'nombre', 'rasgo_1', 'rasgo_2', 'coste', 'region']