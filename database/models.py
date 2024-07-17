from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class user(AbstractUser):
    ciudad = models.CharField(max_length=30, null=True, blank=True)
    direccion = models.CharField(max_length=40, null=True, blank=True)
    codLogin = models.CharField(max_length=30, null=True, blank=True)


class producto(models.Model):
    ID_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250, null=True, blank=True)
    category = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='imageProd', null=True, blank=True)
    stock = models.IntegerField()
    precio_unitario = models.IntegerField()
    calificacion = models.IntegerField(null=True, blank=True)
    descuento = models.IntegerField(null=True, blank=True)


class factura_compra(models.Model):
    ID_facPro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, default="juan")
    apellido = models.CharField(max_length=60, default="juan")
    correo = models.EmailField(null=False, blank=False, default="juan@gmail.com")
    direccion = models.CharField(max_length=40, default="cll")
    ciudad = models.CharField(max_length=20, default="city")
    telefono = models.CharField(max_length=20, default="111111")
    estado = models.CharField(max_length=20)
    fecha = models.DateField(default=timezone.now)
    forma_pago = models.CharField(max_length=20, null=True, blank=True)

    # llaves foraneas
    Id_cliecte = models.ForeignKey(user, null=True, blank=True, on_delete=models.CASCADE)


class factura_unidad(models.Model):
    ID_factura = models.AutoField(primary_key=True)
    valor_compra = models.IntegerField(null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)

    # llaves foraneas
    Id_producto = models.ForeignKey(producto, null=True, blank=True, on_delete=models.CASCADE)
    Id_facturaCompra = models.ForeignKey(factura_compra, null=True, blank=True, on_delete=models.CASCADE)
