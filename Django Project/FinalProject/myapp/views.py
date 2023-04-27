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
            userid=userSignup.objects.get(username=unm)
            print("UserID:",userid.id)
            if user: #true
                print("Login Successfull!")
                request.session['user']=unm
                request.session['uid']=userid.id
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
    user=request.session.get('user')
    uid=request.session.get('uid')
    cuser=userSignup.objects.get(id=uid)
    if request.method=='POST':
        updateReq=signupForm(request.POST)
        if updateReq.is_valid():
            updateReq=signupForm(request.POST,instance=cuser)
            updateReq.save()
            print('Your Profile has been updated!')
            return redirect('notes')
        else:
            print(updateReq.errors)
    return render(request,'profile.html',{'user':user,'cuser':userSignup.objects.get(id=uid)})

def userlogout(request):
    logout(request)
    return redirect('/')