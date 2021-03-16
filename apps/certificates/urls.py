from django.urls import path, include
from rest_framework import routers
from apps.certificates.views import CertificateViewSet

router = routers.DefaultRouter()
router.register(r'', CertificateViewSet)

urlpatterns = [
    path('', include(router.urls))
]