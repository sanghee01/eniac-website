from django.views import View
from . import models
from django.shortcuts import render
from django.core.paginator import Paginator
import activities
from users.models import User

# Create your views here.

def all_activity(request):
    page = request.GET.get("page")
    all_activities = models.Activity.objects.all()
    paginator = Paginator(all_activities, 6)
    activities = paginator.get_page(page)


    all_users = User.objects.all()
    paginator = Paginator(all_users, 20)
    users = paginator.get_page(page)

    return render(request,  "activities/activity.html", context={"act": activities, "user": users})