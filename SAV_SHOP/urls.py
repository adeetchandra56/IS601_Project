from django.urls import path
from .views import index, cart, checkout
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index, name='index'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])