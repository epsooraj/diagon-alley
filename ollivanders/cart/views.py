from rest_framework import viewsets

from . import serializers
from . import models


class CartViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.ListCartSerializer
        return serializers.CartSerializer

    def get_queryset(self):
        return models.Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
