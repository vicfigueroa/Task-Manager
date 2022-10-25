from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def list_projects(request):
    model_list = Project.objects.filter(owner=request.user)
    context = {"list_projects": model_list}
    return render(request, "projects/list.html", context)
