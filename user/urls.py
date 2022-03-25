from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('', views.UserViewSet, basename='user')

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('', include(router.urls)),
]
