from rest_framework import serializers

from . import models
from user import serializers as user_serializers
from product import serializers as product_serializers


class ListCartSerializer(serializers.ModelSerializer):

    user = user_serializers.SimpleUserSerializer()
    product = product_serializers.ProductSerializer()
    unit = product_serializers.ProductUnitSerializer()

    class Meta:
        model = models.Cart
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = ('product', 'unit', 'quantity')
