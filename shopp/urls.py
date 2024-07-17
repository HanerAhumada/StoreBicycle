import imp
from django.urls import path, include
from .views import *
from shopp import views
app_name='shopp'
urlpatterns=[
    path('',registrarCompras,name='comprar'),
]