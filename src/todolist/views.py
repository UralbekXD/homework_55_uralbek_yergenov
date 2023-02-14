from django.shortcuts import render

from todolist.models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }

    return render(request, 'index.html', context=tasks)
