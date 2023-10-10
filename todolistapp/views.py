from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from .models import Todo
from django.contrib import messages

# Create your views here.
def home (request) :
    
    _todos = Todo.objects.all();
    
 
    return  render(request, 'home.html', {'todos' : _todos})

def create(request):
    return  render(request, 'pages/todos/create.html')

def store(request):
    if request.method == 'POST' :
        Todo.objects.create(title=request.POST.get('title'), description=request.POST.get('description'))
        return redirect(to="home")
    return render(request, 'pages/todos/create.html')

def edit(request, todo_id):
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
        