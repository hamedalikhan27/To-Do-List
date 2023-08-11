from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import TaskForm
# Create your views here.
def tasks_views(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'tasks':tasks , 'form':form}
    return render(request, 'list.html',context)

def update(request,pk):
    item = Task.objects.get(id=pk)

    form = TaskForm(instance=item)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'update.html',context)

def delete(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request,'delete.html',context)