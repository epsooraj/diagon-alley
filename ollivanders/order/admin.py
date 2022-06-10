from django.contrib import admin
import nested_admin

from . import models


class OrderProductUnitImage(nested_admin.NestedStackedInline):
    model = models.OrderProductUnitImage
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OrderProductUnit(nested_admin.NestedTabularInline):
    model = models.OrderProductUnit
    inlines = [
        OrderProductUnitImage,
    ]
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OrderProduct(nested_admin.NestedTabularInline):
    model = models.OrderProduct
    inlines = [
        OrderProductUnit,
    ]
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OrderUserAddress(nested_admin.NestedStackedInline):
    model = models.OrderUserAddress
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# class OrderUser(nested_admin.NestedStackedInline):
#     model = models.OrderUser
#     inlines = [
#         OrderUserAddress,
#     ]
#     extra = 0


class OrderAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        OrderProduct,
        # OrderUser,
    ]

    readonly_fields = ('order_id', 'user',
                       'total_product_price', 'total_price',)

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(models.Order, OrderAdmin)
