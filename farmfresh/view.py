from django.http import *
from django.shortcuts import  *

def index(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")
