from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from Todo_App import models
from Todo_App.models import TODO
from django.contrib.auth import authenticate,login,logout

def signup(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        email_id=request.POST.get('email')
        pwd=request.POST.get('pwd')
        my_user = User.objects.create_user(fnm,email_id,pwd)
        my_user.save()
        return redirect('/login')
    
    return render(request,'signup.html')


def login(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        user=authenticate(request,username=fnm,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('/todo')
        else:
            return redirect('/login')

    return render(request,'login.html')