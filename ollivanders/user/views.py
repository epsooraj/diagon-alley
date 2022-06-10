from rest_framework import generics, viewsets
from rest_framework import permissions

from . import models
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'DELETE']:
            return (permissions.IsAdminUser(),)
        return (permissions.IsAuthenticated(),)

    def get_queryset(self):
        if self.request.user.is_staff:
            return models.CustomUser.objects.all()

        return models.CustomUser.objects.filter(id=self.request.user.id)


class CreateUserView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.CreateUserSerializer
    query_set = models.CustomUser.objects.all()
