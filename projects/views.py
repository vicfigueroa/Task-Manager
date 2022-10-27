from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm

# Create your views here.


@login_required
def list_projects(request):
    model_list = Project.objects.filter(owner=request.user)
    context = {"list_projects": model_list}
    return render(request, "projects/list.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form = form.save(False)
            form.purchaser = request.user
            form.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {"project_object": project}
    return render(request, "projects/detail.html", context)
