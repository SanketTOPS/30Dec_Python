from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to Django Project!")

def about(request):
    return HttpResponse("This is About!")

def contact(request):
    return HttpResponse("This is Contact!")