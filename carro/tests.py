from django.test import TestCase, Client
from django.urls import reverse
from database.models import user, producto  # Se cambió `user` a `User` y `producto` a `Producto`
from carro.carro import carro as carroshop
from django.contrib.messages import get_messages
class CarroTestCase(TestCase):

    def setUp(self):
        """ Configuración inicial antes de cada prueba """
        self.client = Client()
        self.user = user.objects.create_user(username='testuser', password='password123')
        self.producto = producto.objects.create(  # Se cambió `producto` a `Producto`
            ID_producto=1,
            nombre_producto="Producto Test",
            descripcion="Descripción del producto",
            category="Electrónica",
            stock=10,
            precio_unitario=50000,
            calificacion=4
        )

    def test_carrito_redireccion_no_autenticado(self):
        """ Prueba que los usuarios no autenticados son redirigidos """
        response = self.client.get(reverse('carro:carrito'))
        self.assertRedirects(response, reverse('registrer:register'))

    def test_carrito_acceso_autenticado(self):
        """ Prueba que los usuarios autenticados pueden acceder al carrito """
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('carro:carrito'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'html/carrito/shopping_car.html')

    def test_agregar_producto_al_carrito(self):
        """ Prueba agregar un producto al carrito """
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('carro:agregar', args=[self.producto.ID_producto]))
        self.assertRedirects(response, reverse('carro:carrito'))

        # Se verifica si hay mensajes antes de acceder a ellos
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(str(messages[0]), "Producto agregado")

    def test_restar_producto_del_carrito(self):
        """ Prueba restar un producto del carrito """
        self.client.login(username='testuser', password='password123')
        self.client.get(reverse('carro:agregar', args=[self.producto.ID_producto]))
        response = self.client.get(reverse('carro:restar', args=[self.producto.ID_producto]))
        self.assertRedirects(response, reverse('carro:carrito'))

    def test_eliminar_producto_del_carrito(self):
        """ Prueba eliminar un producto del carrito """
        self.client.login(username='testuser', password='password123')
        self.client.get(reverse('carro:agregar', args=[self.producto.ID_producto]))
        response = self.client.get(reverse('carro:eliminar', args=[self.producto.ID_producto]))
        self.assertRedirects(response, reverse('carro:carrito'))

    def test_limpiar_carrito(self):
        """ Prueba limpiar el carrito """
        self.client.login(username='testuser', password='password123')
        self.client.get(reverse('carro:agregar', args=[self.producto.ID_producto]))
        response = self.client.get(reverse('carro:limpiar'))
        self.assertRedirects(response, reverse('carro:carrito'))

        messages_list = [str(m) for m in list(get_messages(response.wsgi_request))]
        self.assertTrue(messages_list, "No se encontraron mensajes")
        self.assertTrue(
            any(msg == "Carrito vaciado" for msg in messages_list),
            f"Se esperaba 'Carrito vaciado' en {messages_list}"
        )

    def test_comprar_carrito_con_productos(self):
        """ Prueba comprar cuando hay productos en el carrito """
        self.client.login(username='testuser', password='password123')
        self.client.get(reverse('carro:agregar', args=[self.producto.ID_producto]))
        response = self.client.get(reverse('carro:comprar'))
        self.assertRedirects(response, reverse('carro:carrito'))

        messages_list = [str(m) for m in list(get_messages(response.wsgi_request))]
        self.assertTrue(messages_list, "No se encontraron mensajes")
        self.assertTrue(
            any(msg == "Compra realizada con éxito" for msg in messages_list),
            f"Se esperaba 'Compra realizada con éxito' en {messages_list}"
        )

    def test_comprar_carrito_vacio(self):
        """ Prueba comprar sin productos en el carrito """
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('carro:comprar'))
        self.assertRedirects(response, reverse('carro:carrito'))

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)
        self.assertEqual(str(messages[0]), "No hay productos en el carrito para comprar")