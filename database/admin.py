from django.contrib import admin
from database.models import user, producto, factura_unidad, factura_compra
from .forms import UploadExcelForm
import pandas as pd
from django.urls import path
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
import os

# Definir una clase de administración personalizada para el modelo 'user'
class userAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'ciudad', 'direccion')
    search_fields = ("username", "email", "ciudad", "direccion")
    list_filter = ("is_staff", 'is_active', 'ciudad')

# Definir una clase de administración personalizada para el modelo 'producto'
class prodAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'category', 'stock', 'precio_unitario', 'calificacion', 'descuento')
    search_fields = ("nombre_producto", "category")
    list_filter = ('category', 'stock', 'precio_unitario', 'calificacion', 'descuento')

    change_list_template = "admin/producto_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-excel/', self.admin_site.admin_view(self.upload_excel), name='upload_excel'),
        ]
        return custom_urls + urls

    def upload_excel(self, request):
        if request.method == 'POST':
            form = UploadExcelForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES['file']
                df = pd.read_excel(file)
                productos = []
                for index, row in df.iterrows():
                    prod = producto(
                        nombre_producto=row['nombre_producto'],
                        category=row['category'],
                        stock=row['stock'],
                        precio_unitario=row['precio_unitario'],
                        calificacion=row.get('calificacion', None),
                        descuento=row.get('descuento', None),
                        descripcion=row['descripcion'],
                    )
                    # Asignar la imagen si está presente en el archivo Excel
                    if 'imagen' in df.columns:
                        # Obtiene el nombre del archivo de la ruta completa
                        filename = os.path.basename(row['imagen'])
                        # Guarda el archivo en el campo imagen del producto
                        prod.imagen.save(filename, ContentFile(open(row['imagen'], 'rb').read()), save=False)

                    productos.append(prod)

                producto.objects.bulk_create(productos)
                self.message_user(request, "Datos subidos correctamente.")
                return redirect("..")
        else:
            form = UploadExcelForm()
        return render(request, 'admin/upload_excel.html', {'form': form})

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['upload_form'] = UploadExcelForm()
        return super().changelist_view(request, extra_context=extra_context)

    def render_change_form(self, request, context, *args, **kwargs):
        if not 'upload_form' in context:
            context['upload_form'] = UploadExcelForm()
        return super().render_change_form(request, context, *args, **kwargs)



# Definir una clase de administración personalizada para el modelo 'factura_compra'
class factAdmin(admin.ModelAdmin):
    list_display = ('ID_facPro', 'nombre', 'apellido', 'correo', 'direccion', 'ciudad', 'telefono', 'estado', 'fecha', 'forma_pago', 'Id_cliecte')
    search_fields = ('ID_facPro', 'nombre', 'apellido', 'correo', 'direccion', 'ciudad', 'telefono', 'estado', 'forma_pago', 'Id_cliecte__username')
    list_filter = ('estado', 'fecha', 'ciudad', 'forma_pago')




# Definir una clase de administración personalizada para el modelo 'factura_unidad'
class factAdminProd(admin.ModelAdmin):
    list_display = ('ID_factura', 'valor_compra', 'cantidad', 'Id_producto', 'Id_facturaCompra')
    search_fields = ("ID_factura", "valor_compra", "cantidad", 'Id_producto__nombre_producto', 'Id_facturaCompra__ID_facPro')
    list_filter = ('valor_compra', 'cantidad')

# Registrar los modelos en el sitio de administración usando las clases de administración personalizadas
admin.site.register(user, userAdmin)
admin.site.register(producto, prodAdmin)
admin.site.register(factura_compra, factAdmin)
admin.site.register(factura_unidad, factAdminProd)
