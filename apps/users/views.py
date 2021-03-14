from apps.users.serializers import UserSerializer

from django.contrib.auth import get_user_model
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
