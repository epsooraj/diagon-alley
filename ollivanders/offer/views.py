from django.utils import timezone
from rest_framework import viewsets, views
from rest_framework import permissions
from rest_framework.response import Response

from . import serializers
from . import models


class CouponViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CouponSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.Coupon.objects.all()


class CouponValidationView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        coupon = request.data.get('coupon')
        if not coupon:
            return Response({'detail': 'Coupon not provided'}, status=400)

        coupon_obj = models.Coupon.objects.filter(
            coupon=coupon,
            active=True,
            valid_from__lte=timezone.now(),
            valid_to__gte=timezone.now()
        ).first()

        if not coupon_obj:
            return Response({'detail': 'Coupon not found'}, status=400)

        return Response({'discount': coupon_obj.discount})
