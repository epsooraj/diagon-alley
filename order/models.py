from django.db import models


class Order(models.Model):
    order_id = models.CharField(verbose_name="Order Id", max_length=255)

    total_product_price = models.FloatField(verbose_name="Total Product Price")
    total_price = models.FloatField(verbose_name="Total Price")
