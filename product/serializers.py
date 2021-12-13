from rest_framework import serializers

from . import models as product_models
from category import serializers as category_serializers


class ProductSerializer(serializers.Serializer):

    category = category_serializers.CategorySerializer(read_only=True)
    sub_category = category_serializers.CategorySerializer(read_only=True)

    class Meta:
        model = product_models.Product
        fields = "__all__"
