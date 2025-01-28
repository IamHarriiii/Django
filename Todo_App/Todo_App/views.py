from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import TODO
from django.http import JsonResponse

def home(request):
    if request.user.is_authenticated:
        return redirect('todos')
    return redirect('login')

def signup(request):
    if request.user.is_authenticated:
        return redirect('todos')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')
            
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, 'Account created successfully!')
        return redirect('todos')
        
    return render(request, 'signup.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('todos')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('todos')
        else:
            messages.error(request, 'Invalid credentials')
            
    return render(request, 'login.html')

@login_required(login_url='login')
def todo_list(request):
    todos = TODO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo_list.html', {'todos': todos})

@login_required(login_url='login')
def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            TODO.objects.create(title=title, user=request.user)
            messages.success(request, 'Task added successfully!')
        return redirect('todos')

@login_required(login_url='login')
def delete_todo(request, todo_id):
    todo = get_object_or_404(TODO, id=todo_id, user=request.user)
    todo.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('todos')

@login_required(login_url='login')
def edit_todo(request, todo_id):
    todo = get_object_or_404(TODO, id=todo_id, user=request.user)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            todo.title = title
            todo.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('todos')
            
    return render(request, 'edit_todo.html', {'todo': todo})

@login_required(login_url='login')
def toggle_todo(request, todo_id):
    todo = get_object_or_404(TODO, id=todo_id, user=request.user)
    todo.status = not todo.status
    todo.save()
    return JsonResponse({'status': todo.status})

def logout_view(request):
    logout(request)
    return redirect('login')