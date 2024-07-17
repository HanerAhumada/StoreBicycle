from django.urls import path, include
from django.contrib.auth.urls import urlpatterns
from login.views import logueando

app_name='accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]