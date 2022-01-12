from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path("/create", views.CreateProjectView.as_view(), name="create"),
]