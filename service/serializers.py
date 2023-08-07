from rest_framework import serializers
from .models import ServiceType, Service
from base.models import Region, District

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = "__all__"
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
    
    
    def validate_district(self, district):
        region = self.initial_data.get('region')
        if region and district:
            if district.region != Region.objects.get(pk=region):
                raise serializers.ValidationError("The area of the district should correspond to the region.")
        return district