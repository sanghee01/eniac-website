from django.urls import path
from projects import views as project_view
from django.conf.urls.static import static
from django.conf.urls import  include, url
from django.conf import settings
from django.urls import path
from . import views


app_name = "user"

urlpatterns = [path("login/", views.login, name="login"),
path("logout/", views.log_out, name="logout"),
path("signup", views.SignUpView.as_view(), name="signup"),
path("<int:pk>/profile", views.UserProfileView.as_view(), name="profile"),
]


