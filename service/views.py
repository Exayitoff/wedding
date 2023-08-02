from rest_framework import viewsets
from .serializers import ServiceTypeSerializer, ServiceSerializer
from .models import ServiceType, Service

# Create your views here.

class ServiceTypeList(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()    
    serializer_class = ServiceTypeSerializer
    
class ServiceList(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer