from django.shortcuts import render
from . import models
import projects
from django.core.paginator import Paginator
from users import mixins as user_mixins
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from . import models, forms
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def home_projects(request):
    all_project = models.Project.objects.all()[:1]
    second_project = models.Project.objects.all()[1:2]
    return render(request, "home.html", context={"potato": all_project, "second": second_project})


def all_projects(request):
    page = request.GET.get("page")
    all_projects = models.Project.objects.all()
    paginator = Paginator(all_projects, 6)
    projects = paginator.get_page(page)

    fav_projects = models.Project.objects.filter(views="1")
    pages = Paginator(fav_projects, 6)
    fav_projects_all = pages.get_page(page)


    return render(request, "projects/project_list.html", context={"potato": projects, "fav": fav_projects_all})



class CreateProjectView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateProjectForm
    template_name = "projects/project_create.html"
    def form_valid(self, form):
        project = form.save()
        project.user = self.request.user
        project.save()
        # project.success(self.request, "Photo Uploaded")
        return redirect(reverse("core:project_list"))


class ProjectDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Project

class EditProjectView(UpdateView):

    model = models.Project
    template_name = "projects/project_edit.html"
    fields = (
        "title",
        "desc",
        "thumnail_img",
        "tag",
        "git",
   
    )



@login_required
def delete_project(request, project_pk):
    user = request.user
    try:
        room = models.Project.objects.get(pk=project_pk)
        # 현재 pk획득
        if room.host.pk != user.pk:
            # 이 pk user 랑 pk 가 다를경우 
            messages.error(request, "Cant delete that")
            # 에러메세지
        else:
            models.Project.objects.filter(pk=project_pk).delete()
            # pk 같은거 끼리 필터후 삭제
            messages.success(request, "Photo Deleted")
        return redirect(reverse("core:project", kwargs={"pk": project_pk}))
    except models.Project.DoesNotExist:
        return redirect(reverse("core:project_list"))