from rest_framework.routers import DefaultRouter
from .views import RegionViewSet, DistrictViewSet

router = DefaultRouter()
router.register('regions', RegionViewSet, basename='regions')
router.register('districts', DistrictViewSet, basename='districts')
urlpatterns = router.urls