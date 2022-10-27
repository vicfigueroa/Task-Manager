from django.shortcuts import render, redirect
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task

# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            # task.purchaser = request.user
            project.save()
            return redirect("show_my_tasks")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)


@login_required
def show_my_tasks(request):
    Model = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": Model,
    }
    return render(request, "tasks/list.html", context)
