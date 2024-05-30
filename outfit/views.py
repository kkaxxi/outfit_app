from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def outfit_view(request):
    return HttpResponse("Hello Outfit")


