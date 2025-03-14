from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('', include('django.contrib.auth.urls')),  # Incluye las rutas de autenticación de Django
]