from django.test import TestCase, Client
from django.urls import reverse
from database.models import user  # Importa tu modelo personalizado


class AuthCustomUserTestCase(TestCase):

    def setUp(self):
        """ Configuración inicial antes de cada prueba """
        self.client = Client()
        self.username = 'testuser'
        self.password = 'password123'

        # Crear usuario con tu modelo personalizado
        self.user = user.objects.create_user(
            username=self.username,
            password=self.password,
            ciudad="Bogotá",
            direccion="Calle 123",
            codLogin="ABC123"
        )

    def test_login_correcto(self):
        """Prueba iniciar sesión con credenciales correctas"""
        response = self.client.post(reverse('accounts:login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)  # Redirección esperada
        self.assertRedirects(response, '/')  # Ahora espera redirección a '/'

    def test_login_incorrecto(self):
        """ Prueba iniciar sesión con credenciales incorrectas """
        response = self.client.post(reverse('accounts:login'), {
            'username': self.username,
            'password': 'claveincorrecta'
        })
        self.assertEqual(response.status_code, 200)  # La página se recarga con error
        self.assertFalse('_auth_user_id' in self.client.session)  # Verifica que NO se autenticó

    def test_logout(self):
        """Prueba cerrar sesión"""
        self.client.login(username=self.username, password=self.password)  # Iniciar sesión antes
        response = self.client.get(reverse('accounts:logout'))
        self.assertRedirects(response, '/')