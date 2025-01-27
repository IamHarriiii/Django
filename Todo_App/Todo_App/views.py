from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Todo_App import models
from Todo_App.models import TODO

@login_required(login_url='/loginn')
def home(request):
    return render(request, 'signup.html')

# Signup view
def signupp(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        my_user = User.objects.create_user(username=fnm, email=emailid, password=pwd)
        my_user.save()
        return redirect('/loginn')
    
    return render(request, 'signup.html')

def loginn(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        userr = authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            login(request, userr)
            return redirect('/todopage')
        else:
            return redirect('/loginn')

    return render(request, 'login.html')

@login_required(login_url='/loginn')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        obj = models.TODO(title=title, user=request.user)
        obj.save()
        return redirect('/todopage')

    res = models.TODO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res})

# Delete todo
def delete_todo(request, srno):
    obj = models.TODO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todopage')

# Edit todo
@login_required(login_url='/loginn')
def edit_todo(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        obj = models.TODO.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect('/todopage')

    obj = models.TODO.objects.get(srno=srno)
    return render(request, 'edit_todo.html', {'obj': obj})

# Logout view
def signout(request):
    logout(request)
    return redirect('/loginn')
