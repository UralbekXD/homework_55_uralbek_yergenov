from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from datetime import datetime
from .models import Task, STATUS_CHOICES
from .forms import TaskForm


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }

    return render(request, 'index.html', context=context)


def view_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })


def create_task(request):
    match request.method:
        case 'GET':
            form = TaskForm()
            return render(request, 'create.html', context={
                'form': form,
                'status_choices': STATUS_CHOICES,
                'time_now': datetime.today().strftime('%Y-%m-%d'),
            })

        case 'POST':
            form = TaskForm(data=request.POST)
            if not form.is_valid():
                return render(request, 'create.html', context={
                    'form': form,
                    'status_choices': STATUS_CHOICES,
                    'time_now': datetime.today().strftime('%Y-%m-%d'),
                })

            task = Task.objects.create(**form.cleaned_data)
            return redirect(reverse('task_view', kwargs={'pk': task.pk}))


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    match request.method:
        case 'GET':
            form = TaskForm(
                data={
                    'title': task.title,
                    'description': task.description,
                    'full_description': task.full_description,
                    'status': task.status,
                    'deadline': task.deadline,
                }
            )
            return render(request, 'edit.html', context={
                'pk': task.pk,
                'form': form,
            })

        case 'POST':
            form = TaskForm(data=request.POST)
            if not form.is_valid():
                return render(request, 'edit.html', context={
                    'pk': task.pk,
                    'form': form,
                })

            return redirect(reverse('task_view', kwargs={'pk': pk}))


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')

