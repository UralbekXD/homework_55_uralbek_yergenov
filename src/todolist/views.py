from django.shortcuts import render, redirect
from datetime import datetime
from todolist.models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }

    return render(request, 'index.html', context=context)


def view_task(request):
    pk = request.GET.get('pk')
    task = Task.objects.get(pk=pk)
    context = {
        'task': task
    }

    return render(request, 'task.html', context=context)


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

            task = Task.objects.create(
                title=title,
                description=description,
                status=status,
                deadline=deadline,
            )

            return redirect('/task/?pk={primary_key}'.format(primary_key=task.pk))
