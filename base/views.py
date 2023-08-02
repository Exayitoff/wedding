from rest_framework import viewsets
from .serializers import RegionSerializer, DistrictSerializer
from .models import Region, District

# Create your views here.

class RegionList(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    
class DistrictList(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer