from rest_framework import serializers

from user import models as user_models


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.CustomUser
        fields = ('id', 'phone', 'email', 'first_name', 'last_name',)


class UserSerializer(serializers.ModelSerializer):

    date_joined = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = user_models.CustomUser
        fields = ('id', 'phone', 'email', 'first_name', 'last_name',
                  'is_staff', 'is_active', 'date_joined',)


class CreateUserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = user_models.CustomUser
        fields = ('id', 'phone', 'email', 'first_name', 'last_name',
                  'is_staff', 'is_active', 'date_joined', 'password',)

    def create(self, validated_data):
        user = user_models.CustomUser.objects.create_user(**validated_data)
        return user
