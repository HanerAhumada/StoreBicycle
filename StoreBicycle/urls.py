
from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from StoreBicycle.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage,name='homepage'),
    path("register/", include('registrer.urls', namespace='register')),
    path('tienda/',include('tienda.urls',namespace='shopping')),
    path('carro/',include('carro.urls', namespace='carro')),
    path('shopp/',include('shopp.urls', namespace='shopp')),
    path('accounts/', include('login.urls', namespace="accounts")),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
