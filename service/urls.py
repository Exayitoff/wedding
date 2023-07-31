from django.urls import path
from .views import ServiceList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ServiceList, basename='service')
urlpatterns = router.urls