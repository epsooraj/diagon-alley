from rest_framework import viewsets

from . import serializers
from . import models


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CartSerializer

    def get_queryset(self):
        return models.Cart.objects.filter(user=self.request.user)
