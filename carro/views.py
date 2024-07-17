from ast import Return
from django.shortcuts import render, redirect
from database.models import producto
from django.contrib import messages
from carro.carro import carro as carroshop
from database.models import producto as Productos
from shopp.views import registrarCompras


def carrito(request):
    if request.user.is_authenticated:
        return render(request, 'html/carrito/shopping_car.html')
    else:
        messages.add_message(request=request,level=messages.INFO ,message="inicia sesion primero" )
        return redirect("register")

def agregar_producto(request,producto_id):
    if request.user.is_authenticated:
        car=carroshop(request)
        producto=Productos.objects.get(ID_producto=producto_id)
        car.agregar(producto)
        messages.add_message(request=request,level=messages.SUCCESS ,message="producto agregado" )
        return render(request, 'html/carrito/shopping_car.html')
    messages.add_message(request=request,level=messages.ERROR ,message="inicia sesion primero" )
    return redirect("register")

def restar(request,producto_id):
    car=carroshop(request)
    producto=Productos.objects.get(ID_producto=producto_id)
    car.restar(producto)
    return render(request, 'html/carrito/shopping_car.html')

def eliminar(request,producto_id):
    car=carroshop(request)
    producto=Productos.objects.get(ID_producto=producto_id)
    car.eliminar(producto)
    return render(request, 'html/carrito/shopping_car.html')


def limpiar(request):
    car=carroshop(request=request)
    car.limpiarcarrito()
    messages.add_message(request=request,level=messages.INFO ,message=str(car) )
    return render(request, 'html/carrito/shopping_car.html')

def comprar(request):
    car=carroshop(request=request)
    llaves=car.devolver_datos()
    registrarCompras(request,llaves)
