from django.urls import path
from projects import views as project_view
from django.conf.urls.static import static
from django.conf.urls import  include, url
from django.conf import settings
from django.urls import path
from . import views
from django.urls import reverse_lazy


app_name = "user"

urlpatterns = [path("login/", views.login, name="login"),
path("logout/", views.log_out, name="logout"),
path("signup", views.SignUpView.as_view(), name="signup"),
path("<int:pk>/profile", views.UserProfileView.as_view(), name="profile"),


path("email_verify/", views.email_verify, name="verify"),
path("verify/<str:key>", views.complete_verification, name="complete-verification"),

path('password_reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

path("sigupSec/", views.SignUpSecView.as_view(), name="signupSec"),
path("update-profile/", views.UpdateProfileView.as_view(), name="update"),
path("update-passwod/", views.UpdatePasswordView.as_view(success_url=reverse_lazy('core:project')), name="password"),
]


