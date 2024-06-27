from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Ilimetr API",
        default_version='v1',
        description="API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('home.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('events/', include('events.urls')),
    path('interactive-elements/', include('interactive_elements.urls')),
    path('reports/', include('reports.urls')),
    path('meetings/', include('meetings.urls')),
    path('courses/', include('courses.urls')),
    path('notifications/', include('notifications.urls')),
    path('departments/', include('departments.urls')),
    path('api-courses/', include('courses.api_urls')),
    path('api-departments/', include('departments.api_urls')),
    path('api-interactive-elements/', include('interactive_elements.api_urls')),
    path('api-meetings/', include('meetings.api_urls')),
    path('api-notifications/', include('notifications.api_urls')),
    path('api-users/', include('users.api_urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]