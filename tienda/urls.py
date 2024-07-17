from urllib import request
from django.urls import path
from . import views

app_name='shopping'

urlpatterns = [
    path("<str:filtro>/", views.inventario, name='tienda'),
    path("consultar/<int:productoid>/", views.ver_producto, name='producto'),
]
