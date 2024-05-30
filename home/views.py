from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request):
    return HttpResponse("Hello World")


def index(request):
    return render(request, "home.html")
