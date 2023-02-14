from django.urls import path

from todolist.views import *

urlpatterns = [
    path('', index),
]
