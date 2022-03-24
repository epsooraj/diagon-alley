from django.db import models
from product import models as product_models
from user import models as user_models


class Cart(models.Model):
    user = models.ForeignKey(to=user_models.CustomUser,
                             on_delete=models.CASCADE, related_name='carts')

    product = models.ForeignKey(
        to=product_models.Product, on_delete=models.CASCADE, related_name='carts')
    unit = models.ForeignKey(to=product_models.Unit,
                             on_delete=models.CASCADE, related_name='carts')

    quantity = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return str(self.user)
