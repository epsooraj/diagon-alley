from rest_framework import viewsets
from rest_framework.response import Response

from . import serializers
from . import models
from cart import models as cart_models
from address import models as address_models


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return models.Order.objects.all()

        user = models.OrderUser.objects.filter(
            user_id=self.request.user.id).first()

        if user:
            return models.Order.objects.filter(user=user)

        return models.Order.objects.none()

    def create(self, request, *args, **kwargs):
        user = request.user
        address = request.data.get('address')

        if not user.is_authenticated:
            return Response({'detail': 'User not authenticated'}, status=401)

        if not address:
            return Response({'detail': 'Address not provided'}, status=400)

        cart_objs = cart_models.Cart.objects.filter(user=user)

        if len(cart_objs) == 0:
            return Response({'detail': 'Cart not found'}, status=400)

        address_obj = address_models.Address.objects.filter(
            user=user.id, id=address).first()

        if not address_obj:
            return Response({'detail': 'Address not found'}, status=400)

        order_user_address_obj = models.OrderUserAddress.objects.get_or_create(
            name=address_obj.name,
            address=address_obj.address,
            city=address_obj.city,
            state=address_obj.state,
            country=address_obj.country,
            postal_code=address_obj.postal_code.postal_code,
            lat=address_obj.lat,
            lng=address_obj.lng,
        )[0]

        order_user_obj = models.OrderUser.objects.get_or_create(
            user_id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone=user.phone,
            address=order_user_address_obj,
        )[0]

        order_obj = models.Order.objects.create(
            user=order_user_obj,
            total_product_price=0,
            total_price=0,
        )

        for cart_obj in cart_objs:
            order_product_obj = models.OrderProduct.objects.create(
                order=order_obj,
                product=cart_obj.product,
                quantity=cart_obj.quantity,

                name=cart_obj.product.name,
                name_2=cart_obj.product.name_2,
                description=cart_obj.product.description,

                category=cart_obj.product.category,
                sub_category=cart_obj.product.sub_category,
            )

            order_product_unit_obj = models.OrderProductUnit.objects.create(
                product=order_product_obj,
                product_unit=cart_obj.unit,

                quantity=cart_obj.quantity,

                price=cart_obj.unit.price,
                discount_percentage=cart_obj.unit.discount_percentage,
            )

            for unit_image_objs in cart_obj.unit.unit_images.all():
                models.OrderProductUnitImage.objects.create(
                    unit=order_product_unit_obj,
                    image=unit_image_objs.image,
                )

            discounted_price = order_product_unit_obj.price - (
                order_product_unit_obj.price * order_product_unit_obj.discount_percentage / 100)

            order_obj.total_product_price += discounted_price * cart_obj.quantity

        order_obj.save()
