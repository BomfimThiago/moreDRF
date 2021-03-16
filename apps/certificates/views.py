from apps.certificates.serializers import CertificateSerializer

from apps.certificates.models import Certificate
from rest_framework import viewsets


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
