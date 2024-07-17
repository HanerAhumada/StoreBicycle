from urllib import request
from django.urls import path
from . import views

app_name = 'registrer'

urlpatterns = [
    path("", views.register_request,name='register'),
]
