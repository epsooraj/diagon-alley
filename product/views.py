from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions

from . import models as product_models
from . import serializers as product_serializers
from category import models as category_models


class ProductViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = product_models.Product.objects.all()
    serializer_class = product_serializers.ProductSerializer

    def check_and_set_fields(self, request):
        """
        Check if all required fields are present
        """
        error = False
        msg = {}

        data = {}

        name = request.data.get('name')
        name_2 = request.data.get('name_2')
        description = request.data.get('description', "")
        category = request.data.get('category')
        sub_category = request.data.get('sub_category')
        units = request.data.get('units')

        # Check if all required fields are present
        if not name:
            error = True
            msg['name'] = ['Name field is required']
        if not category:
            error = True
            msg['category'] = ['Category field is required']
        else:
            category_obj = category_models.Category.objects.get(id=category)

        if not sub_category:
            error = True
            msg['sub_category'] = ['Sub Category field is required']
        else:
            sub_category_obj = category_models.Category.objects.get(
                id=sub_category)
        if not units:
            error = True
            msg['units'] = ['Units field is required']

        data = {
            'name': name,
            'name_2': name_2,
            'description': description,
            'category': category_obj,
            'sub_category': sub_category_obj,
            'units': units
        }

        return error, msg, data

    def create(self, request, *args, **kwargs):
        """
        Add new products with units
        params: name, name_2, units, description, category, sub_category
                units: [{unit, value, price, discount_percentage, stock, images: []}]
        """

        error, msg, data = self.check_and_set_fields(request)

        if error:
            return Response({'error': msg}, status=status.HTTP_400_BAD_REQUEST)

        product_obj = product_models.Product.objects.create(
            name=data['name'], name_2=data['name_2'], description=data['description'], category=data['category'], sub_category=data['sub_category'])

        for unit in data['units']:
            unit_obj = product_models.Unit.objects.create(
                product=product_obj, **unit)

            for image in unit['images']:
                product_models.UnitImage.objects.create(
                    unit=unit_obj, image=image)

        serializer = product_serializers.ProductSerializer(product_obj)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """
        Update product with units
        params: name, name_2, units, description, category, sub_category
                units: [{unit, value, price, discount_percentage, stock}]
        """

        name = request.data.get('name')
        name_2 = request.data.get('name_2')
        description = request.data.get('description', "")
        category = request.data.get('category')
        sub_category = request.data.get('sub_category')
        units = request.data.get('units')

        product_obj = product_models.Product.objects.get(id=kwargs['pk'])

        if name:
            product_obj.name = name
        if name_2:
            product_obj.name_2 = name_2
        if description:
            product_obj.description = description
        if category:
            product_obj.category = category
        if sub_category:
            product_obj.sub_category = sub_category

        product_obj.save()

        # product_all_existing_units = product_models.Unit.objects.filter(
        #     product=product_obj)

        if units:
            for unit in units:
                if unit['id']:
                    unit_obj = product_models.Unit.objects.get(
                        id=unit['id'])
                    unit_obj = product_models.Unit.objects.get(id=unit['id'])

                    if unit['unit']:
                        unit_obj.unit = unit['unit']
                    if unit['value']:
                        unit_obj.value = unit['value']
                    if unit['price']:
                        unit_obj.price = unit['price']
                    if unit['discount_percentage']:
                        unit_obj.discount_percentage = unit['discount_percentage']
                    if unit['stock']:
                        unit_obj.stock = unit['stock']

                    unit_obj.save()

                    # Check if there are new images
                    if unit['images']:
                        for image in unit['images']:
                            if image['id']:
                                unit_image_obj = product_models.UnitImage.objects.get(
                                    id=image['id'])
                                unit_image_obj.image = image['image']
                                unit_image_obj.save()
                            else:
                                product_models.UnitImage.objects.create(
                                    unit=unit_obj, image=image['image'])
                else:
                    unit_obj = product_models.Unit.objects.create(
                        product=product_obj, **unit)

                    for image in unit['images']:
                        product_models.UnitImage.objects.create(
                            unit=unit_obj, image=image)

        serializer = product_serializers.ProductSerializer(product_obj)

        return Response(serializer.data, status=status.HTTP_200_OK)
