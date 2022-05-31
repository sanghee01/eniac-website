from cProfile import label
from django.views import View
from . import models
from django.shortcuts import render
from django.core.paginator import Paginator
import activities
from users.models import User
from users import mixins as user_mixins
from django.views.generic import ListView, DetailView, View, UpdateView, FormView, DeleteView
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

    form_class = forms.CreateChallengeForm
    template_name = "activities/challenge_create.html"
    def form_valid(self, form):
        notice = form.save()
        notice.user = self.request.user
        notice.save()
        # project.success(self.request, "Photo Uploaded")
        return redirect(reverse("activity:activities"))



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
       "img_a",   
       "img_b", 
       "img_c", 
       "desc",
    )
    labels = {
        "title": "제목",
    }
    def get_success_url(self):
        return reverse("core:activity_list")

    


def comment_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(models.Activity, pk=pk)
        comment_form = forms.CreateCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) 
            # 바로 저장하지는 않겠다
            comment.activity = article
            comment.user = request.user
            comment.save()
        return redirect('activity:detail', article.pk)
    return redirect('user:login')



class DetailActivity(DetailView):
    model = models.Activity
    def get_context_data(self, **kwargs):
        # 기본 구현을 호출해 context를 가져온다.
        context = super(DetailActivity, self).get_context_data(**kwargs)
        # 여기에 각자 id를 어떻게 내보내지?
        context['form'] = forms.CreateCommentForm(initial={
            'text': '댓글을 입력해주세요.',	# textfield에 value값 설정.
        })
        abc = models.Activity.objects.filter(id=self.kwargs['pk'])[0]
        # 모든 책을 쿼리한 집합을 context 객체에 추가한다.
        context['comment'] = abc.comm.all()
        return context 


class DeleteActivityView(DeleteView): # DeleteView를 임포트하는것 잊지마세요.
    model = models.Activity
    template_name = "activities/activity-delete.html"
    def get_success_url(self):
        return reverse("core:activity_list")
    

                                                                  