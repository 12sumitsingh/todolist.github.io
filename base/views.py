from django.forms.models import ModelForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def Loginuser(request):
    user_count = User.objects.count()
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get('username')
        except:
            messages.error(request, 'User does not exists')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('task-list')
        else:
            messages.error(request, 'Username or password does not exists')
    context = {'page': page, 'user_count': user_count}
    return render(request, 'base/login.html', context)

def Logoutuser(request):
    logout(request)
    return redirect('task-list')

def registeruser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('task-list')
        else:
            messages.error(request, 'an error is occured during registration')
    context = {'form': form}
    return render(request, 'base/login.html', context)


@login_required(login_url='login')
def taskList(request):
   


    if request.user.is_authenticated:
        user = request.user
        task = Task.objects.filter(user = user)

    
    
        context = {'task': task}
        return render(request, 'base/tasklist.html', context)


@login_required(login_url='login')
def taskView(request, pk):
    task = Task.objects.get(id=pk)
    context = {'task': task}
    return render(request, 'base/taskview.html', context)


@login_required(login_url='login')
def createTask(request):
    if request.user.is_authenticated:
        user = request.user
        
        form = TaskForm()
    
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            todo = form.save(commit = False)
            todo.user = user
            todo.save() 
            return redirect('task-list')


    context = {'form': form}
    return render(request, 'base/task_form.html', context)

 
@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    context = {'form': form}
    return render(request, 'base/task_form.html', context)


@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
        
    
    return render(request, 'base/delete.html', {'obj': task})