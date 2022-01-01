from django.views import View
from . import models
from django.shortcuts import render
from django.core.paginator import Paginator
import activities
from users.models import User

# Create your views here.

def all_notice(request):
    page = request.GET.get("page")
    all_notice = models.Notice.objects.all()
    paginator = Paginator(all_notice, 10)
    notices = paginator.get_page(page)

   
    return render(request,  "notices/notice.html", context={"notice": notices})