from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterUser
from rest_framework.parsers import JSONParser
from api.views import register_view
from django.conf import settings
from django.views.generic import TemplateView



def index(request):
    # if request.user.is_authenticated:
    #     return redirect('dashboard')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass")
        user = authenticate(request, username= username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, 'loginPage.html', {'msg' :'Invalid username/password'})
        
    return render(request, 'loginPage.html')

def register(request):
    # if request.user.is_authenticated:
    #     return redirect('dashboard')
    if request.method == "POST":
        data = register_view(request)
        print(data)
    return render(request, 'registerPage.html')

def logoutPage(request):
    logout(request)
    return redirect('/')

