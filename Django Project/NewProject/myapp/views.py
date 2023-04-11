from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request,'index.html',{'name':'Ashok'})

def about(request):
    return render(request,'about.html',{'num':random.randint(1111,9999)})

def contact(request):
    return render(request,'contact.html')