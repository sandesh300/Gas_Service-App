# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.accounts.urls')),
    path('service-requests/', include('apps.service_requests.urls', namespace='service_requests')),  # Add namespace here
    # path('tracking/', include('apps.tracking.urls')),
    # path('support/', include('apps.support_portal.urls', namespace='support')),  # Add namespace if you plan to use this
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)