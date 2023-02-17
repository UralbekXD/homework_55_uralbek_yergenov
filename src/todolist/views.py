from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from datetime import datetime
from todolist.models import Task


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
            context = {
                'status_choices': Task.STATUS_CHOICES,
                'time_now': datetime.today().strftime('%Y-%m-%d'),
            }
            return render(request, 'create.html', context=context)
        case 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            status = request.POST.get('status')
            deadline = request.POST.get('deadline')
            full_description = request.POST.get('full_description')

            task = Task.objects.create(
                title=title,
                description=description,
                status=status,
                deadline=deadline,
                full_description=full_description,
            )

            return redirect(reverse('task_view', kwargs={'pk': task.pk}))
