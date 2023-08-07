from django.urls import path
from .views import ServiceTypeViewSet, ServiceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('service-types', ServiceTypeViewSet, basename='service')
router.register('services', ServiceViewSet, basename='services')
urlpatterns = router.urls   