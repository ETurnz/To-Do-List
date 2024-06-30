from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import TodoItem

@login_required
def index(request):
    todos = TodoItem.objects.filter(user=request.user)
    return render(request, 'todo/index.html', {'todos': todos})

@login_required
def add(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            TodoItem.objects.create(content=content, user=request.user)
        return redirect('index')

@login_required
def delete(request, todo_id):
    TodoItem.objects.filter(id=todo_id, user=request.user).delete()
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})
