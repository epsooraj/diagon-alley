from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/v1/', include([
        path('user/', include('user.urls')),
        path('address/', include('address.urls')),
        path('product/', include('product.urls')),
        path('category/', include('category.urls')),
        path('cart/', include('cart.urls')),
        path('order/', include('order.urls')),
    ])),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
