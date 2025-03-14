from django.test import TestCase
from django.urls import reverse
from database.models import producto
from django.core.files.uploadedfile import SimpleUploadedFile


class InventarioViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear productos de prueba con nombres de atributos correctos
        cls.producto1 = producto.objects.create(
            nombre_producto="Bicicleta Montaña",
            precio_unitario=500,
            category="Montaña",  # Asegurar que coincide con el modelo
            stock=5,
            descripcion="Bicicleta ideal para terrenos difíciles",
            imagen=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        )
        cls.producto2 = producto.objects.create(
            nombre_producto="Bicicleta Ruta",
            precio_unitario=800,
            category="Ruta",
            stock=3,
            descripcion="Bicicleta rápida para carretera",
            imagen=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        )

    def test_inventario_filtro_todos(self):
        """Debe retornar todos los productos cuando el filtro es 'all'."""
        response = self.client.get(reverse('shopping:tienda', args=['all']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bicicleta Montaña")
        self.assertContains(response, "Bicicleta Ruta")

    def test_inventario_filtro_categoria(self):
        """Debe filtrar productos por categoría."""
        response = self.client.get(reverse('shopping:tienda', args=['Montaña']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bicicleta Montaña")
        self.assertNotContains(response, "Bicicleta Ruta")
