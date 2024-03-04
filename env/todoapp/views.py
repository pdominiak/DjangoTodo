from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import logging

from todoapp.models import Task
# Create your views here.

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def markAsDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.isCompleted = True
    task.save()
    return redirect('home')

def markAsUndone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.isCompleted = False
    task.save()
    return redirect('home')

def editTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        taskFromPOST = request.POST['task']
        task.task = taskFromPOST
        task.save()
        return redirect('home')
    else:
        context = {
            'task': task,
        }
        return render(request, 'edit_task.html', context=context)
   

def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')