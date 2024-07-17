from urllib.request import Request
from django.shortcuts import redirect, render
from shopp.shopp import shoppUser
from carro.carro import carro as carroshop


# Create your views here.

def registrarCompras(request):
    if request.user.is_authenticated:
        car = carroshop(request=request)
        llaves = car.devolver_datos()
        if request.method == "POST":
            ciudad = request.POST['ciudad']
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            correo = request.POST['correo']
            telefono = request.POST['telefono']
            direccion = request.POST['direccion']
            compra = shoppUser()
            compra.crear_factura(request.user, llaves, ciudad=ciudad, nombre=nombre, apellido=apellido, correo=correo,
                                 telefono=telefono, direccion=direccion)
            return redirect('homepage')
        return render(request, 'html/shopp/compras.html')
