from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()  # Obtiene el modelo de usuario definido en AUTH_USER_MODEL


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("registrer:register")

    def test_register_get(self):
        """Verifica que la vista carga correctamente con GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_register_post_success(self):
        """Prueba un registro exitoso"""
        response = self.client.post(self.url, {
            "username": "testuser",
            "email": "test@example.com",
            "password1": "TestPassword123!",
            "password2": "TestPassword123!"
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_register_post_fail(self):
        """Prueba un registro fallido por contraseñas que no coinciden"""
        response = self.client.post(self.url, {
            "username": "failuser",
            "email": "fail@example.com",
            "password1": "TestPassword123!",
            "password2": "WrongPassword!"
        })

        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="failuser").exists())
        self.assertContains(response, "registro no exitoso, compruebe la contraseña")  # Verifica el mensaje de error
