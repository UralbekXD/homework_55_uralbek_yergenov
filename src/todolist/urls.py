from django.urls import path

from todolist.views import *

urlpatterns = [
    path('', index, name='index'),
    path('task/<int:pk>', view_task, name='task_view'),
    path('task/add/', create_task, name='task_create'),
]
