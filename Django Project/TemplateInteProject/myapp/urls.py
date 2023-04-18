from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('booking/',views.booking),
    path('team/',views.team),
    path('testimonial/',views.testimonial),
    path('service/',views.service),
    path('menu/',views.menu),
]