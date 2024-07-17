from django.shortcuts import render
from database.models import producto, factura_compra, factura_unidad
from django.contrib import messages


def homepage(request):
    try:
        productos=producto.objects.all()
        proRe=[]
    except Exception as e:
        messages.error(request,'error: '+str(e))
        productos = []
        proRe = []
    return render(request,'html/StoreBicycle/index.html', {'productos': productos,'recurrentes': proRe})