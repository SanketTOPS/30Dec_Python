from django.contrib import admin
from .models import userinfo

# Register your models here.

class userinfoAdmin(admin.ModelAdmin):
    list_display=['name','email','dob','mobile','address']

admin.site.register(userinfo,userinfoAdmin)