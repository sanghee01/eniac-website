from django.shortcuts import render
from . import models
import projects



def all_projects(request):
    all_project = models.Project.objects.all()[:1]
    second_project = models.Project.objects.all()[1:2]
    return render(request, "home.html", context={"potato": all_project, "second": second_project})


def create(request):
  # 생략
  models.Project.thumnail_img = request.FILES['thumnail_img']

