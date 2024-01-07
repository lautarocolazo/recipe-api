from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
# from .views import MyTokenObtainPairView
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
    path('api/user/', include('user.urls')),
    path('api/department/', include('department.urls')),
    path('api/position/', include('job_position.urls')),
    path('api/rating/', include('rating.urls')),
]
