from django.db import models
from category import models as category_models


class Product(models.Model):
    name = models.CharField(max_length=255)
    name_2 = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        to=category_models.Category, on_delete=models.CASCADE, related_name="category")
    sub_category = models.ForeignKey(
        to=category_models.Category, on_delete=models.CASCADE, related_name="sub_category")

    def __str__(self):
        return str(self.name)

    def get_price(self):
        return self.price - (self.price * self.discount_percentage)

    def get_discount(self):
        return self.price * self.discount_percentage

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('name',)


class Unit(models.Model):
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name="units")

    unit = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    price = models.FloatField()
    discount_percentage = models.FloatField(default=0)

    stock = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.value) + " " + str(self.unit)

    class Meta:
        db_table = 'units'
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
        ordering = ('value',)
