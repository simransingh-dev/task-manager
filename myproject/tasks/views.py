from django.shortcuts import render, redirect
from .models import Task

def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect('/')

    tasks = Task.objects.all()
    return render(request, "tasks/index.html", {"tasks": tasks})


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')

def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed
    task.save()
    return redirect('/')

def edit_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == "POST":
        task.title = request.POST.get("title")
        task.save()
        return redirect('/')

    return render(request, "tasks/edit.html", {"task": task})