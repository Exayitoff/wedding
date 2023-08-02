from django.urls import path
from .views import ServiceTypeList, ServiceList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('service-types', ServiceTypeList, basename='service-types')
router.register('services', ServiceList, basename='services')
urlpatterns = router.urls   