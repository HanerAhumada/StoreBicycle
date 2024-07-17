from django.urls import path
from carro.views import *
app_name='carro'
urlpatterns = [
    path('', carrito,name='carrito'),
    path('agregarProducto/<int:producto_id>/', agregar_producto,name='agregar'),
    path('eliminarProducto/<int:producto_id>/', eliminar,name='eliminar'),
    path('restarProducto/<int:producto_id>/', restar,name='restar'),
    path('limpiar/', limpiar,name='limpiar'),
    path('comprar/', comprar, name='comprar')
]