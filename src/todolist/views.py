from django.shortcuts import render

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

