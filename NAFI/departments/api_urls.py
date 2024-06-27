from rest_framework.routers import DefaultRouter
from .api_views import DepartmentViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)

urlpatterns = router.urls