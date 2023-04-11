from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('usersignup/',views.usersignup),
    path('home/',views.home,name='home'),
    path('userlogout/',views.userlogout),
]