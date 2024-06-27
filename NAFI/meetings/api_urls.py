from rest_framework.routers import DefaultRouter
from .api_views import MeetingViewSet

router = DefaultRouter()
router.register(r'meetings', MeetingViewSet)

urlpatterns = router.urls