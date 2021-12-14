from django.urls import path, include

from . import views


urlpatterns = [
    path('', view=views.ProductView.as_view(), name='product'),
]
