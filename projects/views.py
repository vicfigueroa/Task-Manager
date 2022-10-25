from django.shortcuts import render
from projects.models import Project

# Create your views here.


def list_projects(request):
    model_list = Project.objects.all()
    context = {"list_projects": model_list}
    return render(request, "projects/list.html", context)
