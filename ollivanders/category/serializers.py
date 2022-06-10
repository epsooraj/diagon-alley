from rest_framework import serializers

from . import models as category_models


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = category_models.Category
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    sub_categories = SubCategorySerializer(many=True)

    class Meta:
        model = category_models.Category
        fields = "__all__"
