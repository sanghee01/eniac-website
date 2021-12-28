from django.shortcuts import render
from . import models
import projects
from django.core.paginator import Paginator



def home_projects(request):
    all_project = models.Project.objects.all()[:1]
    second_project = models.Project.objects.all()[1:2]
    return render(request, "home.html", context={"potato": all_project, "second": second_project})


def all_projects(request):
    page = request.GET.get("page")
    all_projects = models.Project.objects.all()
    paginator = Paginator(all_projects, 6)
    projects = paginator.get_page(page)
    return render(request, "projects/project_list.html", context={"projects": projects})


def create(request):
  # 생략
  models.Project.thumnail_img = request.FILES['thumnail_img']

