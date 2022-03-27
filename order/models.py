from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from category import models as category_models
from product import models as product_models


class OrderUserAddress(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    postal_code = models.CharField(max_length=200)

    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'order_user_address'
        verbose_name = 'Order User Address'
        verbose_name_plural = 'Order User Addresses'


class OrderUser(models.Model):
    user_id = models.IntegerField()

    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    email = models.EmailField(_('email address'))
    phone = models.CharField(_('phone'), max_length=20, blank=True,)

    address = models.ForeignKey(
        to=OrderUserAddress, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'order_user'
        verbose_name = 'Order User'
        verbose_name_plural = 'Order Users'


class Order(models.Model):
    order_id = models.CharField(verbose_name="Order Id", max_length=255)

    user = models.ForeignKey(OrderUser, on_delete=models.CASCADE)

    total_product_price = models.FloatField(verbose_name="Total Product Price")
    total_price = models.FloatField(verbose_name="Total Price")

    created_at = models.DateTimeField(
        verbose_name="Created At", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name="Updated At", auto_now=True)

    def __str__(self):
        return self.order_id

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_products")
    quantity = models.IntegerField(verbose_name="Quantity")

    product = models.ForeignKey(
        product_models.Product, on_delete=models.CASCADE, related_name="order_products")

    name = models.CharField(max_length=255)
    name_2 = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        to=category_models.Category, on_delete=models.SET_NULL, related_name="order_category", null=True)
    sub_category = models.ForeignKey(
        to=category_models.Category, on_delete=models.SET_NULL, related_name="order_sub_category", null=True)

    def __str__(self):
        return f'{str(self.name)} {str(self.order)}'

    class Meta:
        db_table = 'order_product'
        verbose_name = 'Order Product'
        verbose_name_plural = 'Order Products'
