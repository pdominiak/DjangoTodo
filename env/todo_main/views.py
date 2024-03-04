from django.http import HttpResponse
from django.shortcuts import render
from todoapp.models import Task

def home(request):
    tasks = Task.objects.filter(isCompleted=False).order_by('updatedAt').reverse()
    completedTasks = Task.objects.filter(isCompleted=True)
    context = {
        'tasks' : tasks,
        'completedtasks': completedTasks
    }
    return render(request, 'home.html',context)