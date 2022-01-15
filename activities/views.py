from django.views import View
from . import models
from django.shortcuts import render
from django.core.paginator import Paginator
import activities
from users.models import User
from challenges.models import Challenge

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

    all_challenges = Challenge.objects.all().order_by("-created")
    paginator = Paginator(all_challenges, 6)
    challenges = paginator.get_page(page)



    return render(request,  "activities/activity.html", context={"act": activities,"potato":users,  "next_act": next_activities, "chall": challenges})