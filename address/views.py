from rest_framework import viewsets

from . import serializers


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AddressSerializer

    def get_queryset(self):
        return self.request.user.addresses.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
