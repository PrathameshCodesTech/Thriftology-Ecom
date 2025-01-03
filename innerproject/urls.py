from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('customer/', include('customer.urls')),
    path('product/', include('product.urls')),
    path('customer/', include('customer.urls')),
    path('bidding/', include('bidding.urls')),
    
]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)