from django.shortcuts import  render, redirect
from .forms import *
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request,"registro exitoso")
			return redirect("homepage")
		messages.error(request=request, message="regitro no exitoso, compruebe la contraseña" )
	form = NewUserForm()
	return render (request, "register.html")

