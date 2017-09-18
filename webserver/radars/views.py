from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    print("Hello World")
    return HttpResponse("Hello, world. You're at the radars index.")