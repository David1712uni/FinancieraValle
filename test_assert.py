# app/tests.py

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import AsientoContable
from .forms import AsientoContableForm
from unittest.mock import patch
from django.contrib.auth import get_user_model


class ViewsTestCase(TestCase):
    
    def setUp(self):
        # Crear un usuario de prueba si es necesario para autenticación
        self.user = get_user_model().objects.create_user(username='testuser', password='password')

    def test_index_view_post_success(self):
        """Prueba para verificar si la vista index maneja correctamente un formulario válido."""
        # Simula el inicio de sesión
        self.client.login(username='testuser', password='password')
        
        # Realiza una solicitud POST con datos válidos para el formulario
        data = {
            'cuenta': '10',
            'monto': 1000,
            'tipo_monto': 'Debe',
            'glose': 'Prueba',
            'fecha': timezone.now().date()
        }
        
        response = self.client.post(reverse('index'), data)
        
        # Verifica si se redirige después de una solicitud POST exitosa
        self.assertRedirects(response, reverse('index'))
        
        # Verifica que se haya creado un nuevo asiento contable en la base de datos
        self.assertEqual(AsientoContable.objects.count(), 1)
        asiento = AsientoContable.objects.first()
        self.assertEqual(asiento.cuenta, 'AC')  # Asumiendo que '10' corresponde a 'AC'
        self.assertEqual(asiento.monto, 1000)

    def test_index_view_post_invalid_form(self):
        """Prueba para verificar la validación del formulario en la vista index."""
        # Simula el inicio de sesión
        self.client.login(username='testuser', password='password')
        
        # Realiza una solicitud POST con datos inválidos
        data = {
            'cuenta': '',
            'monto': '',
            'tipo_monto': '',
            'glose': '',
            'fecha': ''
        }
        
        response = self.client.post(reverse('index'), data)
        
        # Verifica que la vista devuelve el formulario con errores
        self.assertFormError(response, 'form', 'cuenta', 'Este campo es obligatorio.')
        self.assertFormError(response, 'form', 'monto', 'Este campo es obligatorio.')

    def test_index_view_get(self):
        """Prueba para verificar si la vista index devuelve el formulario correctamente con GET."""
        response = self.client.get(reverse('index'))
        
        # Verifica que la respuesta sea exitosa (código 200)
        self.assertEqual(response.status_code, 200)
        
        # Verifica que el formulario esté presente en el contexto
        self.assertContains(response, '<form')
        self.assertContains(response, 'cuenta')

    def test_get_tipo_cuenta_function(self):
        """Prueba la función get_tipo_cuenta."""
        from .views import get_tipo_cuenta
        tipo_cuenta = get_tipo_cuenta('10')
        self.assertEqual(tipo_cuenta, 'AC')

