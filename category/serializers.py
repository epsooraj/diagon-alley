from rest_framework import serializers

from . import models as category_models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category_models.Category
        fields = "__all__"
