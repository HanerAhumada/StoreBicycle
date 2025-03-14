from django.shortcuts import redirect, render
from shopp.shopp import shoppUser
from carro.carro import carro as carroshop
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')  # Asegura que solo usuarios autenticados accedan
def registrarCompras(request):
    car = carroshop(request=request)
    llaves = car.devolver_datos()

    if request.method == "POST":
        ciudad = request.POST.get('ciudad')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        compra = shoppUser()
        compra.crear_factura(request.user, llaves, ciudad=ciudad, nombre=nombre, apellido=apellido,
                             correo=correo, telefono=telefono, direccion=direccion)
        return redirect('homepage')

    return render(request, 'html/shopp/compras.html')
