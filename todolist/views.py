from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
        else:
            messages.error(request, 'Error adding task!')
        return redirect('todolist')

    all_tasks = TaskList.objects.all()
    return render(request, 'todolist.html', {'tasks': all_tasks})


def delete_task(request, id):
    task = get_object_or_404(TaskList, id=id)
    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('todolist')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
