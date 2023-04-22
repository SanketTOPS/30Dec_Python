from django.shortcuts import render,redirect
from .forms import signupForm,notesForm
from .models import userSignup
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST': #root
        if request.POST.get('signup')=='signup': #child - signup
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("User created!")
                return redirect('/')
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login': #child - login
            unm=request.POST['username']
            pas=request.POST['password']

            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfull!")
                request.session['user']=unm
                return redirect('notes')
            else:
                print("Error!Try again")
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        newnotes=notesForm(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Your notes has been submitted!")
        else:
            print(newnotes.errors)
    return render(request,'notes.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def profile(request):
    return render(request,'profile.html')

def userlogout(request):
    logout(request)
    return redirect('/')