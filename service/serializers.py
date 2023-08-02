from rest_framework import serializers
from .models import ServiceType, Service

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ['id', 'name', 'created_at', 'updated_at']
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'owner', 'title', 'description', 'price', 'region', 'district', 'address', 'phone_number', 'additional_phone_number', 'telegram', 'instagram', 'youtube', 'created_at', 'updated_at']