from rest_framework.routers import DefaultRouter
from .views import RegionList, DistrictList

router = DefaultRouter()
router.register('region', RegionList, basename='region')
router.register('district', DistrictList, basename='district')
urlpatterns = router.urls