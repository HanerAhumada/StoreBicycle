1. Crear un entorno virtual: python -m venv venv
2. Activar el entorno virtual: venv\Scripts\activate
3. Installar las dependencias: pip install -r requirements.txt
4. crear un archivo .env en la raiz del proyecto y crear 2 variables: DATABASE_URL= la direccion de la base de datos, HOST-ALLOW = 127.0.0.1
5. Hacer las migraciones: python manage.py makemigrations python manage.py migrate
6. crear un superusuario: python manage.py createsuperuser
7. iniciar el servicio: python manage.py runserver
