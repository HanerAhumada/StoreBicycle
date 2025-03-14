# Proyecto Django

Este es un proyecto desarrollado en **Django 4.2.13** con **Python 3.9**. A continuación, se describen los pasos para instalar, configurar y ejecutar el proyecto.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.9.x** (https://www.python.org/downloads/)
- **pip** (administrador de paquetes de Python)
- **Virtualenv** (para gestionar entornos virtuales) `pip install virtualenv`
- **MySQL o PostgreSQL** (según la base de datos que vayas a usar)

## Instalación

1. Clonar el repositorio:
   ```sh
   git clone https://github.com/usuario/proyecto-django.git
   cd proyecto-django
   ```

2. Crear y activar un entorno virtual:
   ```sh
   python -m venv venv
   # En Windows
   venv\Scripts\activate
   # En macOS y Linux
   source venv/bin/activate
   ```

3. Instalar las dependencias del proyecto:
   ```sh
   pip install -r requirements.txt
   ```

## Configuración de Variables de Entorno

Este proyecto utiliza variables de entorno. Debes crear un archivo **`.env`** basado en **`.env.example`**.

1. Copiar el archivo de ejemplo:
   ```sh
   cp .env.example .env
   ```
2. Editar el archivo `.env` y configurar las credenciales de la base de datos.

Ejemplo de `.env`:
```env
DATABASE_URL=mysql://usuario:password@localhost:3306/nombre_basedatos
```

## Base de Datos

1. Crear la base de datos manualmente en MySQL o PostgreSQL.
2. Aplicar las migraciones:
   ```sh
   python manage.py migrate
   ```
3. Crear un superusuario para acceder al panel de administración:
   ```sh
   python manage.py createsuperuser
   ```

## Ejecutar el Servidor

Para iniciar el servidor de desarrollo de Django, usa el siguiente comando:
```sh
python manage.py runserver
```
El proyecto estará disponible en: **http://127.0.0.1:8000/**

## Dependencias

Este proyecto usa las siguientes dependencias:
```txt
asgiref==3.8.1
backports.zoneinfo==0.2.1
Brotli==1.1.0
click==8.1.7
colorama==0.4.6
dj-database-url==2.2.0
Django==4.2.13
gunicorn==22.0.0
h11==0.14.0
mysqlclient==2.2.4
numpy==1.24.4
packaging==24.1
pandas==2.0.3
pillow==10.4.0
psycopg2-binary==2.9.9
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pytz==2024.1
six==1.16.0
sqlparse==0.5.0
typing_extensions==4.12.2
tzdata==2024.1
uvicorn==0.30.1
whitenoise==6.7.0
```

## Despliegue en Producción

Para ejecutar el proyecto en un entorno de producción, se recomienda usar un servidor como **Gunicorn** junto con **Nginx** o **Whitenoise** para servir archivos estáticos.

Ejemplo de ejecución con Gunicorn:
```sh
 gunicorn --bind 0.0.0.0:8000 proyecto.wsgi:application
```

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

