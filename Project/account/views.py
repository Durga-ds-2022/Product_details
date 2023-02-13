from django.shortcuts import  render, redirect
from django.http import HttpResponse
from account.form import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect("home")

	form = NewUserForm
	return render (request, "register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("home")
		
	form = AuthenticationForm()
	return render(request, "login.html", context={"login_form":form})  


def logout_request(request):
	logout(request)
	
	return redirect("login")