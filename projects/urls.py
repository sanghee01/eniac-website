from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path("<int:pk>/", views.ProjectDetail.as_view(), name="detail"),
    path("<int:pk>/edit", views.EditProjectView.as_view(), name="edit"),
    path("/create", views.CreateProjectView.as_view(), name="create"),

]