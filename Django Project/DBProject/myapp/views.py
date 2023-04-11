from django.shortcuts import render,redirect
from .forms import userinfoForm,updateinfo
from .models import userinfo

# Create your views here.

def index(request):
    if request.method=="POST":
        newuser=userinfoForm(request.POST)
        if newuser.is_valid(): #true
            newuser.save()
            print("Record inserted!")
        else:
            print(newuser.errors)
    return render(request,'index.html')

def showdata(request):
    data=userinfo.objects.all()
    return render(request,'showdata.html',{'data':data})

def deletedata(request,id):
    stid=userinfo.objects.get(id=id)
    userinfo.delete(stid)
    return redirect('showdata')

def updatedata(request,id):
    stid=userinfo.objects.get(id=id)
    if request.method=='POST':
        updatereq=updateinfo(request.POST)
        if updatereq.is_valid():
            updatereq=updateinfo(request.POST,instance=stid)
            updatereq.save()
            print("Your data has been updated!")
            return redirect('showdata')
        else:
            print(updatereq.errors)
    return render(request,'updatedata.html',{'stid':userinfo.objects.get(id=id)})

