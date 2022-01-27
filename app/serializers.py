from rest_framework import serializers
from .models import Insert


class InsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insert
        fields = '__all__'
