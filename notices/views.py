from django.views import View
from . import models
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, View, UpdateView, FormView, DeleteView
import activities
from users.models import User   
from django.db.models import Q
from notices.models import Notice
from . import models, forms
from users import mixins as user_mixins
from django.shortcuts import render, redirect, reverse
from users.models import User

# Create your views here.

def all_notice(request):
    page = request.GET.get("page")
    all_notice = models.Notice.objects.all()
    paginator = Paginator(all_notice, 4)
    notices = paginator.get_page(page)
    all_user = User.objects.filter(is_superuser=True)
    return render(request,  "notices/notice.html", context={"notice": notices, "superhost": all_user})


class CreateNoticetView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateNoticeForm
    template_name = "notices/notice-creates.html"
    def form_valid(self, form):
        notice = form.save()
        notice.user = self.request.user
        notice.save()
        # project.success(self.request, "Photo Uploaded")
        return redirect(reverse("core:notice_list"))
        


def search(request):
    products = None
    query = None
    if 'city' in request.GET: 
        query = request.GET.get('city') 
        products = models.Notice.objects.all().filter(Q(title__contains=query) | Q(desc__contains=query) | Q(tag__name__contains=query))
    return render(request, "notices/search.html", {"query": query, "products": products})





class NoticeDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Notice



class EditNoticeView(UpdateView):

    model = models.Notice
    template_name = "notices/notice_edit.html"
    fields = (
        "title",
        "thumnail_img",
        "img_a",
        "img_b",
        "img_c",
        "desc",
        "tag",
    )
    def get_success_url(self):
        return reverse("core:notice_list")



class DeletNoticeView(DeleteView): # DeleteView를 임포트하는것 잊지마세요.
    model = models.Notice
    template_name = "notices/notice-delete.html"
    def get_success_url(self):
        return reverse("core:notice_list")
    


