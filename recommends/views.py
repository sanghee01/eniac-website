from django.views import View
from . import models
from django.shortcuts import render
from django.core.paginator import Paginator
import activities
from users.models import User   
from django.db.models import Q
from notices.models import Notice
from users.models import User   
from django.db.models import Q
from notices.models import Notice
from . import forms
from users import mixins as user_mixins
from django.shortcuts import render, redirect, reverse
from users.models import User
from django.views.generic import ListView, DetailView, View, UpdateView, FormView


# Create your views here.

def all_recommends(request):
    page = request.GET.get("page")
    all_recommends = models.Recommend.objects.all()
    paginator = Paginator(all_recommends, 20)
    web = paginator.get_page(page)
   
    return render(request,  "recommends/recommend_list.html", context={"potato": web})




class CreateRecommendView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateNoticeForm
    template_name = "recommends/recom-create.html"
    def form_valid(self, form):
        recommend = form.save()
        recommend.user = self.request.user
        recommend.save()
        # project.success(self.request, "Photo Uploaded")
        return redirect(reverse("core:recommend_list"))


class EditRecommendView(UpdateView):

    model = models.Recommend
    template_name = "recommends/recom-edit.html"
    fields = (
        "title",
        "desc",
        "img",
        "genre",
        "level",
        "lead",
    )
    def get_success_url(self):
        return reverse("core:recommend_list")
