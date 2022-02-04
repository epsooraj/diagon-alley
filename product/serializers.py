from rest_framework import serializers

from . import models as product_models
from category import serializers as category_serializers


class ProductUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_models.Unit
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    category = category_serializers.CategorySerializer(read_only=True)
    sub_category = category_serializers.CategorySerializer(read_only=True)
    units = ProductUnitSerializer(many=True, read_only=True)

    class Meta:
        model = product_models.Product
        fields = '__all__'
