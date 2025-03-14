from django.shortcuts import render
from database.models import producto, factura_compra, factura_unidad
from django.contrib import messages


def homepage(request):
    products = producto.objects.all()
    pro_re = []
    return render(request, 'html/StoreBicycle/index.html', {'productos': products, 'recurrentes': pro_re})
