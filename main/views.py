from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, FileResponse

from main import models

# Create your views here.
@login_required
def main_page(request):
	return render(request, 'main.html')

def log_out(request):
	logout(request)
	return HttpResponseRedirect('/log_in/')
	
def log_in(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			return render(request, "login.html", {"text": "用户名或密码错误"})
	return render(request, "login.html")