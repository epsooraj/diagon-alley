from rest_framework import views

from . import models as product_models
from . import serializers as product_serializers


class ProductView(views.APIView):
    def get(self, request):
        """
        Return All Products
        """
        pass

    def post(self, request):
        """
        Add new products with units
        """
        pass

    def put(self, request):
        """
        Update product with units
        """
        pass

    def delete(self, request):
        """
        Delete product
        """
        pass
