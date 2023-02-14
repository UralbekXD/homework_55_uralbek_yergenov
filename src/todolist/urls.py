from django.urls import path

from todolist.views import *

urlpatterns = [
    path('', index),
    path('task/', view_task)
]
