from rest_framework import viewsets

from . import models as product_models
from . import serializers as product_serializers


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = product_models.Product.objects.all()
    serializer_class = product_serializers.ProductSerializer
