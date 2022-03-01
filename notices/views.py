from django.views import View
from . import models
from django.shortcuts import render
from django.core.paginator import Paginator
import activities
from users.models import User   
from django.db.models import Q
from notices.models import Notice

# Create your views here.

def all_notice(request):
    page = request.GET.get("page")
    all_notice = models.Notice.objects.all()
    paginator = Paginator(all_notice, 4)
    notices = paginator.get_page(page)
   
    return render(request,  "notices/notice.html", context={"notice": notices})


def search(request):
    products = None
    query = None
    if 'city' in request.GET: 
        query = request.GET.get('city') 
        products = models.Notice.objects.all().filter(Q(title__contains=query) | Q(desc__contains=query) | Q(tag__name__contains=query))
    
    return render(request, "notices/search.html", {"query": query, "products": products})