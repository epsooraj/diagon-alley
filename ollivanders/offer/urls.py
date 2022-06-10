from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('coupon', views.CouponViewSet, basename='coupon')

urlpatterns = [
    path('coupon/validate/', views.CouponValidationView.as_view(),
         name='coupon-validate'),
    path('', include(router.urls)),
]
