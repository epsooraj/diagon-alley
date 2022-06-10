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
    products = OrderProductSerializer(many=True, read_only=True)
    user = OrderUserSerializer(read_only=True)

    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(OrderSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = models.Order
        fields = '__all__'
