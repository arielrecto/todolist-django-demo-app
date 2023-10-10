from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from .models import Todo
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home (request) :
    
    _todos = Todo.objects.all();
    
 
    return  render(request, 'home.html', {'todos' : _todos})


# authentication

def signup(request):
    return render(request, 'pages/auth/register.html')

def store_user(request):   
    User.objects.create_user(username=request.POST.get('username'), email=request.POST.get('email'), password=request.POST.get('password'))
    messages.success(request, "Register Success!")
    return redirect(to='home')

def signin(request):
    
    if request.user.is_authenticated:
        return render(request, 'pages/home.html')
    return render(request, 'pages/auth/login.html')


def auth_user(request):
   
    user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None :
        login(request, user)
        return redirect(to='home')
    else:
        return redirect(to='login')


def signoff(request):
    logout(request)
    return redirect(to='home')


#todos

def create(request):
    if not request.user.is_authenticated:
        return redirect(to='login')
    
    print(request.user.is_authenticated)
   
    return render(request, 'pages/todos/create.html')

def store(request):
    
    if not request.user.is_authenticated:
        return redirect(to='login')
    
    if request.method == 'POST' :
        Todo.objects.create(title=request.POST.get('title'), description=request.POST.get('description'))
        return redirect(to="home")
    return render(request, 'pages/todos/create.html')

def edit(request, todo_id):
    if not request.user.is_authenticated:
        return redirect(to='login')
    
    _todo = Todo.objects.get(id=todo_id)
    return render(request, 'pages/todos/edit.html', {'todo' : _todo})

def update(request, todo_id):
    if(request.method == 'POST'):
        Todo.objects.filter(id=todo_id).update(title=request.POST.get('title'), description=request.POST.get('description'))
        messages.success( request, 'Data Updated!')
        return redirect(to='home')
    
    return redirect(to='edit/' + str(todo_id))


def delete(request, todo_id):
    if(request.method == 'POST'):
        Todo.objects.filter(id=todo_id).delete();
        messages.success(request, 'todo Delete success')
        return redirect(to='home')
    messages.error(request, 'something wrong')
    return redirect(to='home')          


       