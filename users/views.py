from django.views import View
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms
from . import models
from django.core.paginator import Paginator
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import auth
from django.contrib.auth.models import User  # User model 연결 


from django.views.generic import TemplateView
from django.views.generic.edit import CreateView # 오브젝트를 생성하는 뷰 (form 혹은 model과 연결되서 새로운 데이터를 넣을 때 CreateView - generic view를 사용)
# from django.contrib.auth.forms import UserCreationForm  >>  장고의 기본 회원가입 폼 (ID, PW만 확인한다 - 뒤에서 이메일 추가 커스터미아징 예정)




# Create your views here.

def login(request):
    # POST method 요청이 들어올떄 
    if request.method == 'POST':
        # 입력받은 아이디와 비밀번호가 데이터베이스에 있는지 확인한다. 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        # 해당 데이터의 유저가 있다면 
        if user is not None: 
            # 로그인하고 index로 리다이렉트한다. 
            auth.login(request, user)
            return redirect(reverse("core:project"))
        else:
            # 없다면, 에러를 표시하고, login페이지 로 이동(새로고침)
            return render(request, 'users/login.html', {'error': 'username or password is incorrect.'})
    else:
        # POST 요청이 아닐경우 login 페이지 새로고침
        return render(request, 'users/login.html')
        
def log_out(request):
    logout(request)
    return redirect(reverse("core:project"))


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:project_list")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        print(user)

        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

# def signup(request):
#     # 입력한 method 요청이 들어올 때
#     if request.method == 'POST':
#         # 입력한 password1과 password2가 같다면
#         if request.POST['password1'] == request.POST['password2']:
#             # 새로운 회원을 만들고
#             models.User.objects.create_user(request.POST['username'], password=request.POST['password1'], major=request.POST['major'], git_url=request.POST['git_url'])
#         # index로 돌아간다.
#         return redirect(reverse("core:project"))
#     #위의 경우가 아니면 그냥 signup 페이지를 다시 리턴한다.
#     return render(request, 'users/signup.html')
