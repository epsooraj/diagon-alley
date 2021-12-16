from django.db import models

from user import models as user_models


class PostalCode(models.Model):
    """
    PostalCode model
    """
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return str(self.postal_code)


class Address(models.Model):
    """
    Address model
    """
    user = models.ForeignKey(to=user_models.CustomUser,
                             on_delete=models.CASCADE, related_name='addresses')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    postal_code = models.ForeignKey(
        to=PostalCode,
        on_delete=models.SET_NULL,
        verbose_name='Postal Code',
        related_name='addresses',
        null=True,
    )

    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    def __str__(self):
        return self.name
