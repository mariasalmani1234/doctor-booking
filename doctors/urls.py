from rest_framework.routers import DefaultRouter

from .views import DoctorViewSet, SpecialtyViewSet


router = DefaultRouter()

router.register('doctors', DoctorViewSet, basename='doctor')
router.register('specialties', SpecialtyViewSet, basename='specialty')


urlpatterns = router.urls