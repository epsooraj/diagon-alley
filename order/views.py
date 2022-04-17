from rest_framework import viewsets, generics

from . import models as order_models
from . import serializers as order_serializers


class OrderViewSet(viewsets.ModelViewSet):
    # queryset = order_models.Order.objects.filter(user)
    serializer_class = order_serializers.OrderSerializer\


    def get_queryset(self):
        # if user is admin return all else return corresponding user's order
        if self.request.user.is_staff:
            return order_models.Order.objects.all()
        else:
            return order_models.Order.objects.filter(user__user_id=self.request.user)
