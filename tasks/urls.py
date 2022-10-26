from django.urls import path
from tasks.views import create_task, show_tasks

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_tasks, name="show_my_tasks"),
]
