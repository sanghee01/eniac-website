from django.urls import path
from projects import views as project_view
from django.conf.urls.static import static
from django.conf.urls import  include, url
from django.conf import settings
from django.urls import path
from . import views


app_name = "activity"

urlpatterns = [path("activity/", views.ActivityView.as_view(), name="attend")]


