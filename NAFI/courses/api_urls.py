from rest_framework.routers import DefaultRouter
from .api_views import CourseViewSet, ModuleViewSet, LessonViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'lessons', LessonViewSet)

urlpatterns = router.urls