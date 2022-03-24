from rest_framework import serializers

from user import models as user_models


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.CustomUser
        fields = ('id', 'phone', 'email', 'first_name', 'last_name',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.CustomUser
        fields = ('id', 'phone', 'email', 'first_name', 'last_name',
                  'is_staff', 'is_active', 'date_joined',)


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.CustomUser
        fields = ('id', 'phone', 'email', 'first_name', 'last_name',
                  'is_staff', 'is_active', 'date_joined',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = user_models.CustomUser.objects.create_user(**validated_data)
        return user
