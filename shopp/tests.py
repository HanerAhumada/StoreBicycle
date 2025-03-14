from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from carro.carro import carro as carroshop
from unittest.mock import patch
from shopp.shopp import shoppUser

User = get_user_model()


class RegistrarComprasTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('shopp:comprar')

    def test_acceso_sin_autenticacion(self):
        """Un usuario no autenticado debe ser redirigido al login"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)  # Redirección esperada
        self.assertTrue(response.url.startswith('/accounts/login/'))  # Django redirige a login

    def test_acceso_con_autenticacion_get(self):
        """Un usuario autenticado puede ver el formulario de compra"""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)  # Renderiza la página correctamente
        self.assertTemplateUsed(response, 'html/shopp/compras.html')

    @patch.object(shoppUser, 'crear_factura')
    @patch.object(carroshop, 'devolver_datos', return_value={'producto1': 2, 'producto2': 1})
    def test_proceso_compra_exitoso(self, mock_carro, mock_crear_factura):
        """Un usuario autenticado puede registrar una compra correctamente"""
        self.client.login(username='testuser', password='testpassword')
        data = {
            'ciudad': 'Bogotá',
            'nombre': 'Juan',
            'apellido': 'Pérez',
            'correo': 'juan@example.com',
            'telefono': '1234567890',
            'direccion': 'Calle 123'
        }
        response = self.client.post(self.url, data)

        # Asegurarse de que la factura fue creada
        mock_crear_factura.assert_called_once_with(
            self.user, {'producto1': 2, 'producto2': 1},
            ciudad='Bogotá', nombre='Juan', apellido='Pérez',
            correo='juan@example.com', telefono='1234567890',
            direccion='Calle 123'
        )

        # Asegurar redirección a 'homepage'
        self.assertRedirects(response, reverse('homepage'))