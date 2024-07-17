from database.models import factura_unidad, factura_compra
from database.models import producto as prd
from carro.carro import carro
class shoppUser():

    def crear_factura(self,user, productoid,ciudad,nombre,apellido,correo,telefono,direccion):
        
        factura_general=factura_compra()
        factura_general.Id_cliecte=user
        factura_general.nombre=nombre
        factura_general.apellido=apellido
        factura_general.correo=correo
        factura_general.telefono=telefono
        factura_general.ciudad=ciudad
        factura_general.direccion=direccion
        factura_general.estado="activo"
        factura_general.forma_pago="tarjeta"
        factura_general.save()

        for productoUnidad in productoid:
            productoU=prd.objects.filter(ID_producto=productoUnidad[0])
            producto=factura_unidad()
            producto.Id_producto=productoU[0]
            producto.Id_facturaCompra=factura_general
            producto.cantidad=productoUnidad[1]
            producto.valor_compra=productoUnidad[2]
            producto.save()
        

        
        

