from django.shortcuts import render, redirect
from database.models import producto
from .FormsData import formsFiltro as FiltroOptions
from django.contrib import messages

encoding = "utf-8"


# Create your views here.


def inventario(request, filtro):
    products = None

    print(request.method+'  '+filtro )
    if request.method == "GET":
        if filtro != 'all':
            products = producto.objects.filter(category=filtro)
        elif filtro == 'all':
            products = producto.objects.all()
    elif request.method == "POST":
        Filtro_Data = FiltroOptions(request.POST)
        if Filtro_Data.is_valid():
            precio = eval(Filtro_Data.cleaned_data['precio'])
            categoria = Filtro_Data.data['categoria']
            subcategoria = Filtro_Data.data['subcategoria']

            products = producto.objects.all()
            if precio[0] != '':
                products = products.filter(precio_unitario__gte=int(precio[0]))
            if precio[1] != '':
                products = products.filter(precio_unitario__lte=int(precio[1]))

    return render(request, 'html/Tienda/tienda.html', {'products': products, 'filtro': FiltroOptions})


def ver_producto(request, productoid):
    productoUni = producto.objects.filter(ID_producto=productoid)
    if productoUni:
        return render(request, 'html/Tienda/producto.html', {'productos': productoUni})
    return redirect("tienda")
