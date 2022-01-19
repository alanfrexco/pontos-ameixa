from rest_framework import serializers
from app import models

class InsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Insert
        fields = '__all__'