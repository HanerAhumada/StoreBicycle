from django.urls import path
from .views import *

app_name = 'shopp'
urlpatterns = [
    path('', registrarCompras, name='comprar'),
]
