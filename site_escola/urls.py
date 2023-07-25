from django.urls import path
from site_escola.views import index, task, create_task


app_name = 'site_escola'

urlpatterns = [
    path('', index.teste, name='index'),
    path('task', task.taskviews, name='task'),
    path('create_task', create_task.createtask, name='create_task'),
]