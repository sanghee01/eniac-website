from django.views import View
from . import models
from django.shortcuts import render
from django.core.paginator import Paginator
import activities
from users.models import User

from users import mixins as user_mixins
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from . import forms
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.

def all_activity(request):
    page = request.GET.get("page")
    all_activities = models.Activity.objects.filter(semester="1학기")
    paginator = Paginator(all_activities, 3)
    activities = paginator.get_page(page)
    
    all_users = User.objects.all().order_by('-date_joined')
    paginator = Paginator(all_users, 40)
    users = paginator.get_page(page)

    next_all_activities = models.Activity.objects.filter(semester="2학기")
    paginator = Paginator(next_all_activities, 6)
    next_activities = paginator.get_page(page)

    all_challenges = models.Challenge.objects.all().order_by("-created")
    paginator = Paginator(all_challenges, 6)
    challenges = paginator.get_page(page)


    return render(request,  "activities/activity.html", context={"act": activities,"potato":users,  "next_act": next_activities, "chall": challenges})


class CreateChallengeView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms
    template_name = "activities/challenge_create.html"
    def form_valid(self, form):
        activity = form.save() 
        activity.user = self.request.user
        activity.save()
        # project.success(self.request, "Photo Uploaded")
        return redirect(reverse("core:project"))

def create_ActComment(request, act):
    if request.method == "POST":
        form = forms.CreateCommentForm(request.POST)
        # form등록
        room = models.Activity.objects.get_or_none(pk=act)
        if not room:
            return redirect(reverse("core:project"))
        if form.is_valid():
            review = form.save()
            review.desc = room
            review.user = request.user
            review.save()
            messages.success(request, "Room reviewed")
            return redirect(reverse("activity:activities", kwargs={"pk": room.pk}))