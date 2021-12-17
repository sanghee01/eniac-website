from django.shortcuts import render
from . import models
import projects



def all_projects(request):
    all_project = models.Project.objects.all()[:3]
    return render(request, "home.html", context={"potato": all_project})

