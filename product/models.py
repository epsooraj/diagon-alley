from django.db import models
from category import models as category_models


class Product(models.Model):
    name = models.CharField(max_length=255)
    name_2 = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True)
    price = models.FloatField()
    discount_percentage = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

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
