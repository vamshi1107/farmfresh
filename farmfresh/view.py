from django.http import *
from django.shortcuts import  *

def index(request):
    return render(request,"index.html")
