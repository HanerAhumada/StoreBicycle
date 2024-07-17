from django.shortcuts import render
# Create your views here.

def logueando(request):
    return render(request,'registration/login.html') 

