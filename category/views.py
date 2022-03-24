from rest_framework import viewsets
from rest_framework import permissions

from . import models as category_models
from . import serializers as category_serializers


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny]
    queryset = category_models.Category.objects.all()
    serializer_class = category_serializers.CategorySerializer
