from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sensor_data.views import SensorDataViewSet, blink_led, control_fan  # Import control_fan
from django.contrib import admin

router = DefaultRouter()
router.register(r'sensor-data', SensorDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/blink-led/', blink_led),  # Endpoint to handle LED blink request
    path('api/control-fan/', control_fan, name='control_fan'),
    path('api/auth/', include('sensor_data.urls')),
    path('custom-admin/', admin.site.urls),  # Admin interface at /custom-admin/
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/social/', include('dj_rest_auth.registration.urls')),  # Social login URLs
    path('auth/', include('social_django.urls', namespace='social')),
]
