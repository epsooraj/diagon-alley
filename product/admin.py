from django.contrib import admin
import nested_admin

from . import models


class UnitImageInline(nested_admin.NestedStackedInline):
    model = models.UnitImage
    extra = 0


class UnitAdminInline(nested_admin.NestedTabularInline):
    inlines = [
        UnitImageInline,
    ]
    model = models.Unit
    extra = 0


class ProductAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        UnitAdminInline,
    ]


admin.site.register(models.Product, ProductAdmin)
