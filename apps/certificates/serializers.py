from rest_framework import serializers

from apps.certificates.models import Certificate


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate()
        fields = ('id', 'name', 'created_at', 'updated_at')

    def create(self, validated_data):
        return Certificate.objects.create_user(**validated_data)
