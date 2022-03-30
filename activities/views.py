from cProfile import label
from django.views import View
from . import models
from django.shortcuts import render
from django.core.paginator import Paginator
import activities
from users.models import User

from users import mixins as user_mixins
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from . import forms
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages 

from django.shortcuts import render, redirect, reverse
from users.models import User

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

    all_comment = models.Activity.objects.all()
    
    comment_form = forms.CreateCommentForm()
   
    return render(request,  "activities/activity.html", context={"act": activities,"potato":users,  "next_act": next_activities, "chall": challenges, "comment": all_comment, 'comment_form': comment_form})


class CreateChallengeView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms
    template_name = "activities/challenge_create.html"
    def form_valid(self, form):
        activity = form.save() 
        activity.user = self.request.user
        activity.save()
        # project.success(self.request, "Photo Uploaded")
        return redirect(reverse("core:project"))

# def create_ActComment(request, act):
#     if request.method == "POST":
#         form = forms.CreateCommentForm(request.POST)
#         # form등록
#         room = models.Activity.objects.get_or_none(pk=act)
#         if not room:
#             return redirect(reverse("core:project"))
#         if form.is_valid():
#             review = form.save()
#             review.desc = room
#             review.user = request.user
#             review.save()
#             messages.success(request, "Room reviewed")
#             return redirect(reverse("activity:activities", kwargs={"pk": room.pk}))


class CreateActivityView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateActivityForm
    template_name = "activities/activity-create.html"
    def form_valid(self, form):
        notice = form.save()
        notice.user = self.request.user
        notice.save()
        # project.success(self.request, "Photo Uploaded")
        return redirect(reverse("activity:activities"))

class CreateCommentView(user_mixins.LoggedInOnlyView, FormView):
    form_class = forms.CreateCommentForm
    template_name = "activities/activity.html"
    def form_valid(self, form):
        notice = form.save()
        notice.user = self.request.user
        notice.save()
        # project.success(self.request, "Photo Uploaded")
        return redirect(reverse("activity:activities"))


class EditActivityView(UpdateView): 

    model = models.Activity
    template_name = "activities/activity-edit.html"
    fields = (
       "title",
       "semester",
       "thumnail_img",
       "desc",
    )
    labels = {
        "title": "제목",
    }
  
    
    def get_success_url(self):
        return reverse("core:activity_list")



def comment_new(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(models.Activity, pk=pk)
        comment_form = forms.CreateCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.activities = article
          
            comment.user = request.user
            comment.save()
        return redirect('activity:activities', article.pk)
    return redirect('activity:activities')


