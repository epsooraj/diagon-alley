from django.contrib import admin

from . import models

admin.site.register(models.PostalCode)
admin.site.register(models.Address)
