from rest_framework import serializers
from .models import Client, PointsHistoric


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class PointsHistoricSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointsHistoric
        fields = '__all__'
