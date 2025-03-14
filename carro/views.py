from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from database.models import producto as Productos
from carro.carro import carro as carroshop
from shopp.views import registrarCompras
from shopp.views import shoppUser  # Asegúrate de importar shoppUser correctamente


def carrito(request):
    if request.user.is_authenticated:
        return render(request, 'html/carrito/shopping_car.html')
    else:
        messages.error(request, "Inicia sesión primero")
        return redirect("registrer:register")


def agregar_producto(request, producto_id):
    if request.user.is_authenticated:
        car = carroshop(request)
        producto = get_object_or_404(Productos, ID_producto=producto_id)
        car.agregar(producto)
        messages.success(request, "Producto agregado")
        return redirect("carro:carrito")
    messages.error(request, "Inicia sesión primero")
    return redirect("registrer:register")


def restar(request, producto_id):
    if request.user.is_authenticated:
        car = carroshop(request)
        producto = get_object_or_404(Productos, ID_producto=producto_id)
        car.restar(producto)
        return redirect("carro:carrito")
    messages.error(request, "Inicia sesión primero")
    return redirect("registrer:register")


def eliminar(request, producto_id):
    if request.user.is_authenticated:
        car = carroshop(request)
        producto = get_object_or_404(Productos, ID_producto=producto_id)
        car.eliminar(producto)
        return redirect("carro:carrito")
    messages.error(request, "Inicia sesión primero")
    return redirect("registrer:register")


def limpiar(request):
    if request.user.is_authenticated:
        # Consumir mensajes previos para limpiarlos
        list(messages.get_messages(request))
        car = carroshop(request)
        car.limpiarcarrito()
        messages.info(request, "Carrito vaciado")
        return redirect("carro:carrito")
    messages.error(request, "Inicia sesión primero")
    return redirect("registrer:register")


def comprar(request):
    if request.user.is_authenticated:
        # Consumir mensajes previos para que el mensaje nuevo sea el primero
        list(messages.get_messages(request))
        car = carroshop(request)
        llaves = car.devolver_datos()
        if llaves:
            registrarCompras(request)
            messages.success(request, "Compra realizada con éxito")
            car.limpiarcarrito()
            return redirect("carro:carrito")
        else:
            messages.error(request, "No hay productos en el carrito para comprar")
            return redirect("carro:carrito")
    messages.error(request, "Inicia sesión primero")
    return redirect("registrer:register")
