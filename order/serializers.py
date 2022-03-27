from rest_framework import serializers

from . import models


class OrderUserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderUserAddress
        fields = '__all__'


class OrderUserSerializer(serializers.ModelSerializer):
    address = OrderUserAddressSerializer(read_only=True)

    class Meta:
        model = models.OrderUser
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderProduct
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True, read_only=True)
    user = OrderUserSerializer(read_only=True)

    class Meta:
        model = models.Order
        fields = '__all__'
