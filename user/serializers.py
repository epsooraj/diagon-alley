from rest_framework import serializers

from user import models as user_models


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.CustomUser
        fields = ('id', 'phone', 'email', 'first_name', 'last_name',)
