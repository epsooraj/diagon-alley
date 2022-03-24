from rest_framework import serializers

from . import models


class PostalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostalCode
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    postal_code = serializers.CharField()

    class Meta:
        model = models.Address
        fields = '__all__'

    def create(self, validated_data):
        postal_code_data = validated_data.pop('postal_code')
        postal_code_obj = models.PostalCode.objects.get_or_create(
            postal_code=postal_code_data)[0]

        address = models.Address.objects.create(
            postal_code=postal_code_obj, **validated_data)
        return address
