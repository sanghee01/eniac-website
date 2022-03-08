from django.views import View
from . import models
from django.shortcuts import render
from django.core.paginator import Paginator
import activities
from users.models import User   
from django.db.models import Q
from notices.models import Notice

# Create your views here.

def all_recommends(request):
    page = request.GET.get("page")
    all_recommends = models.Recommend.objects.all()
    paginator = Paginator(all_recommends, 20)
    web = paginator.get_page(page)

   

   
    
   
    return render(request,  "recommends/recommend_list.html", context={"potato": web})


